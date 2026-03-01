students = []

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average Marks")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

     if choice == '1':
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = [roll, name, marks]
        students.append(student)

        print("Student Added Successfully!")

      elif choice == '2':
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent Records:")
            for s in students:
                print("Roll:", s[0], "Name:", s[1], "Marks:", s[2])

    elif choice == '3':
        search_roll = input("Enter Roll Number to Search: ")
        found = False

        for s in students:
            if s[0] == search_roll:
                print("Student Found!")
                print("Name:", s[1])
                print("Marks:", s[2])
                found = True
                break

        if not found:
            print("Student Not Found.")

   
    elif choice == '4':
        if len(students) == 0:
            print("No students to calculate average.")
        else:
            total = 0
            for s in students:
                total += s[2]

            average = total / len(students)
            print("Average Marks:", average)

   
    elif choice == '5':
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice. Try Again!")
