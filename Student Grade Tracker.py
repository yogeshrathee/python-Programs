class StudentGradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = []

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].append(grade)
        else:
            print(f"Student '{name}' not found.")

    def view_grades(self, name):
        if name in self.students:
            grades = self.students[name]
            print(f"Grades for {name}: {', '.join(map(str, grades))}")
        else:
            print(f"Student '{name}' not found.")


grade_tracker = StudentGradeTracker()

while True:
    print("Options:")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Grades")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade_tracker.add_student(name)
        print(f"Student '{name}' added.")
    elif choice == "2":
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        grade_tracker.add_grade(name, grade)
        print(f"Grade added for '{name}'.")
    elif choice == "3":
        name = input("Enter student name: ")
        grade_tracker.view_grades(name)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
