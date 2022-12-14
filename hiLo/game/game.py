from game.card import Card
"""Calls the card file from the game folder"""
class Game:
    """This file will directly run the game, hence why it is called Game"""
    def _init_(self):
       """Contuctor for the Game file"""

       self.card = Card()
       self.is_playing = True
       self.total_score = 300
       self.horl = ""
       self.card.newCard()
       self.lastCard = 5
       
    def start_game(self):
        """"Main Game Loop"""
        while self.is_playing:
            self.get_inputs()
            self.check()
            self.do_outputs()
    
    def get_inputs(self):
        """Pretty much is the full game"""

        loop=True
        
        print(f"The card is: {self.lastCard}")
        while loop:
         self.horl = input("Next card is higher or lower? [h/l]: ")
         if self.horl =="h" or self.horl == "l":
            loop = False
         else:
            print("Please enter either h or l")
            print(" ")
            loop = True

    
    def check(self):
       """This is the method that controls the point and the rules of the game""" 
       ncard = self.card.newCard()
       print(f"The new card is: {ncard}")

       if self.lastCard > ncard and self.horl == "l":
        self.total_score = self.total_score + 100
       elif self.lastCard < ncard and self.horl == "h":
        self.total_score = self.total_score + 100
       elif self.lastCard > ncard and self.horl == "h":
        self.total_score = self.total_score -75
       elif self.lastCard < ncard and self.horl == "l":
        self.total_score = self.total_score - 75
     
        self.lastCard = ncard
    
    def do_outputs(self):
        """Checks if the Player wants to play again"""
        print(f"Your score is:{self.total_score}")
        loop = True

        if self.total_score <= 0:
            print("So sorry you lose! Gonna have to restart to play again!")
            self.is_playing = False
        else:
            while loop:
                again = input("Would you like to play again? [y/n] ")
                if again == "n":
                    print(f"You finished your game with {self.total_score} points. Goodbye!")
                    self.is_playing = False
                    loop = False
                elif again == "y":
                    print (" ")
                    loop = False
                else:
                    print("Please either enter y or n.")
                    print(" ")
                    loop = True







