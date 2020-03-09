from monster_class import Monster

class Student(Monster):

    def __init__(self, f_name, l_name, skill, s_id = ""):
        super().__init__(f_name, l_name, skill)
        self.__student_id = s_id

    # Getters
    def get_student_id(self):
        return self.__student_id