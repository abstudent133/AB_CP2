# Simple Grade Book System
***

This project is a simple grade book system built in Python. It allows users to create and manage students, add grades, view student records, and calculate averages and letter grades. The program uses classes to represent students and the overall grade book, and it stores student data in a CSV file so that information is saved between runs. Users interact with the program through a text-based menu system.

## How to use
***
1. Open the project in your code editor (such as VS Code).
2. Make sure all project files are in the correct folder structure.
3. Run the main file:

4. Use the menu to:
- Add new students
- Add grades to students
- View all students
- Find a specific student
- View class summary
5. Follow the prompts in the terminal to input values and navigate the program.

**Libraries required:**
- `csv` (built-in, no download needed)

## Details on project features
***

- **Student Management**
- Create new students with a name and ID
- Each student stores their own list of grades
- Uses a custom `Student` class to manage individual data

- **Grade Management**
- Add grades to individual students
- Input validation ensures only positive numbers are accepted
- Automatically calculates average grade
- Converts numerical averages into letter grades (A–F)

- **View Students**
- Displays all students in a formatted list
- Shows ID, name, average grade, and letter grade

- **Find Student**
- Search for a student by their ID
- Displays detailed information including all grades

- **Class Summary**
- Calculates overall class average
- Displays highest and lowest grades in the class
- Shows a summary of all students

- **File Storage System**
- Student data is saved to a `.csv` file
- Data persists between program runs
- Includes helper functions to convert and store grade lists

- **Object-Oriented Design**
- `Student` class handles individual student data and calculations
- `GradeBook` class manages a collection of students
- Clear separation of responsibilities between classes