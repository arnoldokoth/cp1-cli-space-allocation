from models.person import Person


class Fellow(Person):

    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)




