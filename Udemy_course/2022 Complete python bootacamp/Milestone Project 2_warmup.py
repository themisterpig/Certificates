# card
# suit, rank, Value
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# deck
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shufflle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


#   def __str__(self):

class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):

        if type(new_cards) == type([]):
            # Multiple cards
            self.all_cards.extend(new_cards)
        else:
            # One card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name}: has {len(self.all_cards)} cards.'


if __name__ == '__main__':

    new_playerOne = Player("Jose")
    new_playerTwo = Player("Mariana")

    new_deck = Deck()
    new_deck.shufflle()

    for x in range(26):
        new_playerOne.add_cards(new_deck.deal_one())
        new_playerTwo.add_cards(new_deck.deal_one())

    game_on = True

    round_num = 0
    while game_on:

        round_num += 1
        print(f"Round {round_num}")

        if len(new_playerOne.all_cards) == 0:
            print('Player One, out of cards! Player Two Wins!')
            break
        if len(new_playerTwo.all_cards) == 0:
            print('Player Two, out of cards! Player One Wins!')
            break

        player_one_cards = []
        player_one_cards.append(new_playerOne.remove_one())

        player_two_cards = []
        player_two_cards.append(new_playerTwo.remove_one())

        at_war = True

        while at_war:
            one_card = player_one_cards[-1].value
            two_card = player_two_cards[-1].value

            if one_card > two_card:
                new_playerOne.add_cards(player_one_cards)
                new_playerOne.add_cards(player_two_cards)

                at_war = False
                break
            elif two_card > one_card:
                new_playerTwo.add_cards(player_one_cards)
                new_playerTwo.add_cards(player_two_cards)

                at_war = False
                break
            else:
                print("War!")

                if len(new_playerOne.all_cards) < 5:
                    print("Player One unable to declare war")
                    print("Player TWO Wins!")
                    game_on = False
                    at_war = False
                    break
                elif len(new_playerTwo.all_cards) < 5:
                    print("Player Two unable to declare war")
                    print("PLAYER ONE WINS!")
                    game_on = False
                    at_war = False
                    break
                else:
                    for num in range(3):
                        player_one_cards.append(new_playerOne.remove_one())
                        player_two_cards.append(new_playerTwo.remove_one())
