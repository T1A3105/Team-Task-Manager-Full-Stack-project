const API = "http://localhost:5000";

// 🔐 SIGNUP
async function signup() {
  await fetch(API + "/signup", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      username: su_user.value,
      password: su_pass.value,
      role: su_role.value
    })
  });
  alert("Signup done");
}

// 🔐 LOGIN
async function login() {
  const res = await fetch(API + "/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      username: li_user.value,
      password: li_pass.value
    })
  });

  const data = await res.json();
  localStorage.setItem("token", data.token);

  window.location = "dashboard.html";
}

// 📁 CREATE PROJECT
async function createProject() {
  await fetch(API + "/projects", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + localStorage.token
    },
    body: JSON.stringify({ name: project_name.value })
  });
  alert("Project created");
}

// 📝 CREATE TASK
async function createTask() {
  await fetch(API + "/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + localStorage.token
    },
    body: JSON.stringify({
      title: task_title.value,
      project_id: project_id.value,
      assigned_to: assign_id.value
    })
  });
  alert("Task created");
}

// 📊 LOAD TASKS
async function loadData() {
  const res = await fetch(API + "/tasks", {
    headers: {
      "Authorization": "Bearer " + localStorage.token
    }
  });

  const data = await res.json();

  tasks.innerHTML = "";
  data.forEach(t => {
    tasks.innerHTML += `
      <li>
        ${t.title} - ${t.status}
        <button onclick="updateTask(${t.id})">Done</button>
      </li>
    `;
  });
}

// ✅ UPDATE TASK
async function updateTask(id) {
  await fetch(API + "/tasks/" + id, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + localStorage.token
    },
    body: JSON.stringify({ status: "completed" })
  });

  loadData();
}