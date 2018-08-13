from random import shuffle

colors = ("Schell", "Herz", "Laub", "Eichel")
values = ("7","8","9","10","U","D","K","A")



class SchafkopfDeck():
    def __init__(self):
        self.cards = []
        for color in colors:
            for value in values:
                self.cards.append(SchafkopfCard(color,value))

    def shuffle(self):
        shuffle(self.cards)

    def cards_left(self):
        return len(self.cards)

    def deal_card(self):
        if self.cards_left() < 1:
            return None
        else:
            return self.cards.pop() 

        

    def __repr__(self): 
        return str(self.cards)



class SchafkopfCard():
    def __init__(self,color,value):
        self.color = color
        self.value = value

    def __repr__(self):
        return f"{self.color} {self.value}"



class Player(): 
    def __init__(self,hand, name):
        self.hand = hand
        self.name = name

    def get_hand(self):
        return self.hand

    def __repr__(self):
        return f"Name: {self.name}."



class Move():
    def __init__(self, beginner, beginner_card):
        self.plays = []
        self.plays.append({"player": beginner, "card": beginner_card})

    def add_card(self, player, card):
        self.plays.append({"player": player, "card": card})

    def __repr__(self):
        return str( self.plays ) 



class Round():
    def __init__(self, move):
        self.moves = []
        self.moves.append(move)

    def add_move(self, move):
        self.moves.append(move)

    def __repr__(self):
        return str(self.moves)



deck1 = SchafkopfDeck()
deck1.shuffle()

eight_cards = []
while len(eight_cards) < 8:
    eight_cards.append(deck1.deal_card())
player1 = Player(eight_cards, "Hans")

eight_cards = []
while len(eight_cards) < 8:
    eight_cards.append(deck1.deal_card())
player2 = Player(eight_cards, "Peter")

eight_cards = []
while len(eight_cards) < 8:
    eight_cards.append(deck1.deal_card())
player3 = Player(eight_cards, "Horst")

eight_cards = []
while len(eight_cards) < 8:
    eight_cards.append(deck1.deal_card())
player4 = Player(eight_cards, "Hugo")

deck1.deal_card()

print(player1)
print(player2)
print(player3)
print(player4)

#move 1
move = Move(player1,player1.hand.pop(0))
move.add_card(player2,player2.hand.pop(0))
move.add_card(player3,player3.hand.pop(0))
move.add_card(player4,player4.hand.pop(0))
round1 = Round(move)
print(move)
#move 2
move = Move(player1,player1.hand.pop(0))
move.add_card(player2,player2.hand.pop(0))
move.add_card(player3,player3.hand.pop(0))
move.add_card(player4,player4.hand.pop(0))
round1.add_move(move)
#move 3
move = Move(player1,player1.hand.pop(0))
move.add_card(player2,player2.hand.pop(0))
move.add_card(player3,player3.hand.pop(0))
move.add_card(player4,player4.hand.pop(0))
round1.add_move(move)
#move 4
move = Move(player1,player1.hand.pop(0))
move.add_card(player2,player2.hand.pop(0))
move.add_card(player3,player3.hand.pop(0))
move.add_card(player4,player4.hand.pop(0))
round1.add_move(move)
#move 5
move = Move(player1,player1.hand.pop(0))
move.add_card(player2,player2.hand.pop(0))
move.add_card(player3,player3.hand.pop(0))
move.add_card(player4,player4.hand.pop(0))
round1.add_move(move)
#move 6
move = Move(player1,player1.hand.pop(0))
move.add_card(player2,player2.hand.pop(0))
move.add_card(player3,player3.hand.pop(0))
move.add_card(player4,player4.hand.pop(0))
round1.add_move(move)
#move 7
move = Move(player1,player1.hand.pop(0))
move.add_card(player2,player2.hand.pop(0))
move.add_card(player3,player3.hand.pop(0))
move.add_card(player4,player4.hand.pop(0))
round1.add_move(move)
#move 8
move = Move(player1,player1.hand.pop(0))
move.add_card(player2,player2.hand.pop(0))
move.add_card(player3,player3.hand.pop(0))
move.add_card(player4,player4.hand.pop(0))
round1.add_move(move)

print(round1.moves)