# Student Management System

A simple command-line based Student Management System built using Python. This system allows users to add, view, update, and delete student records. It serves as a basic example of how to manage data using Python's built-in data structures.

## Features

- **Add Student**: Add new student information (ID, Name, Age, Grade).
- **View Students**: Display the list of all students.
- **Update Student**: Update existing student details.
- **Delete Student**: Remove a student's record from the system.
- **Exit**: Exit the program.

## Prerequisites

- Python 3.x

## Getting Started

1. Clone the repository:
```bash
   git clone https://github.com/your-username/student-management-system.git
```

2. Navigate to the project directory:
```bash
cd student-management-system
```
3. Run the program:
```bash
python student_management_system.py
```

## Usage
Once you run the program, you will see a menu with the following options:

1. Add Student: Enter student details such as ID, Name, Age, and Grade.
2. View Students: List all students in the system.
3. Update Student: Modify details of an existing student.
4. Delete Student: Remove a student's data from the system.
5. Exit: Close the application.
 Follow the on-screen instructions to perform any of the actions.

## Code Structure
- `student_management_system.py`: The main script containing the program logic for the Student Management System.

## Sample Output
```mathematica

--- Student Management System ---
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 1
Enter student ID: 101
Enter student name: Alice
Enter student age: 20
Enter student grade: A
Student added successfully!
```

## Future Enhancements
- Data Persistence: Store student data in a database (SQLite, MySQL) or a file (CSV, JSON).
- GUI: Implement a graphical user interface using libraries like Tkinter or PyQt.
- Advanced Search: Add features to search for students by different criteria (name, grade, etc.).
- Error Handling: Add more comprehensive error checking and validation.