#import packages
import random

class MultiSidedDie:
    first = 0
    random.seed(9001)
    def __init__(self,num_of_sides):
        self.num_of_sides = num_of_sides

    def roll(self):
        self.first = random.randint(1,self.num_of_sides)
        return self.first

    def set_value(self,value):
        self.first = value

    def get_value(self):
        return self.first 

dice_instance = MultiSidedDie(5)
print(dice_instance.roll())


