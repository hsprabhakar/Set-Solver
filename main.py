import pygame
import game


def main():
    finished = False
    print('WELCOME TO FAIQUESUCKSATSETSOTHESEAREHACKS.EXE')

    while not finished:
        num_cards = input('Number of cards on screen right now: ')
        print('Number of Cards on screen: ', num_cards)

        Screen = game(num_cards)



main()

