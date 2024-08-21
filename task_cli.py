import sys
from task_manager import TaskManager

import sys

def task_cli():
    try:
        manager = TaskManager()
        command = sys.argv[1].lower()

        if command == "add":
            task_name = sys.argv[2]
            task = manager.add_task(task_name)
            print(f"Task added successfully (ID: {task.id})")

        elif command == "update":
            task_id = int(sys.argv[2])
            task_name = sys.argv[3]
            task = manager.update_task(task_id, task_name)
            if task:
                print(f"Task updated successfully (ID: {task['id']})")
            else:
                print("Task not found")

        elif command == "delete":
            task_id = int(sys.argv[2])
            if manager.delete_task(task_id):
                print("Task deleted successfully")
            else:
                print("Task not found")

        elif command == "mark-in-progress":
            task_id = int(sys.argv[2])
            task = manager.mark_in_progress(task_id)
            if task:
                print(f"Task marked as in-progress (ID: {task['id']})")
            else:
                print("Task not found")

        elif command == "mark-done":
            task_id = int(sys.argv[2])
            task = manager.mark_done(task_id)
            if task:
                print(f"Task marked as done (ID: {task['id']})")
            else:
                print("Task not found")

        elif command == "list":
            if len(sys.argv) > 2:
                status = sys.argv[2].lower()
                tasks = manager.list_tasks(status)
            else:
                tasks = manager.list_tasks()
            for task in tasks:
                print(task)

        else:
            print("Unknown command. Available commands: add, update, delete, mark-in-progress, mark-done, list")

    except Exception as e:
        print("An error occurred:")



if __name__ == "__main__":
    task_cli()

