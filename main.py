
"""
Smart Task Scheduler
Main Application
"""

from task_manager import (
    create_task,
    display_tasks,
    complete_task,
    recent_tasks
)

from analytics import (
    filter_pending_tasks,
    transform_task_names,
    calculate_productivity,
    count_task_priorities,
    group_tasks_by_category,
    validate_category,
    show_configuration
)

from utilities import (
    execution_timer,
    get_current_datetime,
    calculate_deadline,
    simulate_processing
)


# ---------------------------------
# DISPLAY MENU
# ---------------------------------

def display_menu():

    print("\n" + "=" * 45)

    print("       SMART TASK SCHEDULER")

    print("=" * 45)

    print("1. Display Current Date and Time")
    print("2. Create New Task")
    print("3. View All Tasks")
    print("4. Complete a Task")
    print("5. Filter Pending Tasks")
    print("6. Transform Task Names")
    print("7. Productivity Report")
    print("8. Count Task Priorities")
    print("9. Group Tasks by Category")
    print("10. View Recent Tasks")
    print("11. View Configuration")
    print("12. Exit")


# ---------------------------------
# TASK CREATION
# ---------------------------------

@execution_timer
def add_new_task():

    task_id = input("Enter Task ID: ").strip()

    title = input("Enter Task Title: ").strip()

    category = input("Enter Category: ").strip().title()

    validate_category(category)

    if category not in (
        "Development",
        "Learning",
        "Testing",
        "Documentation",
        "Meeting"
    ):
        return

    priority = input(
        "Enter Priority (High/Medium/Low): "
    ).strip().title()

    if priority not in ("High", "Medium", "Low"):

        print("Invalid priority!")

        return

    days = int(
        input("Deadline after how many days? ")
    )

    if days < 0:

        print("Deadline cannot be negative!")

        return

    deadline = calculate_deadline(days)

    create_task(
        task_id,
        title,
        category,
        priority,
        deadline
    )

    simulate_processing()


# ---------------------------------
# MAIN APPLICATION
# ---------------------------------

while True:

    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":

        get_current_datetime()

    elif choice == "2":

        try:

            add_new_task()

        except ValueError:

            print("Please enter a valid number.")

    elif choice == "3":

        display_tasks()

    elif choice == "4":

        task_id = input("Enter Task ID: ").strip()

        complete_task(task_id)

    elif choice == "5":

        filter_pending_tasks()

    elif choice == "6":

        transform_task_names()

    elif choice == "7":

        calculate_productivity()

    elif choice == "8":

        count_task_priorities()

    elif choice == "9":

        group_tasks_by_category()

    elif choice == "10":

        print("\n===== RECENT TASKS =====")

        for task in recent_tasks:

            print(task)

    elif choice == "11":

        show_configuration()

    elif choice == "12":

        print("Thank you for using Smart Task Scheduler!")

        break

    else:

        print("Invalid choice. Please try again.")
