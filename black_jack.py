#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:16:08 2019

@author: Sooraj
"""

# Defining global variables
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'
         , 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True # Variable to switch the while loop if the count is greater 
               # than 21

class Card:
    """
    This class accepts the rank and suits as input and create a card output
    having those inputs eg- "two" of "hearts". The __str__ module returns the 
    output as string
    """
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
        
    def __str__(self):
        return self.ranks+" of "+self.suits
    
class Deck:
    """
    The deck class loads all the cards(with rank & suits) into the deck. A 
    total of 52 cards will be loaded in the deck. From this deck a deal
    (card drawing) can be made after shuffling the deck
    """
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) # loading into deck
    
    def __str__(self):
        deck_comp=''
        for card in self.deck: # from the loaded deck, returning string
            deck_comp +='\n'+ card.__str__() 
        return deck_comp
                                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card=self.deck.pop() # Drawing a card from deck
        return single_card
    
# Testing the deck
#test_deck=Deck()
#test_deck.shuffle() # to shuffle the deck list
#print(test_deck)

class Hand:
    """
    This class is defines the hand that the player have. The hand is made by
    taking each card from the deck and then adding the value to it. The max 
    value is 21. There is also additional information to add for aces values
    to it
    """
    
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.ranks]
        
        # If ace card
        if card.ranks=='Ace':
            self.aces+=1
        
    def adjust_for_ace(self):
        # This will be used if the total value of the hand is 21, then the 
        # value of the ace will be changed from 11 to just 1
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1
     
# Player side
#test_player=Hand()
#pulled_card=test_deck.deal()
#test_player.add_card(pulled_card)
#print("\nPlayer drawing a card from deck and adding to hand :")
#print(pulled_card)
#print(test_player.value)

class chips:
    """
    This class deals with how many chips the player started in the game.
    Initially, the game starts with 100(default value). The depending on the
    bet the player wins or loses.
    """
    
    def __init__(self,total=100):
        self.total=total
        self.bet=0
        
    def win_bet(self):
        self.total+=self.bet
        
    def lose_bet(self):
        self.total-=self.bet
        
# Bet declaration        
def take_bet(chips):
    """
    This function is used for validation to see of the bet made is valid or not
    """
    
    while True:
        try:
            chips.bet=int(input("Enter the bet you needed : "))
        except:
            print("Enter integer values only !")
        else:
            if chips.bet>chips.total:
                print("Sorry you dont have enough chips !")
            else:
                break
            
# Playing scenario - hit or stand
def hit(deck,hand):
    """
    This function is used to take the card from the deck to the hand. The 
    dealer will provide the card to the player from the deck
    """
    
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    """
    This function is used to check if the player want to hit or stand.
    """
    global playing
    
    while True:
        x=input("Do you want to hit or stand ? Enter h or s : ")
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print("Player stands, dealers turn ")
            playing=False
        else:
            print("Please enter the correct options !")
            continue
        break
    
# Card showing section   
def show_some(player,dealer):
    """
    This function is used to show some of the cards. While drawing from deck,
    the first card will be faced down for both the dealer and the player. 
    Now this function invoked will be from the players perspective.
    """
    print("\nDEALER HAND")
    print("Dealers first card hidden")
    print(dealer.cards[1])
    print('\n')
    print("PLAYER HAND")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    """
    This function is to flip and show all the cards for both dealers and players
    to see which one has gone bust
    """
    print("DEALER HAND")
    for card in dealer.cards:
        print(card)
    
    print("PLAYER HAND")
    for card in player.cards:
        print(card)
        
# Game scenarios
def player_bust(player,dealer,chips):
    print("\nPLAYER BUST")
    chips.lose_bet()

def player_win(player,dealer,chips):
    print("\nPLAYER WINS")
    chips.win_bet()

def dealer_bust(player,dealer,chips):
    print("\nDEALER WINS")
    chips.win_bet()

def dealer_win(player,dealer,chips):
    print("\nDEALER BUST, PLAYER WINS")
    chips.lose_bet()

def push(player,dealer):
    print('\nDEALER AND PLAYER TIE ! PUSH')
    
# Main game layout
while True:
    
    #Welome message
    print("\nWelcome to BlackJack!")
    
    #Creating a deck
    deck=Deck()
    deck.shuffle()
    
    #Creating a hand for player and dealer. Two times taken as first card is 
    #hidden no value
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Setting up players chips(account)
    player_chips=chips()
    
    # Asking the player for bet
    take_bet(player_chips)
    
    #Now the game starts and then cards can be shown, first card by the dealer
    #will remain hidden
    show_some(player_hand,dealer_hand)
    
    #Player can hit or stand which is done with the "playing" global variable
    while playing:
        hit_or_stand(deck,player_hand)
        
        #See the cards partially, just to see for player if 21 is reached
        show_some(player_hand,dealer_hand)
        
        #If player hand >21 means player bust and break
        if player_hand.value>21:
            player_bust(player_hand,dealer_hand,player_chips)
            break
        
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        # the playing is compared with dealers card values in mind
        if player_hand.value<=21:
            
            #This for hit for dealer as for player its already done
            while dealer_hand.value<player_hand.value:
                hit(deck,dealer_hand)
            
            # Show all cards. From the dealer perspective, to know how much value
            show_all(player_hand,dealer_hand)
            
            # Run different winning scenarios
            if dealer_hand.value>21:
                dealer_bust(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value>player_hand.value:
                dealer_win(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value<player_hand.value:
                player_win(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)
            
        # Inform Player of their chips total
        print("\nThe total chips the player has is: {}".format(player_chips.total))
        
        # Ask to play again
        option=input("\nDo you want to play again ? y or n : ")
        
        if option[0].lower()=='y':
            playing=True
            continue
        else:
            print("Thanks for playing!")
            break