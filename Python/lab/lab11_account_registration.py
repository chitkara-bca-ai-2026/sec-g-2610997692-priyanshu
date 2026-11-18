username = input("Enter your username: ")
password = input("Enter your password: ")

length_pass = len(password) >= 8
digit_pass = any(char.isdigit() for char in password)
upper_pass = any(char.isupper() for char in password)

is_valid = length_pass and digit_pass and upper_pass

print("PASSWORD VALIDATION REPORT")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")
print()
print("Validation Rules")

if length_pass:
    print(f"[PASS] Minimum 8 characters ({len(password)} characters)")
else:
    print(f"[FAIL] Minimum 8 characters ({len(password)} characters)")

if digit_pass:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if upper_pass:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print()
print("Result")
if is_valid:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")
    print("Please meet all the security requirements.")

