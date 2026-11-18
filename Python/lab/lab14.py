books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = {book[3] for book in books}
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("LIBRARY BOOK & CATEGORY MANAGER")
while True:
    print()
    print("Select an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
    print()
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        print()
        print("Current Library Catalog (Fixed Records)")
        for index, book in enumerate(books, start=1):
            title, author, year, category = book
            print(f"{index}. \"{title}\" by {author} ({year}) | Genre: {category}")
        print(f"Total Books: {len(books)}")
        
    elif choice == "2":
        print()
        print("Add New Book Record")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")
        
        new_book = (title, author, year, category)
        books.append(new_book)
        library_categories.add(category)
        
        print()
        print(f"[SUCCESS] \"{title}\" added as an immutable catalog record.")
        print(f"[INFO] Category set updated with: \"{category}\"")
        
    elif choice == "3":
        print()
        print("Unique Categories Available in Library (Set)")
        sorted_categories = sorted(list(library_categories))
        for cat in sorted_categories:
            print(f" - {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")
        
    elif choice == "4":
        print()
        print("Add to Student Wishlist")
        req_category = input("Enter requested category: ")
        student_wishlist.add(req_category)
        print(f"[SUCCESS] \"{req_category}\" added to student wishlist.")
        
    elif choice == "5":
        print()
        print("CATEGORY GAP ANALYSIS")
        print(f"Library Holdings(Set): {sorted(list(library_categories))}")
        print(f"Student Wishlist(Set): {sorted(list(student_wishlist))}")
       
        
        intersection_res = sorted(list(library_categories & student_wishlist))
        difference_res = sorted(list(student_wishlist - library_categories))
        union_res = sorted(list(library_categories | student_wishlist))
        
        print(f"1. Already in Stock (Intersection &): {intersection_res}")
        print()
        print(f"2. Purchase Order Needed (Difference -): {difference_res}")
        print()
        print(f"3. Full Combined Genre Coverage (Union |): {union_res}")
        
    elif choice == "6":
        print("Thank you for using the Library Manager. Goodbye!")
        break
        
    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 6.")
