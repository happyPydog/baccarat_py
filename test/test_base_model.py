import os
import sys

sys.path.append(os.getcwd())

from baccarat.base_model import Card, Hand, Deck, Dealer


def main():

    #############
    # Test Card #
    #############
    card_1 = Card(number="A", suits="♡", point=1)
    card_2 = Card(number="10", suits="♡", point=0)
    card_3 = Card(number="7", suits="♡", point=7)
    card_4 = Card(number="5", suits="♡", point=5)

    print(f"{card_1.number = }, {card_1.suits = }, {card_1.point = }")

    # __repr__
    print(card_1)

    #############
    # Test Hand #
    #############
    player = Hand()
    banker = Hand()

    print(player)

    # __add__

    player += [card_1, card_3]
    banker += [card_2, card_4]

    print(player)

    print(f"{(player > banker) = }")

    # test __add__ TypeError
    # print(player + 1)

    #############
    # Test Deck #
    #############
    deck = Deck.make_deck() * 8

    ###############
    # Test Dealer #
    ###############
    dealer = Dealer()
    dealer.init(deck)
    dealer.shuffle()

    # Four cards are dealed at the beginning
    first_card = dealer.draw()
    first_card = dealer.draw()
    first_card = dealer.draw()
    first_card = dealer.draw()

    print(dealer.deck)

    dealer.reset()
    print(dealer.deck)
    print(deck)


if __name__ == "__main__":
    main()
