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
- <a href="https://www.docker.com/products/docker-desktop/">Docker Desktop</a> installed and running. installed and running.

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