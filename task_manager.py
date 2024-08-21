import json
import os
from datetime import datetime

from task import Task, TaskStatus


import os
import json
from datetime import datetime

class TaskManager:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, task_description)
        self.tasks.append(task.to_dict())

        self.save_tasks()
        return task

    def update_task(self, task_id, task_description):
        for task in self.tasks:
            if task["id"] == task_id:
                task["description"] = task_description
                task["updatedAt"] = datetime.now().isoformat()
                self.save_tasks()
                return task
        return None

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                del self.tasks[i]
                self.save_tasks()
                return True
        return False

    def mark_in_progress(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = TaskStatus.IN_PROGRESS.value
                task["updatedAt"] = datetime.now().isoformat()
                self.save_tasks()
                return task
        return None

    def mark_done(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = TaskStatus.DONE.value
                task["updatedAt"] = datetime.now().isoformat()  # Convertimos datetime a string
                self.save_tasks()
                return task
        return None

    def list_tasks(self, status=None):
        if status:
            return [task for task in self.tasks if task["status"] == status]
        return self.tasks


