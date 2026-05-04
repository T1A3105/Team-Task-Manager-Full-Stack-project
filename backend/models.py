from extensions import db

# =========================
# MANY-TO-MANY RELATIONSHIP
# =========================
project_members = db.Table(
    "project_members",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("project_id", db.Integer, db.ForeignKey("project.id"))
)

# =========================
# USER MODEL
# =========================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.LargeBinary(200))
    role = db.Column(db.String(20))

    projects = db.relationship(
        "Project",
        secondary=project_members,
        back_populates="members"
    )

# =========================
# PROJECT MODEL
# =========================
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    owner_id = db.Column(db.Integer)

    members = db.relationship(
        "User",
        secondary=project_members,
        back_populates="projects"
    )

# =========================
# TASK MODEL
# =========================
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.String(20))
    project_id = db.Column(db.Integer)
    assigned_to = db.Column(db.Integer)