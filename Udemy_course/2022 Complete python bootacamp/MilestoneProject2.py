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

    def add_cards(self, new_cards, player=False):
        self.all_cards.append(new_cards)
        if player:
            self.print_values()

    def start_player(self, new_card1, new_card2, player=False):
        self.new_hand()
        self.all_cards.append(new_card1)
        self.all_cards.append(new_card2)
        if player:
            self.print_values()

    def bot_play(self, player_value, new_deck):
        print("Casino Hand :")
        number = 0
        while self.valueCasino() <= player_value and self.valueCasino() <= 21:
            self.all_cards.append(new_deck.deal_one())

        self.print_values()
        print()

    def valueCasino(self):
        list = []
        list.extend(self.countValues())
        number = 0
        if min(list)!= 0:
            number = min(list)
        for a in list:
            if a <= 21:
                number = a
        if number == 0:
            number = max(list)
        return number

    def showFirst(self):
        print("Casino Hand: ", self.all_cards[0].value)
        print(self.all_cards[0])

    def countValues(self):
        aces = False
        result = 0
        result2 = 0
        for a in self.all_cards:
            result = result + int(a.value)
            if int(a.value) == 1:
                aces = True
        if aces:
            result2 = int(result - 1 + 10)

        if result2 > result:
            temp = result2
            result2 = result
            result = temp
        return result, result2

    def lost(self):
        result, result2 = self.countValues()
        if result2 == 0:
            if result > 21:
                return True
        else:
            if result > 21 and result2 > 21:
                return True
        return False

    def print_values(self):
        result, result2 = self.countValues()

        cards = ""
        for a in self.all_cards:
            cards = a.rank + " of " + a.suit + " | " + cards

        print(result, end="")
        if result2 != 0:
            print("/", result2, end=" ")
        print()
        print(cards)

    def new_hand(self):
        self.all_cards.clear()


def valuePlayer(player_hand):
    list = []
    list.extend(player_hand.countValues())
    for a in list:
        if a <= 21:
            return int(a)


if __name__ == '__main__':
    player_hand = Hand("Jose", 10)
    casino_hand = Hand("Casino", 1000)

    player_hand.new_hand()
    new_deck = Deck()
    new_deck.shuffle()

    end = True
    while end:
        while True:
            if player_hand.money == 0:
                print("You are broke")
                exit()
            else:
                print("You have: ", player_hand.money)

                money = int(input("How much do you want to bet?"))
                if money > player_hand.money:
                    break
                player_hand.start_player(new_deck.deal_one(), new_deck.deal_one(), True)
                casino_hand.start_player(new_deck.deal_one(), new_deck.deal_one())
                casino_hand.showFirst()
                choise = input("Do you want to deal one? (1-yes 2-No)")

                while choise != "2":
                    player_hand.add_cards(new_deck.deal_one(), True)

                    if player_hand.lost():
                        print("Higher than 21 Lost")
                        break
                    choise = input("Do you want to deal one? (1-yes 2-No)")
                player_value = valuePlayer(player_hand)

                casino_hand.bot_play(player_value, new_deck)
                casino_value = valuePlayer(casino_hand)

                if player_value < casino_value:
                    player_hand.money = player_hand.money - money
                    casino_hand.money = casino_hand.money + money
                elif player_value > casino_value:
                    player_hand.money = player_hand.money + money
                    casino_hand.money = casino_hand.money - money

        # while True:
        #     choise = int(input("Do you want to deal one? (1-yes 2-No)"))
        #     while choise !=2:
        #         player_hand.add_cards(new_deck.deal_one())
        #         choise = int(input("Do you want to deal one? (1-yes 2-No)"))
