from random import randint


class Die():
    '''Single die'''

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        '''simulating roll od the die'''
        return randint(1,self.num_sides)