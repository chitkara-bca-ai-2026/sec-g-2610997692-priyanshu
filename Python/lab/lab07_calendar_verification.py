
print("CALENDAR VERIFICATION SYSTEM")
year = int(input("Enter year: "))
if year <= 0:
    print("Error: Please enter a positive integer greater than 0.")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            status = "LEAP YEAR"
            days_year = 366
            days_feb = 29
            reason = "Century year divisible by 400"
        else:
            status = "COMMON YEAR"
            days_year = 365
            days_feb = 28
            reason = "Century year not divisible by 400"
    elif year % 4 == 0:
        status = "LEAP YEAR"
        days_year = 366
        days_feb = 29
        reason = "Divisible by 4 and not a century year"
    else:
        status = "COMMON YEAR"
        days_year = 365
        days_feb = 28
        reason = "Not divisible by 4"
    print()
    print(f"Year: {year}")
    print(f"Status: {status}")
    print(f"Days in Year: {days_year} days")
    print(f"Days in February: {days_feb} days")
    print(f"Reason: {reason}")

