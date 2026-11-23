
"""
Analytics Module

Demonstrates:
1. Filter
2. Map
3. Reduce
4. Frozen Set
5. ChainMap
6. Counter
7. DefaultDict
"""

from collections import (
    Counter,
    ChainMap,
    defaultdict
)

from functools import reduce

from task_manager import get_all_tasks


# ---------------------------------
# FROZENSET
# ---------------------------------

TASK_CATEGORIES = frozenset([
    "Development",
    "Learning",
    "Testing",
    "Documentation",
    "Meeting"
])


# ---------------------------------
# CHAINMAP
# ---------------------------------

default_config = {
    "theme": "Light",
    "notification": True,
    "language": "English"
}

user_config = {
    "theme": "Dark",
    "language": "English"
}

config = ChainMap(user_config, default_config)


def show_configuration():

    print("\n===== APPLICATION CONFIGURATION =====")

    print("Theme:", config["theme"])

    print("Notification:", config["notification"])

    print("Language:", config["language"])


# ---------------------------------
# FILTER
# ---------------------------------

def filter_pending_tasks():

    tasks = get_all_tasks()

    pending = list(
        filter(
            lambda task: task.status == "Pending",
            tasks
        )
    )

    print("\n===== PENDING TASKS =====")

    for task in pending:

        print(task.title)


# ---------------------------------
# MAP
# ---------------------------------

def transform_task_names():

    tasks = get_all_tasks()

    names = list(
        map(
            lambda task: task.title.upper(),
            tasks
        )
    )

    print("\n===== TASK NAMES =====")

    for name in names:

        print(name)


# ---------------------------------
# REDUCE
# ---------------------------------

def calculate_productivity():

    tasks = get_all_tasks()

    completed_count = reduce(
        lambda total, task:
            total + (1 if task.status == "Completed" else 0),
        tasks,
        0
    )

    print("\n===== PRODUCTIVITY REPORT =====")

    print("Total Tasks:", len(tasks))

    print("Completed Tasks:", completed_count)

    if tasks:

        score = (
            completed_count / len(tasks)
        ) * 100

        print(f"Productivity Score: {score:.2f}%")

    else:

        print("Productivity Score: 0%")


# ---------------------------------
# COUNTER
# ---------------------------------

def count_task_priorities():

    tasks = get_all_tasks()

    priority_count = Counter(
        task.priority for task in tasks
    )

    print("\n===== PRIORITY SUMMARY =====")

    print(priority_count)


# ---------------------------------
# DEFAULTDICT
# ---------------------------------

def group_tasks_by_category():

    tasks = get_all_tasks()

    grouped_tasks = defaultdict(list)

    for task in tasks:

        grouped_tasks[task.category].append(
            task.title
        )

    print("\n===== CATEGORY-WISE TASKS =====")

    for category, titles in grouped_tasks.items():

        print(category, ":", titles)


# ---------------------------------
# FROZENSET VALIDATION
# ---------------------------------

def validate_category(category):

    if category in TASK_CATEGORIES:

        print("Valid task category!")

    else:

        print("Invalid task category!")
