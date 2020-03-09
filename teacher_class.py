from monster_class import Monster

class Teacher(Monster):

    def __init__(self, t_id):
        self.__teacher_id = t_id

    # Getters
    def get_teacher_id(self):
        return self.__teacher_id

