from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    completed: bool = False

tasks = []
next_task = 1

@app.post("/tasks")
def create_task(task: Task):

    global next_task

    new_task = {
        "id": next_task,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)

    next_task += 1

    return new_task


@app.get("/tasks")
def get_tasks():
    return tasks

# NOTE:
# Static routes like /tasks/completed must always be defined before parameterized routes like /tasks/{task_id}.
# If the @app.get("/tasks/completed") route is placed after @app.get("/tasks/{task_id}") in your code, 
# FastAPI will match "completed" as the {task_id} path parameter. 
# It will attempt to parse "completed" as an integer, fail, and return a 422 Unprocessable Entity error.
@app.get("/tasks/completed")
def get_completed_tasks():
    completed_list = []
    for task in tasks:
        if task["completed"] == True:
            completed_list.append(task)

    return completed_list


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
        
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["completed"] = updated_task.completed

            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
        

@app.delete("/tasks/{task_id}")
def del_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_task = tasks.pop(index)
            return deleted_task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
