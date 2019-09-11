import random
#random.seed(1)
class Poker:
    money = 100
    rolls = 2
    dice_rolls = []
    def __init__(self):
        while self.money>0:
            print(f'Your money: ${self.money}')
            move = input('What is your move 1.play 2.quit:')
            if move == 'play':
                self.money -= 10 
                for i in range(5):
                    i = random.randint(1,6)
                    self.dice_rolls.append(i)
                print(f'Your current dice rolls : {self.dice_rolls}')
                move_2 = input('What is decision 1.roll 2.score now :')
                if move_2 == 'score':
                    print(self.score())
                elif move_2 == 'roll':
                    roll_index = input('Which is the dice you want to reroll:')
            elif move == 'quit':
                print(f'Your total money is ${self.money}')
                break
            else:
                print('Please try again cant recognise command.')




    
    def roll(self,dice_change):
        self.dice_rolls[dice_change] = random.randint(1,6)
    
    def value(self):
        return self.dice_rolls

    def reset_round(self):
        pass
    def start(self):
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
            return 'Five Of A Kind , +$30'
        elif len(unique) == 2:
            for i in unique:
                counts = self.dice_rolls.count(i)
                if counts == 3 or counts == 2:
                    self.money += 12
                    return 'Full House , +$12'
                else:
                    self.money += 15
                    return 'Four of a kind ,+$15'
        elif len(unique) == 3:
            for i in unique:
                counts = self.dice_rolls.count(i)
                if counts == 2:
                    self.money += 5
                    return 'Two Pair , +$5'
                elif counts == 3:
                    self.money += 8
                    return 'Three Of a kind ,+$8'
        if self.dice_rolls == [1,2,3,4,5] or self.dice_rolls == [2,3,4,5,6]:
            self.money += 20
            return 'Straight , +$20' 
        else:
            return 'Nothing matched'

poker_instance = Poker()

