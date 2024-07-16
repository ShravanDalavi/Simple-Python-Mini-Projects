# Python Task Scheduler
This Python Task Scheduler allows users to manage tasks with due dates, mark them as completed, and view reminders for upcoming and overdue tasks.

## Description
The Task Scheduler consists of two main classes: 'Task' and 'TaskScheduler'. The 'Task' class represents individual tasks with attributes for title, due date, and completion status. The 'TaskScheduler' class manages a list of tasks and provides methods to add, remove, mark tasks as completed, show tasks, and check reminders.

## Installation
1. Clone the Repository:
```bash
              git clone https://github.com/yourusername/task-scheduler.git
              cd task-scheduler
```
2. Install Required Modules:       
Ensure you have Python installed. The script uses the standard library 'datetime' for date handling.   
```bash  
                 # No additional modules required beyond Python's standard library
```
## How to Run the Script
Once you have cloned the repository and ensured Python is installed:
```bash
                 python task_scheduler.py
```                
Follow the on-screen prompts to interact with the Task Scheduler.

## Script Overview
The 'task_scheduler.py' script provides a menu-driven interface to perform various operations:

- Add a Task: Enter a task title and due date.
- Show Tasks: Display all tasks currently managed by the scheduler.
- Check Reminders: View upcoming tasks and overdue tasks.
- Mark Task as Completed: Set a task's completion status.
- Remove a Task: Delete a task from the scheduler.
- Exit: Terminate the program.

## Example Usage
```bash
           $ python task_scheduler.py
  
           Task Scheduler Menu:
           1. Add a task
           2. Show tasks
           3. Check reminders
           4. Mark task as completed
           5. Remove a task
           6. Exit
 
           Enter your choice (1-6): 1
           Enter task title: Complete Project Report
           Enter due date (YYYY-MM-DD): 2024-07-01
           Task 'Complete Project Report' added with due date 2024-07-01.

              ...

```