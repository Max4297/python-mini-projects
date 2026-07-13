grades = []

while True:
    print("""===== Student Grade Manager =====

1. Add grade
2. Show grades
3. Show average grade
4. Show highest grade
5. Show lowest grade
0. Exit""")

    choice = input("Choose an option: ")

    match choice: 
        case "0":
            print("Goodbye!")
            break
        case "1":
            grade = int(input("Enter grade: "))
            grades.append(grade)
            print("Grade added")
        case "2":
            if grades:
                print("Grades:\n")
                for grade in grades:
                    print(grade)
            else:
                print("No grades yet.")
        case "3":
            if not grades:
                print("First, enter the grades.")
            else:
                sum_grades = 0
                for grade in grades:
                    sum_grades += grade
                print(f"Average grade: {sum_grades/len(grades)}")
        case "4":
            if not grades:
                print("First, enter the grades.")
            else:
                maximum_grade = grades[0]
                for grade in grades:
                    if maximum_grade < grade:
                        maximum_grade = grade
                print(f"Highest grade: {maximum_grade}")
        case "5":
             if not grades:
                print("First, enter the grades.")
             else:
                minimum_grade = grades[0]
                for grade in grades:
                    if minimum_grade > grade:
                        minimum_grade = grade
                print(f"Lowest grade: {minimum_grade}")
        case _:
            print("Invalid option.")