import sys

from teacher_class import Teacher
from student_class import Student
from workshop_class import Monster_Workshop

print("Welcome to Monsters University receptionist software")
print("----------------------------------------------------")
pw = input("Please enter password: ")

if not pw == "qwert":
    print("Error")
    sys.exit()

while True:
    print("Enter an option:")
    print("0. to exit")
    print("1. Create new student")
    print("2. Create new Teacher")
    option = input("")

    try:
        option = int(option)
    except ValueError:
        print("Incorrect entry.")
        continue

    if option == 0:
        print("Thank you, come again")
        sys.exit()
    elif option == 1:
        student1 = Student("Mike", "Wazowski")
        print("Succesful. {} {} added.".format(student1.get_f_name(), student1.get_l_name()))
    elif option == 2:
        teacher1 = Teacher("Filipe", "Paiva", t_id=1)
        print("Successful, {} {} added.".format(teacher1.get_f_name(), teacher1.get_l_name()))

