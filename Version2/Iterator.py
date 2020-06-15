card_1 = 0
card_2 = 1
card_3 = 2
CARDS = ['a', 'b', 'c', 'd', 'e']
length_of_cards = len(CARDS)

finished = False
while not finished:

    print(CARDS[card_1], CARDS[card_2], CARDS[card_3])

    # Iterate Cards 2 and 3
    if card_3 < length_of_cards - 1:
        card_3 += 1
    elif card_3 == length_of_cards - 1:
        card_2 += 1
        card_3 = card_2 + 1

    # Iterate Card 1
    if card_2 == length_of_cards - 2 and card_3 == length_of_cards - 1:
        card_1 += 1
        card_2 = card_1 + 1
        card_3 = card_2 + 1

    if card_1 == length_of_cards - 3 and card_2 == length_of_cards - 1 and card_3 == length_of_cards:
        print("AHAHAHA IT WORKS")
        finished = True