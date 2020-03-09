class Monster_Workshop:

    def __init__(self, subject, list_of_attendees, teacher):
        self.__subject = subject
        self.__list_of_attendees = list_of_attendees
        self.__teacher = teacher


    # Getters
    def get_subject(self):
        return self.__subject

    def get_list_of_attendees(self):
        return self.__list_of_attendees

    def get_teacher(self):
        return self.__teacher