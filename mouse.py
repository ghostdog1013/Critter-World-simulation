# CS111 Intro to Programming
# Name: Shuhang Xue and Yilun Liu
# Instructor: Aaron Bauer
# HW6 Mouse.py



import color, attack, direction

class Mouse():

    def __init__(self, color):
        self.color = color
        self.count = 0                  # construct an instance variable to track the number of moves being made.

    def fight(self, oppInfo):
        return attack.SCRATCH           # always return SCRATCH as the stretegy.

    def getColor(self):
        return self.color

    def getMove(self, info):
        self.count += 1
        if self.count % 2 == 1:
            return direction.EAST
        else:
            return direction.SOUTH              # alternates between east and south

    def getChar(self):
            return 'M'                          # always return M as the representative letter

    def fightOver(self, won, oppAttack):

        pass

    def __str__(self):
        return self.__class__.__qualname__
