import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.allcards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.allcards.append(created_card)

    def shuffle(self):
        random.shuffle(self.allcards)

    def deal_one(self):
        return self.allcards.pop()


class Hand:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.all_cards = []

    def add_cards(self, new_cards):
        self.all_cards.append(new_cards)

    def start_player(self, new_card1, new_card2):
        self.all_cards.append(new_card1)
        self.all_cards.append(new_card2)

        self.print_values(new_card1, new_card2)

    def print_values(self, new_card1, new_card2):

        value1 = int(new_card1.value)
        value2 = int(new_card2.value)

        if value1 == 1 or value2 == 1:
            result = int(value1 + value2)
            print(new_card1.rank + " of " + new_card1.suit, "   ", new_card2.rank + " of " + new_card2.suit)
            print(result,end="/")
            if value1 == 1:
                result = int(10 + value2)
                print(result)
            elif value2 == 1:
                result = int(value1 + 10)
                print(result)
        else:

            result = int(value1 + value2)

            print(new_card1.rank + " of " + new_card1.suit, "   ", new_card2.rank + " of " + new_card2.suit)
            print(result)



    def new_hand(self):
        self.all_cards.clear()


if __name__ == '__main__':
    player_hand = Hand("Jose", 10)
    casino_hand = Hand("Casino", 1000)

    new_deck = Deck()
    new_deck.shuffle()

    end = True
    while end:
        while True:
            money = int(input("How much do you want to bet?"))
            if money <= player_hand.money:
                break

        player_hand.start_player(new_deck.deal_one(), new_deck.deal_one())
