import art
from game import Game


def main():
    finished = False
    print('WELCOME TO FAIQUESUCKSATSETSOTHESEAREHACKS.EXE')
    art.tprint('OwO', font='random')

    while not finished:
        game = Game()
        game.iterator()

        finished = True


main()
