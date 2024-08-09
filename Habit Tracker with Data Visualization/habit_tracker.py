import json
import datetime
import matplotlib.pyplot as plt

class Habit:
    def __init__(self, name):
        self.name = name
        self.history = {}

    def mark_completed(self, date=None):
        date = date or datetime.datetime.now().strftime('%Y-%m-%d')
        self.history[date] = True

    def __repr__(self):
        return f"{self.name}: {len(self.history)} completions"

class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, name):
        if name not in self.habits:
            self.habits[name] = Habit(name)
        else:
            print("Habit already exists.")

    def delete_habit(self, name):
        if name in self.habits:
            del self.habits[name]
        else:
            print("Habit does not exist.")

    def mark_completed(self, name, date=None):
        if name in self.habits:
            self.habits[name].mark_completed(date)
        else:
            print("Habit does not exist.")

    def view_habits(self):
        for habit in self.habits.values():
            print(habit)

    def save_to_file(self, filename='habits.json'):
        data = {name: habit.history for name, habit in self.habits.items()}
        with open(filename, 'w') as f:
            json.dump(data, f)
        print("Habits saved to file.")

    def load_from_file(self, filename='habits.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.habits = {name: Habit(name) for name in data}
                for name, history in data.items():
                    self.habits[name].history = history
            print("Habits loaded from file.")
        except FileNotFoundError:
            print("File not found. Starting with an empty habit tracker.")

    def visualize_habit(self, name):
        if name in self.habits:
            dates = list(self.habits[name].history.keys())
            dates.sort()
            completions = [1 if date in dates else 0 for date in dates]

            plt.figure(figsize=(10, 5))
            plt.plot(dates, completions, marker='o')
            plt.title(f'Habit Completion: {name}')
            plt.xlabel('Date')
            plt.ylabel('Completion')
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("Habit does not exist.")

def main():
    tracker = HabitTracker()
    tracker.load_from_file()
    
    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. Delete Habit")
        print("3. Mark Habit as Completed")
        print("4. View All Habits")
        print("5. Save Habits to File")
        print("6. Load Habits from File")
        print("7. Visualize Habit")
        print("8. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter habit name: ")
            tracker.add_habit(name)
        elif choice == '2':
            name = input("Enter habit name to delete: ")
            tracker.delete_habit(name)
        elif choice == '3':
            name = input("Enter habit name: ")
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            tracker.mark_completed(name, date if date else None)
        elif choice == '4':
            tracker.view_habits()
        elif choice == '5':
            tracker.save_to_file()
        elif choice == '6':
            tracker.load_from_file()
        elif choice == '7':
            name = input("Enter habit name to visualize: ")
            tracker.visualize_habit(name)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
