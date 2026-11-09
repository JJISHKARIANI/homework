from stud_managment import StudentManagemnt
from student import Student

def main():
    manager = StudentManagemnt()
    while True:
        print("Students (system)")
        print("1. add student ")
        print("2. search student with id ")
        print("3. update student information ")
        print("4. delete a student ")
        print("5. list of the all student ")
        print("6. exit ")

        choice = input("choose a option (1-6): ").strip()

        try:
            if choice == '1':
                name = input("enter a name: ")
                roll_number = int(input("enter a id number (int): "))
                grade = float(input("enter a grade (float): "))
                manager.add_student(name, roll_number, grade)

            elif choice == '2':
                roll_number = int(input("enter id of student: "))
                student = manager.search_student(roll_number)
                print(f"found {student}")

            elif choice == '3':
                roll_number = int(input("update: enter a student (id): "))
                new_name = input("new name (leave a space if u not changing it): ").strip()
                new_grade_str = input("new grade (leave space if u not changing it): ").strip()

                name_arg = new_name if new_name else None
                grade_arg = float(new_grade_str) if new_grade_str else None

                manager.update_student(roll_number, new_name=name_arg, new_grade=grade_arg)

            elif choice == '4':
                roll_number = int(input("delete - enter a student(id) : "))
                manager.delete_student(roll_number)

            elif choice == '5':
                manager.display_all_student()

            elif choice == '6':
                print("programm done. goodbye")
                break
            else:
                print("incorrect.number must be (1 - 6)")

        except ValueError as e:
            print(f"[error]")
        except KeyError as e:
            print(f"[searching error]")
        except Exception as e:
            print(f"[unexcpected error]")

if __name__ == "_main_":
    main()

res = main()
print(res)