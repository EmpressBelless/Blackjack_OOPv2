import random

class Card:
  def __init__(self, suit, value):
    self.suit = suit
    # ["Hearts", "Spades", "Clubs", "Diamonds"]
    self.value = value
    # ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

  def show(self):
    print(f'("{self.suit} of {self.value}")')

class Deck:
  def __init__(self):
    self.cards = []
    self.build()

  def build(self): 
    for i in range(1,14):
      for j in ("Spades", "Hearts", "Diamonds", "Clubs"):
        self.cards.append(Card(i, j))
    Deck.shuffle(self)
        #print(f'("{i} of {j}")')

  def shuffle(self): #shuffles my deck
    random.shuffle(self.cards)

  def show(self): # if I want to see all of the cards in my deck
    for see in self.cards:
      Deck.show(see)

  def draw(self):  # I pop(1) card out of my list and put it in single_card. Deck should already be shuffled. 
    single_card = self.cards.pop()
    return single_card

class Player:
  def __init__(self, name):
    self.name = name
    self.playerhand = []

  def draw(self): #This is for player. confirmation confirmed how many cards he drew
    playerhand = Deck.cards.pop(self)
    print(f'("Player drew {len(self.playerhand)} cards")')

  def showhand(self):
    for card in self.playerhand:
      Card.showhand(card)

class Dealer(Player):
  def __init__(self, name):
      super().__init__(name)
      self.value = 0
      self.aces = 0
      self.dealerhand = []

  def draw(self):  #Dealer draws cards and they're stored in dealer_hand
    self.dealerhand = Deck.cards.pop(self)
    print(f'("Player drew {len(self.dealerhand)} cards")')

#   def hit():
#     pass

#   def stand(self, value):
#     pass
newplayer = Deck()
newplayer1 = newplayer
class Game:

  def run():
    while True:
      response = input("Welcome! Let's Play! Enter Play to begin: ")
      if response.lower() == "play":
          Deck.build(newplayer1)
          print("Deck has been shuffled!")
          Dealer.draw(newplayer1)
          Dealer.draw(newplayer1)
          Player.draw(newplayer1)
          Player.draw(newplayer1)
          Player.showhand()
      elif response.lower() == "hit":
        Player.hit()
        player.Deck.draw()
        Dealer.Deck.draw()
      elif response.lower() == "stand":
        Player.stand()
      else:
        print("That is incorrect.  Please try again.")
  run()

  

