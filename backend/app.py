from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from datetime import datetime

from extensions import db
from models import User, Project, Task
import bcrypt

# ========================
# APP CONFIG
# ========================
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///teamtask.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# ========================
# INIT EXTENSIONS
# ========================
db.init_app(app)
jwt = JWTManager(app)
CORS(app)

# ========================
# CREATE TABLES
# ========================
with app.app_context():
    db.create_all()

# ========================
# HOME
# ========================
@app.route("/")
def home():
    return jsonify({"message": "Team Task Manager API Running 🚀"})

# ========================
# SIGNUP
# ========================
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"msg": "User already exists"}), 400

    hashed = bcrypt.hashpw(
        data["password"].encode("utf-8"),
        bcrypt.gensalt()
    )

    user = User(
        username=data["username"],
        password=hashed,
        role=data.get("role", "member")
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201

# ========================
# LOGIN
# ========================
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if user and bcrypt.checkpw(
        data["password"].encode("utf-8"),
        user.password
    ):
        token = create_access_token(
            identity={"id": user.id, "role": user.role}
        )
        return jsonify({"token": token})

    return jsonify({"msg": "Invalid credentials"}), 401

# ========================
# CREATE PROJECT
# ========================
@app.route("/projects", methods=["POST"])
@jwt_required()
def create_project():
    user = get_jwt_identity()
    data = request.get_json()

    if user["role"] != "admin":
        return jsonify({"msg": "Access denied"}), 403

    project = Project(
        name=data["name"],
        owner_id=user["id"]
    )

    db.session.add(project)
    db.session.commit()

    return jsonify({"msg": "Project created"}), 201

# ========================
# ADD MEMBER TO PROJECT
# ========================
@app.route("/projects/<int:project_id>/add-member", methods=["POST"])
@jwt_required()
def add_member(project_id):
    data = request.get_json()

    user = User.query.get(data["user_id"])
    project = Project.query.get(project_id)

    if not user or not project:
        return jsonify({"msg": "User or Project not found"}), 404

    project.members.append(user)
    db.session.commit()

    return jsonify({"msg": "User added to project"})

# ========================
# VIEW PROJECT MEMBERS
# ========================
@app.route("/projects/<int:project_id>/members", methods=["GET"])
@jwt_required()
def get_members(project_id):
    project = Project.query.get(project_id)

    return jsonify([
        {"id": u.id, "username": u.username}
        for u in project.members
    ])

# ========================
# GET PROJECTS
# ========================
@app.route("/projects", methods=["GET"])
@jwt_required()
def get_projects():
    projects = Project.query.all()

    return jsonify([
        {"id": p.id, "name": p.name}
        for p in projects
    ])

# ========================
# CREATE TASK
# ========================
@app.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    data = request.get_json()

    task = Task(
        title=data["title"],
        status="pending",
        project_id=data["project_id"],
        assigned_to=data["assigned_to"]
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"msg": "Task created"}), 201

# ========================
# GET TASKS
# ========================
@app.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()

    return jsonify([
        {"id": t.id, "title": t.title, "status": t.status}
        for t in tasks
    ])

# ========================
# UPDATE TASK
# ========================
@app.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required()
def update_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"msg": "Task not found"}), 404

    data = request.get_json()
    task.status = data.get("status", task.status)

    db.session.commit()

    return jsonify({"msg": "Updated successfully"})

# ========================
# DASHBOARD
# ========================
@app.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    tasks = Task.query.all()

    total = len(tasks)
    completed = len([t for t in tasks if t.status == "completed"])
    pending = len([t for t in tasks if t.status == "pending"])

    return jsonify({
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending
    })

# ========================
# FILTER TASKS
# ========================
@app.route("/tasks/filter/<status>", methods=["GET"])
@jwt_required()
def filter_tasks(status):
    tasks = Task.query.filter_by(status=status).all()

    return jsonify([
        {"id": t.id, "title": t.title, "status": t.status}
        for t in tasks
    ])

# ========================
# OVERDUE TASKS
# ========================
@app.route("/tasks/overdue", methods=["GET"])
@jwt_required()
def overdue_tasks():
    today = datetime.today().date()

    tasks = Task.query.filter(
        Task.status != "completed"
    ).all()

    return jsonify([
        {"id": t.id, "title": t.title}
        for t in tasks
    ])

# ========================
# RUN APP
# ========================
if __name__ == "__main__":
    app.run(debug=True)