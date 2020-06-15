class Game:
    def __init__(self, num_cards):

        self.num_cards = int(num_cards)
        self.list_of_cards = []

    def receive_attribute(self):

        for _ in range(self.num_cards):

            proper_num = False
            while not proper_num:
                number = int((input('Number of shit on card (1-3)  ')))


                if number not in range(1, 4):
                    print('dumbass foo choose a number between 1-3, not',
                          number, 'smfh..')

                else:
                    proper_num = True

            # --------------------------------------------

            proper_shape = False
            while not proper_shape:
                shape = int(input('Shape: \n OVAL = 1 \n DIAMOND = 2 \n'
                              ' SQUIGGLY = 3 \n'))


                if shape not in range(1, 4):
                    print('Fat fingers or u dum')

                else:
                    proper_shape = True

            # --------------------------------------------------

            proper_colour = False
            while not proper_colour:
                colour = int(input('RED: 1 \n GREEN = 2 \n BLUE = 3 \n'))


                if colour not in range(1, 4):
                    print('1, 2, or 3!!$!%^%!$!')

                else:
                    proper_colour = True

            proper_shade = False
            while not proper_shade:
                shade = int(input('EMPTY: 1 \n LINE = 2 \n FILL = 3 \n'))


                if shade not in range(1, 4):
                    print('1, 2, or 3!!$!%^%!$!')

                else:
                    proper_shade = True

            self.list_of_cards.append([number, shape, colour, shade])

    def iterator(self):

        card_1_index = 0
        card_2_index = 1
        card_3_index = 2
        setFound = False
        finished = False
        length_of_cards = len(self.list_of_cards)

        while not setFound and not finished:

            # card_1, 2, and 3 are the list of attributes (the card) within the overall list

            card_1 = self.list_of_cards[card_1_index]
            card_2 = self.list_of_cards[card_2_index]
            card_3 = self.list_of_cards[card_3_index]

            setFound = self.calculate(card_1, card_2, card_3)

            if setFound:  # if set found when calculating current card
                print('Yooo set has been found!')
                # convert to card number starting from 1 for ease
                CARD_1 = card_1_index + 1
                CARD_2 = card_2_index + 1
                CARD_3 = card_3_index + 1
                setFound = True
                print('Hope you feel smart...your cards are...: \n', CARD_1, CARD_2, CARD_3)

            # iterator part------
            if card_3_index < length_of_cards - 1:  # card_3 has not reached end of its iteration
                card_3_index += 1

            elif card_3_index == length_of_cards - 1 and card_2_index < length_of_cards - 2:  # card_3 has reached end of iteration AND card_3 has NOT
                # reached end of iteration

                card_2_index += 1
                card_3_index = card_2_index + 1
                # card 2 go up by 1
                # card 3 go up by 1 + new card 2


            elif card_3_index == length_of_cards - 1 and card_2_index == length_of_cards - 2:  # if both card_3 and card_2 reach end of their iterations

                if card_1_index < length_of_cards - 3:
                    card_1_index += 1
                    card_2_index = card_1_index + 1
                    card_3_index = card_2_index + 1
                elif card_1_index == length_of_cards - 3:
                    finished = True

        if finished == True and not setFound:
            print('ERROR: If you are seeing this message, youre fucked cuz you shouldnt be lmao')


    def calculate(self, card_1, card_2, card_3):

        attribute = 0
        set_found = False
        attribute_match = 0  # All 3 cards have a same value for attribute
        attribute_unique = 0  # All 3 cards have unique value for attribute

        while attribute < 4:
            unique_check = []

            if card_1[attribute] == card_2[attribute] == card_3[attribute]:
                attribute_match += 1  # We found an attribute that is common on the 3 cards!

            else:
                unique_check.append(card_1[attribute])
                unique_check.append(card_2[attribute])
                unique_check.append(card_3[attribute])

                if len(unique_check) == len(set(unique_check)):
                    attribute_unique += 1

            attribute += 1

        if (attribute_match == 0 and attribute_unique == 4) or (attribute_match == 1 and attribute_unique == 3) or (
                attribute_match == 2 and attribute_unique == 2) or (attribute_match == 3 and attribute_unique == 1):
            set_found = True

        return set_found

        pass
