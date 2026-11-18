students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}


print("STUDENT INFORMATION MANAGEMENT SYSTEM")


while True:
    print()
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    print()
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        print()
        print("Enrolled Student Records")
        for roll, info in students.items():
            print(f"Roll No: {roll}  | Name: {info['Name']}  | Branch: {info['Branch']}  | Sem: {info['Semester']} | Marks: {info['Marks']}")
        print(f"Total Enrolled Students: {len(students)}")
        
    elif choice == "2":
        print()
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)
        if student:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print(f"  Name      : {student['Name']}")
            print(f"  Branch    : {student['Branch']}")
            print(f"  Semester  : {student['Semester']}")
            print(f"  Marks     : {student['Marks']}")
        else:
            print(f"\n[ERROR] No record found for Roll Number '{roll}'.")
            
    elif choice == "3":
        print()
        print("Register New Student")
        roll = input("Enter Roll Number: ")
        if roll in students:
            print(f"[ERROR] Roll Number '{roll}' already exists!")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            semester = input("Enter Semester: ")
            print("Enter marks obtained in 3 subjects:")
            m1 = float(input("  Subject 1: "))
            m2 = float(input("  Subject 2: "))
            m3 = float(input("  Subject 3: "))
            
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": [m1, m2, m3]
            }
            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")
            
    elif choice == "4":
        print()
        roll = input("Enter Roll Number to update: ")
        student = students.get(roll)
        if student:
            print(f"Current details for {student['Name']} (Roll {roll}):")
            print(f"1. Branch: {student['Branch']} | 2. Semester: {student['Semester']}")
            field_choice = input("Choose field to update (1 for Branch, 2 for Semester): ")
            if field_choice == "1":
                new_branch = input("Enter new branch: ")
                student["Branch"] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            elif field_choice == "2":
                new_sem = input("Enter new semester: ")
                student["Semester"] = new_sem
                print(f"[SUCCESS] Semester updated to '{new_sem}'.")
            else:
                print("[ERROR] Invalid selection.")
        else:
            print(f"[ERROR] Roll Number '{roll}' not found.")
            
    elif choice == "5":
        print()
        roll = input("Enter Roll Number for Academic Performance: ")
        student = students.get(roll)
        if student:
            total = sum(student["Marks"])
            average = total / len(student["Marks"])
            failed = any(m < 40 for m in student["Marks"])
            result = "FAIL" if failed or average < 40 else "PASS"
            
            print()
            print("ACADEMIC REPORT")
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {student['Marks']}")
            print(f"Total Marks  : {total} / {len(student['Marks']) * 100}")
            print(f"Average Marks: {average:.2f}%")
            print(f"Final Result : {result}")
            
        else:
            print(f"[ERROR] Roll Number '{roll}' not found.")
            
    elif choice == "6":
        print()
        roll = input("Enter Roll Number to delete: ")
        removed = students.pop(roll, None)
        if removed:
            print(f"\n[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"\n[ERROR] Roll Number '{roll}' not found.")
            
    elif choice == "7":
        print("\nThank you for using Student Information System. Goodbye!")
        break
        
    else:
        print("\n[ERROR] Invalid choice. Please enter a number between 1 and 7.")
