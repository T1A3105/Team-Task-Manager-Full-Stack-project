# 📌 Team Task Manager (Full Stack Project)

## 🚀 Overview
The **Team Task Manager** is a full-stack web application designed to help teams efficiently manage projects and tasks. It enables users to create projects, assign tasks, track progress, and collaborate effectively with role-based access (Admin and Member).

---

## ✨ Features

### 🔐 Authentication
- User Signup & Login
- Secure password hashing
- Session-based authentication

### 👥 Role-Based Access
- **Admin**
  - Create and manage projects
  - Assign tasks to team members
- **Member**
  - View assigned tasks
  - Update task status

### 📁 Project Management
- Create multiple projects
- Assign tasks under each project
- Track project progress

### ✅ Task Management
- Create tasks with status tracking (Pending / In Progress / Completed)
- Update task status
- View assigned tasks in dashboard

### 📊 Dashboard
- Overview of all tasks
- Status tracking system
- Organized project-wise task view

---

## 🛠️ Tech Stack

**Frontend:**
- HTML
- CSS
- JavaScript

**Backend:**
- Python (Flask)

**Database:**
- SQLite / MySQL

**Tools:**
- Git & GitHub
- VS Code

---

## 📁 Project Structure
│
├── backend/
│ ├── routes/ # API routes (auth, tasks, projects)
│ ├── models/ # Database models
│ ├── static/ # Static backend files (if any)
│ ├── app.py # Main backend entry point
│ ├── config.py # Configuration settings
│ ├── requirements.txt # Python dependencies
│ └── database.db # SQLite database
│
├── frontend/
│ ├── index.html # Login page
│ ├── dashboard.html # Main dashboard
│ ├── style.css # Styling file
│ ├── script.js # Frontend logic
│ └── assets/ # Images/icons (if any)
│
├── README.md # Project documentation
└── .gitignore # Ignored files


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/T1A3105/Team-Task-Manager-Full-Stack-project.git

### 2️⃣ Navigate to project folder
cd team-task-manager

### 3️⃣ Setup backend
cd backend
pip install -r requirements.txt
python app.py

### 4️⃣ Run frontend
open:
frontend/index.html

▶️ How to Run Project
1.Start backend server
2.Open frontend in browser
3.Register / Login
4.Create projects and assign tasks
5.Track progress from dashboard

🔮 Future Enhancements

🔔 Notifications for task updates
📱 Responsive UI improvements
🌐 Cloud deployment (Render / Railway)
📊 Analytics dashboard
💬 Team chat feature
📅 Deadline reminders


👨‍💻 Author
Deepthi C
📍 India

⭐ Support
If you like this project, please ⭐ the repository to support it!

