# Task Manager CLI (Vityarthi Project)

## Overview
The **Task Manager CLI** is a Python-based command-line application designed to assist users in organizing their daily activities. It addresses the problem of task tracking by providing a simple, lightweight interface to create, view, and modify daily to-do lists without the need for complex software installation. This project allows users to interactively manage their schedule through a text-based menu.

## Features
The application includes the following functional modules:
* **Task Initialization:** Users can define the size of their task list and bulk-add tasks at startup.
* **Dynamic Task Addition:** Allows appending new tasks to the list during runtime.
* **Task Updates:** Users can modify existing tasks by specifying the current task name and the new desired value.
* **Task Visualization:** A dedicated view function to display the current list of active tasks.
* **Interactive Menu:** A continuous loop structure allowing multiple operations in a single session.

## Technologies/Tools Used
* **Programming Language:** Python 3.x
* **Interface:** Command Line Interface (CLI) / Standard I/O
* **Development Environment:** VS Code / Python IDLE
* **Version Control:** Git & GitHub

## Steps to Install & Run the Project
1.  **Prerequisites:**
    Ensure Python 3.x is installed on your system. You can verify this by running:
    ```bash
    python --version
    ```

2.  **Clone the Repository:**
    ```bash
    git clone <your-repo-link-here>
    ```

3.  **Navigate to the Directory:**
    ```bash
    cd <your-project-folder>
    ```

4.  **Run the Application:**
    Execute the script using the Python command:
    ```bash
    python app1.py
    ```

## Instructions for Testing
To verify the project functionality, follow these test steps:

1.  **Initialization Test:**
    * Run the program.
    * When prompted for the number of tasks, enter `2`.
    * Enter "Study" for task 1 and "Exercise" for task 2.
    * *Expected Result:* The system prints the list `['Study', 'Exercise']`.

2.  **Add Task Test:**
    * Select option `1` (Add Task).
    * Enter "Groceries".
    * *Expected Result:* System confirms the task is added.

3.  **Update Task Test:**
    * Select option `2` (Update Tasks).
    * Enter the task name to update: "Exercise".
    * Enter the new task name: "Gym".
    * *Expected Result:* System confirms the update.

4.  **View and Exit:**
    * Select option `3` to verify the list now reads `['Study', 'Gym', 'Groceries']`.
    * Select option `4` to exit the application.
    
Screenshots 
<img width="534" height="307" alt="image" src="https://github.com/user-attachments/assets/f2dd96b3-5a13-4823-9c90-f19da83dd4d4" />
