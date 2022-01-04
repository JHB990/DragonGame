import random

class Dragon:
    def __init__(self, name, kind, level, live):
        self.name = name
        self.kind = kind
        self.level = level
        self.live = live
    def player(self):
        print('\tHello ', self.name, '\n\t\tYou are a : ', self.kind ,' Dragon\n\t\tYour level is ', self.level, '\n\t\tYour stats are: ', self.stats)


class Troll:
    def __init__(self, level, punch, live, back):
        self.level = level
        self.punch = punch
        self.live = live
        self.back = back
    def enemy(self):
        print('\n\tTroll: \n\t', self.level, '\n\t\t', self.punch, '\n\t\t', self.live)


class game(Dragon, Troll):
    def gameStart():
        print('Dragon')
        print('please enter the information of your dragon: ')
        dragon = Dragon(input('Name: '), input('kind: '), 1, 1)
        dragon.player()
    def battle():
        a = 0
        b = 0
        c = 0
        d = 0
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        c = random.randint(1, 4)
        d = random.randint(1, 4)
        troll = Troll(a,b,c,d)
        troll.enemy()

        


game.gameStart()
print('Wlecome to Ralthed the kingdom of the Imperial Dragons of the North, \n You live on Ascencia the capital of the Kingdom')
print('just for try you see a Troll on the middle of the city just in fornt of the castle, you decide to defend the kingdom, the troll wants to destroy everything')
game.battle()