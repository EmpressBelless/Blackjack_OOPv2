import random

class Card:
  def __init__(self, suit, value):
    self.suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
    self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

  def facecard(self, points):
    if self.value == 'J' or 'Q' or 'K':
      self.points = 10

  def show(self):
    print(f'("{self.suit} of {self.value}")')

amazing = Card()
amazing.show()
class Deck:
  def __init__(self):
    self.cards = []
    self.shuffle()

  def shuffle(self): #missing one argument
    for i in range(1, 14):
      for j in ("Spades", "Clubs", "Diamonds", "Hearts"):
        self.cards.append(Card(j, i))
        # print(f'("{i} of {j}")')

  def draw(self):
    return self.cards.pop()
    # print(f'("Player has {deck_number} and {deck_suit} ")')

class Player:
  def __init__(self, name):
    self.name = name
    self.hand = []

  def draw(self):
    self.hand.append(Deck.draw())
    return self

  def hand(self):
    for card in self.hand:
      card.show()

  def hit():
    pass

  def stand(self, value):
    pass

class Game:
  def run():
    response = input("Welcome! Let's Play! Enter Play to begin: ")
    if response.lower() == "play":
      Deck.shuffle(self)  #I think this expects an attribute
    elif response.lower() == "hit":
      Player.hit()
    elif response.lower() == "stand":
      Player.stand()
    else:
      print("That is incorrect.  Please try again.")
  run()
