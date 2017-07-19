from student import Student
import json


def draw_main_menu():
    main_menu = "01 - Teacher Menu\n" \
                "02 - Student Menu\n" \
                "Q - Quit"
    print(main_menu)

    selection = input("Enter a choice: ")

    return selection


def draw_teacher_menu():
    teacher_menu = "01 - Add Student\n" \
                   "02 - Remove Student\n" \
                   "03 - Class Roster"
    print(teacher_menu)

    selection = input("Enter a choice: ")

    return selection


def draw_student_menu():
    student_menu = "01 - Change Password"
    print(student_menu)

    selection = input("Enter a choice: ")

    return selection


def add_student(file):
    name = input("Enter the student's name: ")
    nickname = input("Enter the student's nick name: ")
    student_id = input("Enter the student's ID: ")

    student = Student(name, nickname, student_id)

    student_json = json.dumps({student.student_id:
                              [student.name,
                               student.nickname,
                               student.password]})

    json.dump(student_json, file)

if __name__ == "__main__":
    with open('class_roster.txt', 'r+') as class_roster:

        while True:
            choice = draw_main_menu()

            if choice == "01":
                choice = draw_teacher_menu()
                if choice == "01":
                    add_student(class_roster)
                    class_roster.close()
            elif choice == "02":
                draw_student_menu()
            elif choice.upper() == "Q":
                exit(1)
            else:
                print("Invalid entry. Enter 01, 02 or Q.")
                continue

