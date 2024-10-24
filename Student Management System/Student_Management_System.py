class StudentManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store student data

    def add_student(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            print("Student ID already exists!")
            return
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        self.students[student_id] = {'Name': name, 'Age': age, 'Grade': grade}
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        print("\nStudent List:")
        for student_id, details in self.students.items():
            print(f"ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grade: {details['Grade']}")
        print()

    def update_student(self):
        student_id = input("Enter student ID to update: ")
        if student_id not in self.students:
            print("Student ID not found!")
            return
        print("Enter new details (leave blank to keep current value):")
        name = input(f"Enter new name (current: {self.students[student_id]['Name']}): ") or self.students[student_id]['Name']
        age = input(f"Enter new age (current: {self.students[student_id]['Age']}): ") or self.students[student_id]['Age']
        grade = input(f"Enter new grade (current: {self.students[student_id]['Grade']}): ") or self.students[student_id]['Grade']
        self.students[student_id] = {'Name': name, 'Age': age, 'Grade': grade}
        print("Student information updated successfully!")

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        if student_id not in self.students:
            print("Student ID not found!")
            return
        del self.students[student_id]
        print("Student record deleted successfully!")

    def menu(self):
        while True:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.menu()
