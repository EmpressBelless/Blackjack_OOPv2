import random

class Card:
  def __init__(self, suit, value):
    self.suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
    self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

  def facecard(self):
    if self.value == 'J' or 'Q' or 'K':
      self.value = 10

  def __repr__(self):
    return " of ".join((self.value, self.suit))

class Deck:
  def __init__(self):
      self.cards = []
  def shuffle(self):
    pass 
  def draw(self, something):
    cards = []
    deck_number = random.choice(Dealer.deck).pop()
    deck_suit = random.shuffle(Dealer.suit).pop()

    # for i in Dealer.deck:
    #   Dealer_hand = random.shuffle(Dealer.deck).pop()
    # for i in Dealer.suit:
    #   Dealer_hand = random.shuffle(Dealer.suit).pop()
    # for i in Dealer.deck:
    #   Player_hand = random.shuffle(Dealer.deck).pop()
    # for i in Dealer.suit:
    #   Player_hand = random.shuffle(Dealer.suit).pop()
  def hand():
    pass
class Player:
  def __init__(self, Player):
    self.player = Player

  def hit():
    pass
  def stand(self, value):
    # def discard(self):
    # how could I discard the deck or should I say we can only play once...
    pass


class Game:
  def run():
    while True:
      response = input("Welcome! Let's Play! Enter Play to begin: ")
      if response.lower == "Play":
        Deck.shuffle()
      if response.lower() == "hit":
        Player.hit()
      if response.lower() == "stand":
        Player.stand()
  run()



Player1 = Player("Suzette")
Player1.run()

#Class Name():
   #def init(self, last_n, f_n, age)
   #self. last-n = last_n
   #sef.first_n = first_n
  #  #self.age = age
  # #def say_if_minor(self):
  #   if self.age < 21:
  #     print("this patient is a minor")

  #instead of saying def say_if_minor(pid4343.first_n, 4343,last_n, pid4343.age)
  #you'd write
  # def say_if_minor(self)
