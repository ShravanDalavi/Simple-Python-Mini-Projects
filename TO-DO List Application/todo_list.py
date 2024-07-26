tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Deleted task: '{deleted_task}'")
    else:
        print("Invalid index.")

def todo_list():
    while True:
        print("\nTODO List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            index = int(input("Enter index of task to delete: "))
            delete_task(index)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please try again.")

todo_list()
