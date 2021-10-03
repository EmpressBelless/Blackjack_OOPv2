import random

class Card:
  def __init__(self, suit, value):
    self.suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
    self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

  def facecard(self):
    if self.value == 'J' or 'Q' or 'K':
      self.points = 10

  def show(self):
    print(f'("{self.suit} of {self.value}")')

class Deck:
  def __init__(self):
    self.cards = []
    self.shuffle()

  def shuffle(self):
    for i in range(1, 14):
      for j in ("Spades", "Clubs", "Diamonds", "Hearts"):
        self.cards.append(Card(j, i))
        print(f'("{i} of {j}")')
        print(len(self.cards))

deck = Deck()
deck.show()
#   def draw(self):
#     self.cards = []
#     deck_number = random.choice(self.value).pop()
#     deck_suit = random.choice(self.suit).pop()
#         # return " of ".join((self.value, self.suit))
#     print(f'("Player has {deck_number} and {deck_suit} ")')
# # class Player:

#     for i in Dealer.deck:
#       Dealer_hand = random.shuffle(Dealer.deck).pop()
#     for i in Dealer.suit:
#       Dealer_hand = random.shuffle(Dealer.suit).pop()
#     for i in Dealer.deck:
#       Player_hand = random.shuffle(Dealer.deck).pop()
#     for i in Dealer.suit:
#     #   Player_hand = random.shuffle(Dealer.suit).pop()
#   def hand():
#     pass

#   def hit():
#     pass

#   def stand(self, value):
#     # def discard(self):
#     # how could I discard the deck or should I say we can only play once...
#     pass

# class Game:
#   def run():
#     while True:
#       response = input("Welcome! Let's Play! Enter Play to begin: ").lower()
#       if response == "play":
#         Deck.shuffle(response)
#     # if response.lower() == "hit":
#     #   Player.hit()
#     # if response.lower() == "stand":
#     #   Player.stand()
#       else:
#         print("That is incorrect.  Please try again.")
#   run()
  #instead of saying def say_if_minor(pid4343.first_n, 4343,last_n, pid4343.age)
  #you'd write
  # def say_if_minor(self)
