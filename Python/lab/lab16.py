def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    return base ** exp

def format_number(n):
    if n is None:
        return None
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n

history = []


print("ENTERPRISE MODULAR UTILITY CALCULATOR")


while True:
    print()
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")
    print()
    
    choice = input("Enter your choice (1-8): ")
    
    if choice in ["1", "2", "3", "4", "5"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("[ERROR] Please enter valid numbers.")
            continue
            
        if choice == "1":
            res = format_number(add(a, b))
            a_fmt, b_fmt = format_number(a), format_number(b)
            record = f"{a_fmt} + {b_fmt} = {res}"
            print(f"[RESULT] {record}")
            history.append(record)
        elif choice == "2":
            res = format_number(subtract(a, b))
            a_fmt, b_fmt = format_number(a), format_number(b)
            record = f"{a_fmt} - {b_fmt} = {res}"
            print(f"[RESULT] {record}")
            history.append(record)
        elif choice == "3":
            res = format_number(multiply(a, b))
            a_fmt, b_fmt = format_number(a), format_number(b)
            record = f"{a_fmt} * {b_fmt} = {res}"
            print(f"[RESULT] {record}")
            history.append(record)
        elif choice == "4":
            res = divide(a, b)
            if res is None:
                print("[ERROR] Division by zero is not allowed.")
            else:
                res_fmt = format_number(res)
                a_fmt, b_fmt = format_number(a), format_number(b)
                record = f"{a_fmt} / {b_fmt} = {res_fmt}"
                print(f"[RESULT] {record}")
                history.append(record)
        elif choice == "5":
            res = modulus(a, b)
            if res is None:
                print("[ERROR] Modulus by zero is not allowed.")
            else:
                res_fmt = format_number(res)
                a_fmt, b_fmt = format_number(a), format_number(b)
                record = f"{a_fmt} % {b_fmt} = {res_fmt}"
                print(f"[RESULT] {record}")
                history.append(record)
                
    elif choice == "6":
        try:
            base_input = input("Enter base number: ")
            base = float(base_input)
            exp_input = input("Enter exponent (press Enter for default 2): ")
            if exp_input.strip() == "":
                res = format_number(power(base))
                base_fmt = format_number(base)
                record = f"{base_fmt} ** 2 = {res}"
            else:
                exp = float(exp_input)
                res = format_number(power(base, exp))
                base_fmt, exp_fmt = format_number(base), format_number(exp)
                record = f"{base_fmt} ** {exp_fmt} = {res}"
            print(f"[RESULT] {record}")
            history.append(record)
        except ValueError:
            print("[ERROR] Please enter valid numbers.")
            
    elif choice == "7":
        print()
        print("Calculation History")
        if not history:
            print("No calculations performed yet.")
        else:
            for idx, item in enumerate(history, start=1):
                print(f"{idx}. {item}")
        print("-" * 27)
        
    elif choice == "8":
        print("Thank you for using Enterprise Modular Utility Calculator. Goodbye!")
        break
        
    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 8.")
