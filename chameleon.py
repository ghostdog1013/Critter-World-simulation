# CS111 Intro to Programming
# Name: Shuhang Xue and Yilun Liu
# Instructor: Aaron Bauer
# HW6 Chameleon.py



import color, attack, direction
import random


class Chameleon():

    Attack = {}
    losecount = 0
    wincount = 0
    Fightcount = 0
    max = 0
    max_attack = attack.SCRATCH

    def __init__(self):
        self.count = 0
        self.fightcount = 0          # initialize the counting of each strategy to be zero.


    def fight(self, oppInfo):
        self.lastoppColor = oppInfo.color
        if self.fightcount == 0:
            attacks = [attack.SCRATCH, attack.ROAR, attack.POUNCE]
            return random.choice(attacks)
        else:                                   # assign the last opponent's action to chameleon

            return Chameleon.max_attack


    def getColor(self):
        if self.fightcount == 0:
            return color.GREEN
        else:
            return self.lastoppColor             # emulate last opponent's color

    def getMove(self, info):
        if Chameleon.wincount > Chameleon.losecount:
        # if Chameleon.loseCount < Chameleon.Fightcount * 0.5:
            if info.getNeighbor(direction.NORTH) != "." :
                return direction.NORTH

            if info.getNeighbor(direction.SOUTH) != "." :
                return direction.SOUTH

            if info.getNeighbor(direction.EAST) != "." :
                return direction.EAST

            if info.getNeighbor(direction.WEST) != "." :
                return direction.WEST
                                                    # The chameleon will always waits for its prey and goes
                                                    # to wherever a critter it can move to
            return direction.CENTER

        else:
            if info.getNeighbor(direction.NORTH) == "." :
                return direction.NORTH

            if info.getNeighbor(direction.SOUTH) == "." :
                return direction.NORTH

            if info.getNeighbor(direction.EAST) == "." :
                return direction.EAST

            if info.getNeighbor(direction.WEST) == "." :
                return direction.WEST

            return direction.CENTER


    def getChar(self):
            return 'C'                      # represented by 'C'

    def fightOver(self, won, oppAttack):             # (This satisfies the optional extension part)
        self.fightcount += 1
        self.lastoppAttack = oppAttack
        Chameleon.Fightcount += 1

        if oppAttack not in Chameleon.Attack:
            Chameleon.Attack[oppAttack] = 1
        else:
            Chameleon.Attack[oppAttack] += 1

        for oppAttack in Chameleon.Attack:
            if Chameleon.Attack[oppAttack] > Chameleon.max:
                Chameleon.max = Chameleon.Attack[oppAttack]
                Chameleon.max_attack = oppAttack


        if won == False:                    # Chameleon will use the attack that beats the most used
                                            # attack against the Chameleons so far
            Chameleon.losecount += 1
        else:
            Chameleon.wincount += 1
        pass

    def __str__(self):
        return self.__class__.__qualname__
