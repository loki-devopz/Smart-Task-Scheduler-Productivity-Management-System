
"""
Utilities Module

Concepts:
1. Date and Time
2. Sleep
3. Program Execution Time
4. Decorators
"""

import time
from datetime import datetime, date, timedelta


# ---------------------------------
# DECORATOR: Execution Time
# ---------------------------------

def execution_timer(function):
    """Measure the execution time of a function."""

    def wrapper(*args, **kwargs):

        start_time = time.perf_counter()

        result = function(*args, **kwargs)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(
            f"\nExecution Time: "
            f"{execution_time:.6f} seconds"
        )

        return result

    return wrapper


# ---------------------------------
# CURRENT DATE AND TIME
# ---------------------------------

def get_current_datetime():
    """Return current date and time."""

    current = datetime.now()

    print("\n===== CURRENT DATE AND TIME =====")

    print("Date:", current.strftime("%d-%m-%Y"))

    print("Time:", current.strftime("%I:%M:%S %p"))

    print("Day:", current.strftime("%A"))

    print("Month:", current.strftime("%B"))

    return current


# ---------------------------------
# DEADLINE CALCULATION
# ---------------------------------

def calculate_deadline(days):
    """Calculate a future task deadline."""

    deadline = datetime.now() + timedelta(days=days)

    return deadline.strftime("%d-%m-%Y")


# ---------------------------------
# SLEEP
# ---------------------------------

def simulate_processing():
    """Simulate a task processing delay."""

    print("\nProcessing your task...")

    time.sleep(2)

    print("Task processing completed!")


# ---------------------------------
# DATE COMPARISON
# ---------------------------------

def check_deadline(deadline):

    today = date.today()

    task_date = datetime.strptime(
        deadline, "%d-%m-%Y"
    ).date()

    if task_date < today:

        return "Overdue"

    elif task_date == today:

        return "Due Today"

    else:

        return "Upcoming"
