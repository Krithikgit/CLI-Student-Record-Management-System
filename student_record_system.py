import sqlite3
import csv

def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT,
            grade TEXT
        )
    ''')
    conn.commit()
    conn.close()

def export_to_csv():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    with open("students_export.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write headers
        writer.writerow(["ID", "Name", "Age", "Department", "Grade"])
        # Write data
        writer.writerows(rows)

    print("📁✨ Data exported successfully to students_export.csv")

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    department = input("Enter department: ")
    grade = input("Enter grade: ")

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, department, grade) VALUES (?, ?, ?, ?)",
                   (name, age, department, grade))
    conn.commit()
    conn.close()
    print("✅ Student added successfully.")

def view_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Student Records ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Dept: {row[3]}, Grade: {row[4]}")

def update_student():
    student_id = input("Enter student ID to update: ")
    name = input("New name: ")
    age = input("New age: ")
    department = input("New department: ")
    grade = input("New grade: ")

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET name = ?, age = ?, department = ?, grade = ?
        WHERE id = ?
    ''', (name, age, department, grade, student_id))
    conn.commit()
    conn.close()
    print("✅ Student updated successfully.")

def delete_student():
    student_id = input("Enter student ID to delete: ")

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted successfully.")

def menu():
    while True:
        print("\n====== Student Record System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Export to CSV")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            export_to_csv()
        elif choice == '6':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    init_db()
    menu()
