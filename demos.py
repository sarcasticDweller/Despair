from main import *
class Demos:
    def __init__(self):
        # how are you supposed to do unit tests? this works for now
        pass

    def straight_demo(self):
        card1, card2, card3, card4, card5 = Card("heart", 1), Card("heart", 2), Card("heart", 3), Card("heart", 4), Card("spade", 5)
        deck1 = Deck([card1, card2, card3])
        print(f"deck1: {deck1}")
        print(f"is a straight of three? {deck1.is_straight(3)}")
        print(f"is a straight of four? {deck1.is_straight(4)}")
        deck2 = Deck([card1, card3, card4])
        print(f"deck2: {deck2}")
        print(f"is a straight of three? {deck2.is_straight(3)}")
        print(f"is a straight of four? {deck2.is_straight(4)}")
        deck3 = Deck([card1, card2, card5])
        print(f"deck3: {deck3}")
        print(f"is a straight of three? {deck3.is_straight(3)}")
        print(f"is a straight of four? {deck3.is_straight(4)}")
    
    def pair_demo(self):
        card1, card2, card3, card4, card5 = Card("heart", 1), Card("spade", 1), Card("heart", 3), Card("heart", 4), Card("spade", 5)
        deck1 = Deck([card1, card2])
        print(f"deck1: {deck1}")
        print(f"is a pair size 2? {deck1.is_pair(2)}")
        print(f"is a pair size 3? {deck1.is_pair(3)}")
        deck2 = Deck([card3, card4])
        deck1 = Deck([card1, card2])
        print(f"deck1: {deck2}")
        print(f"is a pair size 2? {deck2.is_pair(2)}")
        print(f"is a pair size 3? {deck2.is_pair(3)}")