import datetime

class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.completed = False
    
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - Due: {self.due_date} - Status: {status}"

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date):
        task = Task(title, due_date)
        self.tasks.append(task)
        print(f"Task '{title}' added with due date {due_date}.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks added.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)

    def check_reminders(self):
        today = datetime.date.today()
        upcoming_tasks = [task for task in self.tasks if not task.completed and task.due_date >= today]
        overdue_tasks = [task for task in self.tasks if not task.completed and task.due_date < today]

        if upcoming_tasks:
            print("\nUpcoming Tasks:")
            for task in upcoming_tasks:
                print(task)

        if overdue_tasks:
            print("\nOverdue Tasks:")
            for task in overdue_tasks:
                print(task)

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Task '{title}' not found.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' removed.")
                return
        print(f"Task '{title}' not found.")

# Helper function to get a valid date from the user
def get_due_date():
    while True:
        try:
            date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return due_date
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Main program
if __name__ == "__main__":
    scheduler = TaskScheduler()

    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add a task")
        print("2. Show tasks")
        print("3. Check reminders")
        print("4. Mark task as completed")
        print("5. Remove a task")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            due_date = get_due_date()
            scheduler.add_task(title, due_date)
        elif choice == '2':
            scheduler.show_tasks()
        elif choice == '3':
            scheduler.check_reminders()
        elif choice == '4':
            title = input("Enter the title of the task to mark as completed: ")
            scheduler.mark_completed(title)
        elif choice == '5':
            title = input("Enter the title of the task to remove: ")
            scheduler.remove_task(title)
        elif choice == '6':
            print("Exiting Task Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
