import sys
import time as t

from teacher_class import Teacher
from student_class import Student
from workshop_class import Monster_Workshop

PASSWORD = "q"
teacher_list = []
student_list = []
workshop_list = []

print("Welcome to Monsters University receptionist software")
print("----------------------------------------------------")
pw_entry = input("Please enter password: ")

if not pw_entry == PASSWORD:
    print("Error")
    sys.exit()

while True:
    print("Enter an option:")
    print("0. to exit")
    print("1. Create new student")
    print("2. Create new Teacher")
    print("3. Create Workshop")
    print("4. List all workshops")
    print("5. Add student skills")
    print("6. List all skills")
    option = input("\nEntry: ")

    try:
        option = int(option)
    except ValueError:
        print("Incorrect entry.\n")
        continue

    if option == 0:
        print("Thank you, goodbye")
        sys.exit()

    elif option == 1:
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        student_list.append(Student(f_name, l_name))
        print("Successful. {} {} added.".format(student_list[-1].get_f_name(), student_list[-1].get_l_name()))

    elif option == 2:
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        teacher_list.append(Teacher(f_name, l_name))
        print("Successful, {} {} added. ID - {}".format(teacher_list[-1].get_f_name(),
                                                        teacher_list[-1].get_l_name(),
                                                        len(teacher_list)))

    elif option == 3:
        ws_id = input("Enter class name: ")
        t_id = int(input("Enter teacher ID number: ")) - 1
        workshop_list.append(Monster_Workshop(ws_id, 14, teacher_list[t_id].get_f_name()))
        print("Successful. {} class created with {} teacher".format(workshop_list[-1].get_subject(),
                                                                    workshop_list[-1].get_teacher()))

    elif option == 4:
        print("\nCurrent Workshops:")
        for item in workshop_list:
            print(item.get_subject())

    elif option == 5:
        s_id = int(input("Enter student number: ")) - 1
        entry = input("Enter new skill: ")
        print(student_list[s_id].set_skill(entry.capitalize()))

    elif option == 6:
        s_id = int(input("Enter student ID: ")) - 1
        print("\nUser skills:")

        item_index = 1

        for item in student_list[s_id].get_skill():
            print(str(item_index) + ". " + item)
            item_index += 1
            t.sleep(.5)

    else:
        print("Invalid value")

    print("-------------------")
    print(" ")