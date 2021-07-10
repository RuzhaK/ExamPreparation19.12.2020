from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors=[]
        self.supplies=[]
        self.medicine=[]

    # todo - tezi trite moje bi ne triabwa da sa taka

    @property
    def food(self):
        try:
            food_objects=[s for s in self.supplies if s.__class__.__name__=="FoodSupply"]
        except IndexError():
            return "There are no food supplies left!"

        return food_objects

    @property
    def water(self):
        try:
            water_objects = [s for s in self.supplies if s.__class__.__name__ == "WaterSupply"]
        except IndexError():
            return "There are no water supplies left!"

        return water_objects

    @property
    def painkillers(self):
        try:
            painkillers = [s for s in self.medicine if s.__class__.__name__ == "Painkiller"]
        except IndexError():
            return "There are no painkillers left!"

        return painkillers

    @property
    def salves(self):
        try:
            salves = [s for s in self.medicine if s.__class__.__name__ == "Salve"]
        except IndexError():
            return "There are no salves left!"

        return salves

    def add_survivor(self,survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError( f"Survivor with name {survivor.name} already exists.")

        self.survivors.append(survivor)

    def add_supply(self,supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self,medicine: Medicine):

        self.medicine.append(medicine)

    def heal(self,survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            medicine_found=[m for m in self.medicine if m.__class__.__name__==medicine_type][-1]
            medicine_found.apply(survivor)
            self.medicine.remove(medicine_found)
            return f"{survivor.name} healed successfully with {medicine_type}"




    def sustain(self,survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            supply_found = [m for m in self.supplies if m.__class__.__name__== sustenance_type][-1]
            supply_found.apply(survivor)
            self.supplies.remove(supply_found)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs-=2*s.age
        for i in range (len(self.survivors)):
            if self.survivors[i].needs_sustenance:
                food_item=self.food[0]
                food_item.apply(self.survivors[i])
                b.supplies.remove([s for s in b.supplies if s.__class__.__name__ == "FoodSupply"][0])
            # if self.survivors[i].needs_sustenance:
                water_item=self.water[0]
                b.supplies.remove([s for s in b.supplies if s.__class__.__name__ == "WaterSupply"][0])

                water_item.apply(self.survivors[i])


# todo дава грешка последния неясно защо
# b=Bunker()
#
# s=Survivor("N1",2)
# s1=Survivor("N2",3)
# s3=Survivor("N3",4)
# fp1=FoodSupply()
# fp2=FoodSupply()
# fp3=FoodSupply()
# fp4=FoodSupply()
# wp1=WaterSupply()
# wp2=WaterSupply()
# wp3=WaterSupply()
# m1=Salve()
# m2=Salve()
# m3=Painkiller()
# m4=Painkiller()
# b.add_survivor(s)
# # b.add_survivor(s1)
# # b.add_survivor(s3)
# b.add_supply(fp1)
# b.add_supply(fp2)
# b.add_supply(fp3)
# b.add_supply(fp4)
# b.add_supply(wp1)
# b.add_supply(wp2)
# # b.add_supply(wp3)
# b.add_medicine(m1)
# b.add_medicine(m2)
# b.add_medicine(m3)
# b.add_medicine(m4)
# s.health=80
# b.heal(s,"Salve")
# s1.health=90
# b.heal(s1,"Painkiller")
# s3.needs=10
# s.health=80
# s.needs=10
# b.sustain(s3,"WaterSupply")
#
# b.next_day()
#
#
#
#
# a=5