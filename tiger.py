# CS111 Intro to Programming
# Name: Shuhang Xue and Yilun Liu
# Instructor: Aaron Bauer
# HW6 Tiger.py



import color, attack, direction
import random

class Tiger():

    def __init__(self):
        self.count = 0              # Construct an instance variable to track the number of moves being made. 

    def fight(self, oppInfo):
        return attack.ROAR              # always attack.ROAR

    def getColor(self):
        if self.count % 2 == 0:
            return color.ORANGE
        else:
            return color.BLACK          # alternates between color.ORANGE and color.BLACK
                                        # (first color.ORANGE, then color.BLACK, then ...)

    def getMove(self, info):
        self.count += 1
        if (self.count - 1) % 3 == 0:
            moves = [direction.EAST, direction.SOUTH, direction.EAST, direction.WEST]
            self.move = random.choice(moves)
        return self.move                # moves 3 turns in a row in one random direction (direction.NORTH, direction.SOUTH, direction.EAST, or direction.WEST)
                                        # then chooses a new random direction and repeats


    def getChar(self):
            return 'T'

    def fightOver(self, won, oppAttack):

        pass

    def __str__(self):
        return self.__class__.__qualname__
