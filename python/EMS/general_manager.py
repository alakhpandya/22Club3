from manager import Manager

class GeneralManager(Manager):
    dep_id = "G"
    team_size = 100

    def __init__(self, name, age, gender, qualification):
        super().__init__(name, age, gender, qualification)