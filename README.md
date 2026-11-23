# Smart Task Scheduler & Productivity Management System

A console-based Python application for creating, organizing, completing, and analyzing tasks.

## Features

- Create tasks with an ID, title, category, priority, and deadline.
- View all tasks and mark tasks as complete.
- Filter pending tasks.
- Transform task titles to uppercase.
- View a productivity report with completion percentage.
- Count tasks by priority.
- Group tasks by category.
- View the five most recently created tasks.
- Display the current date and time.
- Show application configuration.

## Categories

- Development
- Learning
- Testing
- Documentation
- Meeting

## Priorities

- High
- Medium
- Low

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Installation

Clone or download this project, then open a terminal in the project directory:

```powershell
cd "SmartTaskScheduler"
```

## Run the Application

```powershell
python main.py
```

On systems where `python` is not available, use:

```powershell
python3 main.py
```

## Menu Options

| Option | Description |
|---|---|
| 1 | Display the current date and time |
| 2 | Create a new task |
| 3 | View all tasks |
| 4 | Complete a task |
| 5 | Filter pending tasks |
| 6 | Transform task names to uppercase |
| 7 | View the productivity report |
| 8 | Count tasks by priority |
| 9 | Group tasks by category |
| 10 | View recent tasks |
| 11 | View application configuration |
| 12 | Exit the application |

## Example: Creating a Task

1. Select `2` from the menu.
2. Enter a unique task ID.
3. Enter a task title.
4. Enter a valid category.
5. Enter `High`, `Medium`, or `Low` as the priority.
6. Enter the number of days until the deadline.

Example:

```text
Enter Task ID: T001
Enter Task Title: Prepare project report
Enter Category: Documentation
Enter Priority (High/Medium/Low): High
Deadline after how many days? 3
```

## Project Structure

```text
SmartTaskScheduler/
|-- main.py          # Interactive menu and application entry point
|-- task_manager.py  # Task storage and task operations
|-- analytics.py     # Filtering, reporting, and configuration
|-- utilities.py     # Date, deadline, timing, and processing helpers
|-- data/            # Reserved data directory
```

## Data Storage

Tasks are kept in memory while the application is running. Data is not saved to disk and will be cleared when the program exits.

## Python Concepts Demonstrated

- Named tuples and custom collections
- `OrderedDict`, `UserDict`, `UserList`, `UserString`, and `deque`
- `filter`, `map`, `reduce`, `Counter`, `defaultdict`, and `ChainMap`
- Frozenset validation
- Date and time calculations
- Decorators and execution timing
