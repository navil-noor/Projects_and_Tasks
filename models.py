from sqlmodel import SQLModel, Field, Relationship

class ProjectTaskLink(SQLModel, table=True):
    project_id: int | None = Field(default=None, foreign_key="project.id", primary_key=True)
    task_id: int | None = Field(default=None, foreign_key="task.id", primary_key=True)

class Project(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    budget: int
    description: str
    hours_used: int

    tasks: list["Task"] = Relationship(back_populates="projects", link_model=ProjectTaskLink)

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    tags: str

    projects: list["Project"] = Relationship(back_populates="tasks", link_model=ProjectTaskLink)