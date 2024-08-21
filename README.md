# Task Tracker CLI

Task Tracker is a command-line application for managing tasks. You can add, update, delete, mark as in-progress or done, and list tasks stored in a JSON file. This is a Python sample solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/).

## Features

- **Add tasks**: Add new tasks to your list.
- **Update tasks**: Modify the name of an existing task.
- **Delete tasks**: Remove tasks from the list.
- **Mark tasks as in-progress**: Change the status of a task to "in-progress".
- **Mark tasks as done**: Change the status of a task to "done".
- **List tasks**: Display all tasks or filter by status.

## Requirements

- Python 3.7 or higher
- Python Standard Library (no additional libraries required)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aleja84/task-tracker-cli.git

2. Navigate to the project directory:

   ```bash
   cd task-tracker-cli

## Usage

### Available Commands

- **add**: Add a new task.

  ```bash
  python3 task_cli.py add "Task name"

- **update**: Update an existing task.

  ```bash
  python3 task_cli.py update <task_id> "New task name"

- **delete**: Delete a task.

  ```bash
  python3 task_cli.py delete <task_id>

- **mark-in-progress**: Mark a task as in-progress.
  ```bash
  python3 task_cli.py mark-in-progress <task_id>

- **mark-done**: Mark a task as done.
  ```bash
  python3 task_cli.py mark-done <task_id>

- **list**: List all tasks or filter by status.
  ```bash
  python3 task_cli.py list [status]
