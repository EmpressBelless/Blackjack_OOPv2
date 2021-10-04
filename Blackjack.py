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
    self.shuffle()
  

  def build(self): 
    for i in range(1,14):
      for j in ("Spades", "Hearts", "Diamonds", "Clubs"):
        self.cards.append(Card(i, j))
        print(f'("{i} of {j}")')
    return self.cards
        
  def shuffle(self): #shuffles my deck
    random.shuffle(self.cards)
    print("New Deck Shuffled!")

  def show(self): # if I want to see all of the cards in my deck
    for see in self.cards:
      Deck.show(see)

  def draw(self):  # I pop(1) card out of my list and put it in single_card. Deck should already be shuffled. 
    single_card = self.cards.pop()
    return single_card

class Player(Deck):
  def __init__(self, name):
    self.name = name
    self.playerhand = []
    self.playerhandlist = []

  def __repr__(self): #correct this
      return super().__repr__()

  def draw(self): #This is for player. confirmation confirmed how many cards he drew
    self.playerhand = self.cards.pop()
    # return f'("Player drew {len(playerhand)} cards")'

  def showhand(self):  #correct this
      print(repr(self.playerhand))

class Dealer(Player):
  def __init__(self, name):
      super().__init__(name)
      # self.value = 0
      # self.aces = 0
      self.dealerhand = []

  def draw(self):  #Dealer draws cards and they're stored in dealer_hand
    dealerhand = self.cards.pop()
    # dealer_hand_count = len(dealerhand)
    # return f'("Player drew {dealer_hand_count} cards")'

#   def hit():
#     pass

#   def stand(self, value):
#     pass

class Game:
  def run():
    Deck() #This just activates the deck and shuffles. 
    while True:
      name = input("Welcome! Let's Play! Who will the Dealer be going up against today?: ")
      response = input(f'("Awesome! To begin {name} type play:")')
      if response.lower() == "play":
        while Dealer.dealerhand == []:
          Dealer.dealerhand = Deck.cards.pop()  #or dealer.draw()
          Dealer.dealerhand = Deck.cards.pop()
          print(f'("Dealer has {len(Dealer.dealerhand)} cards")')
        while Player.playerhand == []:
          Player.playerhand = Deck.cards.pop() #or player.draw()
          Player.playerhand = Deck.cards.pop()
          print(f'("Player has {len(Player.playerhand)} cards")')

        Player.showhand()
      elif response.lower() == "hit":
        Player.hit()
        player.Deck.draw()
        Dealer.Deck.draw()
      elif response.lower() == "stand":
        Player.stand()
      else:
        print("That is incorrect.  Please try again.")

newplayer = Game()
newplayer = "Suzette"
Game.run()

  

