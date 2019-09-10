import random
#random.seed(1)
class Poker:
    money = 100
    rolls = 2
    dice_rolls = []
    def __init__(self):
        self.money -= 10
        for i in range(5):
            i = random.randint(1,6)
            self.dice_rolls.append(i)
    
    def roll(self,dice_change):
        self.dice_rolls[dice_change] = random.randint(1,6)
    
    def value(self):
        return self.dice_rolls

    def reset_round(self):
        pass

    def score(self):
        self.dice_rolls.sort()
        unique = []
        for i in self.dice_rolls:
            if i in unique:
                pass
            else:
                unique.append(i)
        if len(unique) == 1:
            self.money += 30
            return 'Five Of A Kind'
        elif len(unique) == 2:
            for i in unique:
                counts = self.dice_rolls.count(i)
                if counts == 3 or counts == 2:
                    return 'Full House'
                else:
                    return 'Four of a kind'
        elif len(unique) == 3:
            for i in unique:
                counts = self.dice_rolls.count(i)
                if counts == 2:
                    return 'Two Pair'
                elif counts == 3:
                    return 'Three Of a kind'
        if self.dice_rolls == [1,2,3,4,5] or self.dice_rolls == [2,3,4,5,6]:
            self.money += 25
            return 'Straight' 
        else:
            return 'Nothing matched'

poker_instance = Poker()
print(poker_instance.score())
print(poker_instance.value())
print(poker_instance.roll(0))
print(poker_instance.value())
print(poker_instance.score())

