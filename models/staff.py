from models.person import Person


class Staff(Person):

    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)


