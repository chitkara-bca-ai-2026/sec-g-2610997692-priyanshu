inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("INVENTORY CONTROL SYSTEM")

while True:
    print()
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    print()
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        print()
        print("Current Inventory")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")
            
    elif choice == "2":
        item_to_add = input("Enter item name to add: ")
        inventory.append(item_to_add)
        print(f"[SUCCESS] \"{item_to_add}\" added to inventory.")
        
    elif choice == "3":
        item_to_remove = input("Enter item name to remove: ")
        if item_to_remove in inventory:
            inventory.remove(item_to_remove)
            print(f"[SUCCESS] \"{item_to_remove}\" removed from inventory.")
        else:
            print(f"[ERROR] \"{item_to_remove}\" not found in inventory.")
            
    elif choice == "4":
        inventory.sort()
        print("[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")
            
    elif choice == "5":
        print("Thank you for using Inventory Control System. Goodbye!")
        break
        
    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 5.")
