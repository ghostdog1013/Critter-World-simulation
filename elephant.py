# CS111 Intro to Programming
# Name: Shuhang Xue and Yilun Liu
# Instructor: Aaron Bauer
# HW6 Elephant.py

import color, attack, direction

class Elephant():

    def __init__(self, steps):
        self.steps = steps
        self.count = 0

    def fight(self, oppInfo):
        if oppInfo.char == "T":
            return attack.ROAR              # if opponent displays as a Tiger (with the character 'T')
                                            # then attack.ROAR; otherwise attack.POUNCE
        else:
            return attack.POUNCE

    def getColor(self):
        return color.GRAY                   # always return gray.

    def getMove(self, info):
        self.count += 1
        if (self.count - 1) % self.steps == 0 and (self.count - 1) / self.steps % 4 == 0:
            self.move = direction.SOUTH
        if (self.count - 1) % self.steps == 0 and (self.count - 1) / self.steps % 4 == 1:
            self.move = direction.WEST
        if (self.count - 1) % self.steps == 0 and (self.count - 1) / self.steps % 4 == 2:
            self.move = direction.NORTH
        if (self.count - 1) % self.steps == 0 and (self.count - 1) / self.steps % 4 == 3:
            self.move = direction.EAST                              # first go direction.SOUTH steps times
                                                                    # then go direction.WEST steps times
                                                                    # then go direction.NORTH steps times
                                                                    # then go direction.EAST steps times (a clockwise square pattern), then repeats
        return self.move


    def getChar(self):
            return 'E'

    def fightOver(self, won, oppAttack):

        pass

    def __str__(self):
        return self.__class__.__qualname__
