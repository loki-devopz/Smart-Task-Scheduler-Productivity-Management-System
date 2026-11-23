
"""
Task Manager Module

Demonstrates Python Collections.
"""

from collections import (
    namedtuple,
    deque,
    OrderedDict,
    UserDict,
    UserList,
    UserString
)

from datetime import datetime


# ---------------------------------
# NAMEDTUPLE
# ---------------------------------

Task = namedtuple(
    "Task",
    ["task_id", "title", "category",
     "priority", "deadline", "status"]
)


# ---------------------------------
# USERDICT
# ---------------------------------

class TaskStorage(UserDict):
    """Customized dictionary for storing tasks."""

    def add_task(self, task):

        self.data[task.task_id] = task

    def get_task(self, task_id):

        return self.data.get(task_id)


# ---------------------------------
# USERLIST
# ---------------------------------

class TaskList(UserList):
    """Customized list for managing task records."""

    def pending_tasks(self):

        return [
            task for task in self.data
            if task.status == "Pending"
        ]


# ---------------------------------
# USERSTRING
# ---------------------------------

class TaskLabel(UserString):
    """Customized string for task labels."""

    def uppercase(self):

        return self.data.upper()


# ---------------------------------
# DEQUE
# ---------------------------------

recent_tasks = deque(maxlen=5)


# ---------------------------------
# ORDEREDDICT
# ---------------------------------

task_history = OrderedDict()


# ---------------------------------
# TASK STORAGE
# ---------------------------------

task_storage = TaskStorage()

task_list = TaskList()


def create_task(task_id, title, category, priority, deadline):
    """Create and store a new task."""

    task = Task(
        task_id,
        title,
        category,
        priority,
        deadline,
        "Pending"
    )

    task_storage.add_task(task)

    task_list.append(task)

    recent_tasks.append(task.title)

    task_history[task_id] = datetime.now()

    print("\nTask created successfully!")

    return task


def get_all_tasks():
    """Return all stored tasks."""

    return list(task_storage.values())


def complete_task(task_id):
    """Mark a task as completed."""

    task = task_storage.get_task(task_id)

    if task is None:

        print("Task not found!")

        return

    updated_task = task._replace(status="Completed")

    task_storage[task_id] = updated_task

    # Update task list
    for index, existing_task in enumerate(task_list):

        if existing_task.task_id == task_id:

            task_list[index] = updated_task

            break

    print("Task completed successfully!")


def display_tasks():
    """Display all tasks."""

    print("\n========== TASK LIST ==========")

    for task in task_storage.values():

        label = TaskLabel(task.title)

        print(
            f"ID: {task.task_id} | "
            f"Title: {label.uppercase()} | "
            f"Priority: {task.priority} | "
            f"Status: {task.status} | "
            f"Deadline: {task.deadline}"
        )
