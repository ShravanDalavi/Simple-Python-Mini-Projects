# TO DO List Application
This Python TODO List Application allows users to manage tasks by adding, viewing, and deleting them through a simple command-line interface.

## 🗒️ Description
The application provides basic functionality to manipulate tasks:

- Add Task: Allows users to input a task which gets added to the task list.
- View Tasks: Displays all tasks currently stored in the list.
- Delete Task: Removes a task based on its index in the list.
- Exit: Terminates the application.

## Installation
1. Clone the Repository:
```bash
               git clone https://github.com/yourusername/todo-list.git
               cd todo-list
```
2. No Additional Modules Required:
This application only uses Python's standard library, so no additional modules need to be installed.

## ▶️ How to Run the Script
After cloning the repository and navigating to the project directory:
```bash
                python todo_list.py
```                                
Follow the on-screen prompts to interact with the TODO List Application.

## Script Overview
The 'todo_list.py' script implements a menu-driven interface where users can perform various operations on tasks:

- Add Task: Input a task to add it to the list.
- View Tasks: Display all tasks currently stored.
- Delete Task: Remove a task by specifying its index.
- Exit: Quit the application

## Example Usage
```bash

                $ python todo_list.py

                TODO List Application
                1. Add Task
                2. View Tasks
                3. Delete Task
                4. Exit

                Enter your choice: 1
                Enter task: Complete assignment
                Task 'Complete assignment' added.

                2. View Tasks
                3. Delete Task
                4. Exit

                Enter your choice: 2
                Tasks:
                1. Complete assignment

                3. Delete Task
                4. Exit

                Enter your choice: 3
                Enter index of task to delete: 1
                Deleted task: 'Complete assignment'

                2. View Tasks
                3. Delete Task
                4. Exit

                Enter your choice: 4
                Exiting program.
```
