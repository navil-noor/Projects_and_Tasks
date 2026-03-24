from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from db import init_db, get_session
from sqlmodel import Session, select
from models import Task, Project

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)


# Logic for tasks
# creating a task
@app.post("/tasks")
async def create_task(task: Task, session: Session=Depends(get_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

# showing list of tasks
@app.get("/tasks")
async def show_tasks(session: Session=Depends(get_session)):
    statement = select(Task)
    results = session.exec(statement)
    tasks = results.all()
    return tasks

# showing task by id
@app.get("/tasks/{task_id}")
async def show_task(task_id: int, session: Session=Depends(get_session)):
    task = session.get(Task, task_id)
    return task

# delete task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, session: Session=Depends(get_session)):
    item = session.get(Task, task_id)
    if not item:
        raise HTTPException(status_code=404, detail="Task Not Found!")
    session.delete(item)
    session.commit()
    return { "ok": True }


# Logic for projects
# creating a project
@app.post("/projects")
async def create_project(project: Project, session: Session=Depends(get_session)):
    session.add(project)
    session.commit()
    session.refresh(project)
    return project

# showing list of projects
@app.get("/projects")
async def show_projects(session: Session=Depends(get_session)):
    statement = select(Project)
    results = session.exec(statement)
    projects = results.all()
    return projects

# showing project by id
@app.get("/projects/{project_id}")
async def show_project(project_id: int, session: Session=Depends(get_session)):
    project = session.get(Project, project_id)
    return project

# delete project
@app.delete("/projects/{project_id}")
async def delete_project(project_id: int, session: Session=Depends(get_session)):
    item = session.get(Project, project_id)
    if not item:
        raise HTTPException(status_code=404, detail="Project Not Found!")
    session.delete(item)
    session.commit()
    return { "ok": True }



@app.get("/")
async def home():
    return {"message": "Hello World"}