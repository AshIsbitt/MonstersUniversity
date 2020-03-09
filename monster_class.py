class Monster():
    def __init__(self, f_name, l_name, skill):
        self.__f_name = f_name
        self.__l_name = l_name
        self.__skill = skill

    # Getters
    def get_f_name(self):
        return self.__f_name

    def get_l_name(self):
        return self.__l_name

    def get_skills(self):
        for item in self.__skill:
            return item

    # Setters
    