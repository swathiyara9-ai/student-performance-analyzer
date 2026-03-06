import matplotlib.pyplot as plt
import csv

students = {}

# Load previous data


def load_data():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                students[row[0]] = float(row[1])
    except:
        pass


# Save data
def save_data():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Marks"])

        for name, marks in students.items():
            writer.writerow([name, marks])

    print("Data saved successfully!")


# Add student
def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!")


# Grade calculation
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# View students
def view_students():
    if not students:
        print("No student records found.")
        return

    print("\nName\tMarks\tGrade")

    for name, marks in students.items():
        grade = calculate_grade(marks)
        print(f"{name}\t{marks}\t{grade}")


# Class average
def class_average():
    if not students:
        print("No data available.")
        return

    avg = sum(students.values()) / len(students)
    print("Class Average:", round(avg, 2))


# Find topper
def find_topper():
    if not students:
        print("No data available.")
        return

    topper = max(students, key=students.get)
    print("Topper:", topper, "-", students[topper])


# Grade statistics
def grade_statistics():
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for marks in students.values():
        grade = calculate_grade(marks)
        grades[grade] += 1

    print("\nGrade Distribution:")

    for g, count in grades.items():
        print(g, ":", count)


# Marks graph
def show_marks_graph():
    if not students:
        print("No data to display.")
        return

    names = list(students.keys())
    marks = list(students.values())

    plt.bar(names, marks)

    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.title("Student Marks Analysis")

    plt.show()

# clears the data


def clear_data():
    students.clear()
    print("All student data cleared.")

# Grade distribution graph


def grade_distribution_graph():
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for marks in students.values():
        grade = calculate_grade(marks)
        grades[grade] += 1

    plt.bar(grades.keys(), grades.values())

    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Grade Distribution")

    plt.show()


# Load existing data
load_data()


# Main menu
while True:
    print("\n--- Student Performance Analyzer ---")
    print("1 Add Student")
    print("2 View Students")
    print("3 Class Average")
    print("4 Find Topper")
    print("5 Grade Statistics")
    print("6 Show Marks Graph")
    print("7 Grade Distribution Graph")
    print("8 Save Data")
    print("9 Clear Data")
    print("10 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        class_average()

    elif choice == "4":
        find_topper()

    elif choice == "5":
        grade_statistics()

    elif choice == "6":
        show_marks_graph()

    elif choice == "7":
        grade_distribution_graph()

    elif choice == "8":
        save_data()

    elif choice == "9":
        clear_data()

    elif choice == "10":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
