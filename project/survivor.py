class Survivor:
    initial_health =100
    initial_needs =100
    def __init__(self,name: str, age: int):
        self.age = age
        self.name = name
        self.health = Survivor.initial_health
        self.needs = Survivor.initial_needs

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value=="":
            raise ValueError("Name not valid!")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._validate_age(value)
        self._age = value

    def _validate_age(self, value):
        if value <0:
            raise ValueError("Age not valid!")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")

        self._health = value
        if self._health>100:
            self._health=100




    @property
    def needs(self):
        return self._needs
    # todo:

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")

        self._needs = value
        if self._needs>100:
            self._needs=100


    @property
    def needs_sustenance(self):
        return True if self.needs<100 else False

    @property
    def needs_healing(self):
        return True if self.health < 100 else False

    # def health_plus_value_more_than_100(self,value):
    #     if self.health+value>100:
    #         return True






#
# s=Survivor("N", 0)
# s.needs=80
# s.needs=120
# s.health=90
# s.health=120
# s.health=120
# print(s.needs)
# print(s.health)
#
# a=5
