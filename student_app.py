from student import Student
import json
import os


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


def add_student():
    with open('class_roster.txt', 'r+') as class_roster:
        name = input("Enter the student's name: ")
        nickname = input("Enter the student's nick name: ")
        student_id = input("Enter the student's ID: ")

        student = Student(name, nickname, student_id)

        if os.stat('class_roster.txt').st_size == 0:
            roster = {student.student_id: {"Name": student.name,
                                           "Nickname": student.nickname,
                                           "Password": student.password}}
            json.dump(roster, class_roster)
            print(roster)
            class_roster.close()
        else:
            roster = json.load(class_roster)
            roster[student.student_id] = {"Name": student.name,
                                          "Nickname": student.nickname,
                                          "Password": student.password}
            class_roster.seek(0)
            class_roster.truncate()
            json.dump(roster, class_roster)
            print(roster)
            class_roster.close()


def change_password():
    with open('class_roster.txt', 'r+') as class_roster:
        roster = json.load(class_roster)
        student_id = input("Enter your Student ID: ")
        while True:
            old_password = input("Enter your old password: ")
            if old_password == roster[student_id]["Password"]:
                student = Student(roster[student_id]["Name"],
                                  roster[student_id]["Nickname"],
                                  roster[student_id],
                                  old_password)
                while True:
                    try:
                        new_password = input(
                            "The password must meet the following criteria:\n"
                            "* At least 8 characters long\n* At least 1 "
                            "lowercase letter\n* At least 1 uppercase "
                            "letter.\n\nEnter a new password: ")
                        student.password = new_password
                        break
                    except ValueError:
                        print("Invalid password entered.")
                roster[student_id]["Password"] = student.password
                class_roster.seek(0)
                class_roster.truncate()
                json.dump(roster, class_roster)
                print(roster)
                class_roster.close()
                return
            else:
                print("Invalid password.")
                continue

if __name__ == "__main__":
    # with open('class_roster.txt', 'r+') as class_roster:

    while True:
        choice = draw_main_menu()

        if choice == "01":
            choice = draw_teacher_menu()
            if choice == "01":
                add_student()
        elif choice == "02":
            choice = draw_student_menu()
            if choice == "01":
                change_password()
        elif choice.upper() == "Q":
            exit(1)
        else:
            print("Invalid entry. Enter 01, 02 or Q.")
            continue

