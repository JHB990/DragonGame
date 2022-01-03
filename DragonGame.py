import random

class Dragon:
    def __init__(self, name, kind, level, stats):
        self.name = name
        self.kind = kind
        self.level = level
        self.stats = stats
    def player(self):
        print('\tHello ', self.name, '\n\t\tYou are a : ', self.kind ,' Dragon\n\t\tYour level is ', self.level, '\n\t\tYour stats are: ', self.stats)


class Troll:
    def __init__(self):
        stats = {
            "level" : 10,
            "punch" : 5,
            "live" : 4,
            "back" : 2
        }


def game():
    print('Dragon')
    print('please enter the information of your dragon: ')
    dragon = Dragon(input('Name: '), input('kind: '), 1, 1)
    dragon.player()


game()
print('Wlecome to Ralthed the kingdom of the Imperial Dragons of the North, \n You live on Ascencia the capital of the Kingdom')