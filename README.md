
# Task Manager CLI Application

A simple command-line interface (CLI) application to manage tasks. This application allows users to add, view, delete, and mark tasks as complete, with the ability to save and load tasks to/from a file for persistent storage.

## Features

- **Add Task**: Add a new task to the task list with a unique ID.
- **View Tasks**: View all tasks with their ID and status (completed or not).
- **Delete Task**: Delete a specific task by its ID.
- **Mark Task as Complete**: Update the status of a task to indicate it is completed.
- **Save and Load Tasks**: Automatically saves tasks to a JSON file (`tasks.json`) on exit and loads existing tasks on startup.

## Project Structure





## Setup

1. Clone or download the repository.
2. Ensure you have Python 3.6+ installed. You can download it from [Python's official website](https://www.python.org/downloads/).
3. Open a terminal or command prompt.
4. Navigate to the project directory, e.g., `task_manager/`.

## Installation

There are no external dependencies for this project. It uses Python's built-in libraries: `json` and `os`.

## Usage

1. Open a terminal or command prompt and navigate to the directory where you have saved the project.
2. Run the following command to start the Task Manager CLI:

```bash
python task_manager.py




Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 1

Enter task title: Finish documentation
Task 'Finish documentation' added with ID 1.

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 2

[✗] ID: 1 - Finish documentation


Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 1
Enter task title: paln the project road map
Task 'paln the project road map' added with ID 6.

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 1
Enter task title: write documentaion
Task 'write documentaion' added with ID 7.

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 2
[✓] ID: 1 - Buy groceries
[✓] ID: 2 - Complete homework
[✗] ID: 3 - Go for a run
[✗] ID: 4 -  Finish the CLI project
[✗] ID: 5 - Review the code
[✗] ID: 6 - paln the project road map
[✗] ID: 7 - write documentaion

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 3
Enter task ID to delete: 1
Task ID 1 deleted.

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 2
[✓] ID: 2 - Complete homework
[✗] ID: 3 - Go for a run
[✗] ID: 4 -  Finish the CLI project
[✗] ID: 5 - Review the code
[✗] ID: 6 - paln the project road map
[✗] ID: 7 - write documentaion

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 4
Enter task ID to mark as complete: 2
Task ID 2 marked as complete.

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 4
Enter task ID to mark as complete: 3
Task ID 3 marked as complete.

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 2
[✓] ID: 2 - Complete homework
[✓] ID: 3 - Go for a run
[✗] ID: 4 -  Finish the CLI project
[✗] ID: 5 - Review the code
[✗] ID: 6 - paln the project road map
[✗] ID: 7 - write documentaion

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 5
Tasks saved to file.

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 4
Enter task ID to mark as complete: 6
Task ID 6 marked as complete.

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 5
Tasks saved to file.

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 2
[✓] ID: 2 - Complete homework
[✓] ID: 3 - Go for a run
[✗] ID: 4 -  Finish the CLI project
[✗] ID: 5 - Review the code
[✓] ID: 6 - paln the project road map
[✗] ID: 7 - write documentaion

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option: 6 
Tasks saved to file.
Exiting Task Manager. Goodbye!



---
##                    OverView of this project
### Explanation:

- **Project Overview**: Provides a brief description of what the Task Manager CLI is and its main features.
- **Project Structure**: Outlines the directory structure so that users know where to find files and how they are organized.
- **Setup Instructions**: Guides users through the steps to set up the project, including installing Python if necessary.
- **Usage**: Provides clear instructions on how to run the application, interact with the CLI, and examples of how it works.
- **File Handling**: Explains how the program saves and loads task data using the `tasks.json` file.
- **Future Enhancements**: Lists ideas for future improvements that could be added to the project.
- **License**: States the licensing information (MIT License in this case).
- **Acknowledgments**: Credits the resources or individuals who inspired or helped with the project.

This README file should serve as a complete reference for anyone who wishes to use, contribute to, or understand the project.

