from monster_class import Monster

class Teacher(Monster):

    def __init__(self, f_name, l_name, skill=[], t_id=""):
        super().__init__(f_name, l_name, skill)
        self.__teacher_id = t_id

    # Getters
    def get_teacher_id(self):
        return self.__teacher_id

