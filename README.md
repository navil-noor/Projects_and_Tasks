# 🚀 Projects & Tasks API
A containerized FastAPI application for managing projects and tasks with a Many-to-Many relationship. This project demonstrates modern backend patterns, including database resilience, many-to-many link tables, and full containerization.

## 🛠️ Tech Stack
- **Framework:** FastAPI
- **ORM:** SQLModel (SQLAlchemy + Pydantic)
- **Database:** PostgreSQL (Production) / SQLite (Local Development)
- **Containerization:** Docker & Docker Compose
- **Server:** Uvicorn

## ✨ Key Features
- **Full CRUD:** Create, Read, Update, and Delete for both Projects and Tasks.
- **Many-to-Many Logic:** Link multiple tasks to multiple projects via a dedicated ProjectTaskLink model.
- **Smart Filtering:**
  - Retrieve all tasks associated with a specific project.
  - Search for tasks using specific tags.
- **Database Resilience:** Custom retry logic in the startup sequence to ensure the app waits for the PostgreSQL service to be fully ready.
- **Automatic Docs:** Fully interactive API documentation via Swagger UI.

## 🚀 How to Run
### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### Quick Start
1. Clone the repository to your local machine.
2. Open a terminal in the project folder.
3. Run the following command:
```bash
docker-compose up --build
```
Once the logs show Uvicorn running on [http://0.0.0.0:8000](http://0.0.0.0:8000), the app is ready!

### Accessing the API
- Interactive Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternative Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📁 Project Structure
| File | Description |
| --- | --- |
| main.py | API endpoints and application lifecycle logic |
| models.py | SQLModel definitions for Project, Task, and the ProjectTaskLink table |
| db.py | Database engine configuration and session management (including connection retry logic) |
| Dockerfile | Instructions for building the Python environment |
| docker-compose.yml | Orchestration for the FastAPI app and PostgreSQL database |

## 🧪 Example Workflow
1. Create a Project: `POST /projects`
2. Create a Task: `POST /tasks` (add tags like "urgent,work")
3. Link Task to Project: `POST /projects/{project_id}/task/{task_id}`
4. View Project Progress: `GET /projects/{project_id}/tasks`

## 🕹️ Detailed Start Guide (Testing the API)

Once your containers are running, the best way to test the system is through the **Interactive Swagger UI**.

### 1. Open the API Lab
Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) in your browser. This interface allows you to send real data to your database without writing any frontend code.

### 2. Step-by-Step Walkthrough

#### **Step A: Create a Project**
* Find the **POST `/projects`** endpoint and click **"Try it out"**.
* Use this example JSON and click **Execute**:
    ```json
    {
      "name": "Apollo 11",
      "budget": 50000,
      "description": "Moon landing mission",
      "hours_used": 0
    }
    ```
* **Note:** Keep track of the `"id"` in the response (usually `1`).

#### **Step B: Create a Task**
* Find the **POST `/tasks`** endpoint and click **"Try it out"**.
* Use this example JSON and click **Execute**:
    ```json
    {
      "title": "Build Rocket",
      "description": "Assemble the main boosters",
      "tags": "engineering,urgent"
    }
    ```
* **Note:** Keep track of this `"id"` as well (usually `1`).

#### **Step C: Link the Task to the Project**
* Find the **POST `/projects/{project_id}/task/{task_id}`** endpoint.
* Enter `1` for the project ID and `1` for the task ID.
* Click **Execute**. The database now creates a relationship between these two items.

#### **Step D: Verify the Relationship**
* Go to **GET `/projects/{project_id}/tasks`**.
* Enter `1` and click **Execute**. 
* You will see your "Build Rocket" task appearing inside the project's task list!

---

## 🗺️ API Reference Cheat Sheet

| Feature | Endpoint | Method | Purpose |
| :--- | :--- | :--- | :--- |
| **Projects** | `/projects` | `POST` / `GET` | Create or list all projects. |
| **Tasks** | `/tasks` | `POST` / `GET` | Create or list all tasks. |
| **Linking** | `/projects/{pid}/task/{tid}` | `POST` | Connect a task to a project. |
| **Filtering** | `/projects/{pid}/tasks` | `GET` | View all tasks for a specific project. |
| **Tag Search** | `/tasks/tag/{tag_name}` | `GET` | Search tasks by a specific tag (e.g., "urgent"). |

---

## 🛠️ Troubleshooting Docker
* **Port Conflict:** If you get an error saying `port 8000 is already in use`, make sure you don't have a local `uvicorn` process running outside of Docker.
* **Database Reset:** To wipe the database and start fresh, run:
  `docker-compose down -v` (The `-v` removes the stored data volume).