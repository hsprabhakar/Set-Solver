
class Game:
    def __init__(self, num_cards):

        self.num_cards = 0
        self.list_of_cards = []


    def receive_attribute(self):

        for _ in range(self.num_cards):

            proper_num = False
            while not proper_num:
                number = (input('Number (1-3)'))
                if type(number) != int:
                    print('No wonder ur ass at this game..',
                          number, 'aint a fkin number')

                elif number not in range(1,4):
                    print('dumbass foo choose a number between 1-3, not',
                          number, 'smfh..')

                else:
                    proper_num = True

            #--------------------------------------------

            proper_shape = False
            while not proper_shape:
                shape = input('Shape: \n OVAL = 1 \n DIAMOND = 2 \n'
                              ' SQUIGGLY = 3')

                if type(shape) != int:
                    print('Bitchass really chose ',
                          shape, 'as a shape...')

                elif shape not in range(1, 4):
                    print('Fat fingers or u dum')

                else:
                    proper_shape = True

            #--------------------------------------------------

            proper_colour = False
            while not proper_colour:
                colour = input('Shape: \n OVAL = 1 \n DIAMOND = 2 \n'
                              ' SQUIGGLY = 3')

                if type(colour) != int:
                    print('Colourblind? ',
                          number, 'isnt a colour...')

                elif colour not in range(1, 4):
                    print('1, 2, or 3!!$!%^%!$!')

                else:
                    proper_colour = True

            self.list_of_cards.append([number, shape, colour])



    def calculate(self):
        # rule 1
        #Nothing matches

        pass




