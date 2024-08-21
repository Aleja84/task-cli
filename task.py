from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


class Task:
    def __init__(self, task_id, task_description, task_status=TaskStatus.TODO):
        self.id = task_id
        self.description = task_description
        self.status = TaskStatus(task_status)
        self.createdAt = datetime.now()
        self.updatedAt = None

    def __str__(self):
        return f"Task ID: {self.id}, Task Description: {self.description}, Task Status: {self.status}"

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None
        }