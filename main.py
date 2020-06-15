import pygame
import art
import random

from game import Game

def main():
    finished = False
    print('WELCOME TO FAIQUESUCKSATSETSOTHESEAREHACKS.EXE')
    art.tprint('OwO', font='random')

    while not finished:
        num_cards = input('Number of cards on screen right now: ')
        print('Number of Cards on screen: ', num_cards)

        game = Game(num_cards)
        game.receive_attribute()
        game.iterator()

        quit_program = input('Are there more cards? ')
        if quit_program == 'n' or quit_program == 'N':
            art.tprint('Git Gud', font='random')
            finished = True


main()

