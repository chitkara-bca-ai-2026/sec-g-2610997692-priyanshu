def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    total, average = calculate_results(student["Marks"])
    print(f"Roll No: {roll}  | Name: {student['Name']}  | Marks: {student['Marks']} | Total: {total} | Average: {average:.2f}%")

def add_student(records, roll, name, marks):
    if roll in records:
        print(f"[ERROR] Roll Number '{roll}' already exists!")
    else:
        records[roll] = {
            "Name": name,
            "Marks": marks
        }
        print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")

students = {
    "101": {
        "Name": "Aman",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Marks": [74, 80, 82]
    }
}


print("STUDENT RECORDS MANAGEMENT SYSTEM")


while True:
    print()
    print("Select an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")
    print()
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        print()
        print("All Student Records")
        for roll, student in students.items():
            display_student(roll, student)
        print(f"Total Students: {len(students)}")
        
    elif choice == "2":
        print()
        print("Add New Student")
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        print("Enter marks for 3 subjects:")
        try:
            m1 = float(input("  Subject 1: "))
            m2 = float(input("  Subject 2: "))
            m3 = float(input("  Subject 3: "))
            add_student(students, roll, name, [m1, m2, m3])
        except ValueError:
            print("[ERROR] Please enter valid numeric marks.")
            
    elif choice == "3":
        print()
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)
        if student:
            print("\n[RECORD FOUND]")
            display_student(roll, student)
        else:
            print(f"\n[ERROR] No student found with Roll Number '{roll}'.")
            
    elif choice == "4":
        print("\nThank you for using the Student Records System. Goodbye!")
        break
        
    else:
        print("\n[ERROR] Invalid choice. Please enter a number between 1 and 4.")
