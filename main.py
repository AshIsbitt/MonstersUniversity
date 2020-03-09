import sys
import time as t

from teacher_class import Teacher
from student_class import Student
from workshop_class import Monster_Workshop

PASSWORD = "q"

print("Welcome to Monsters University receptionist software")
print("----------------------------------------------------")
pw = input("Please enter password: ")

if not PASSWORD == "q":
    print("Error")
    sys.exit()

while True:
    print("Enter an option:")
    print("0. to exit")
    print("1. Create new student")
    print("2. Create new Teacher")
    print("4. Create Workshop")
    print("5. Add student skills")
    print("6. List all skills")
    option = input("")

    try:
        option = int(option)
    except ValueError:
        print("Incorrect entry.")
        continue

    if option == 0:
        print("Thank you, goodbye")
        sys.exit()

    elif option == 1:
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        student1 = Student(f_name, l_name)
        print("Succesful. {} {} added.".format(student1.get_f_name(), student1.get_l_name()))

    elif option == 2:
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        teacher1 = Teacher("Filipe", "Paiva", t_id=1)
        print("Successful, {} {} added.".format(teacher1.get_f_name(), teacher1.get_l_name()))

    elif option == 4:
        ws_id = input("Enter class name: ")
        workshop1 = Monster_Workshop(ws_id, 14, teacher1.get_f_name())
        print("Successful. {} class created with {} teacher".format(ws_Devops.get_subject(), ws_Devops.get_teacher()))

    elif option == 5:
        entry = input("Enter new skill: ")
        print(student1.set_skill(entry.capitalize()))

    elif option == 6:
        print("\nUser skills:")

        item_index = 1

        for item in student1.get_skills():
            print(str(item_index) + ". " + item)
            item_index += 1
            t.sleep(.5)

    print("-----------")
    print(" ")