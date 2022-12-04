class Player:
    def __init__(self):
       self._guess = " "
       self._attempts = 4
    
    def get_guess(self):
        return self._guess

    def set_guess(self,guess):
        self._guess = guess
    
    def bad_attempt(self):
        self._attempts = self._attempts - 1

    def parachute(self):
        if self._attempts == 4:
            print(" ____ ")
            print("/____\\")
            print("\\    /")
            print("  \\ /")
            print("    O   ")
            print("   /|\\ ")
            print("   / \\  ")
            print("\n")
            print("^^^^^^^^^^^")
        elif self._attempts == 3:
            print("/____\\")
            print("\\    /")
            print("  \\ /")
            print("    O   ")
            print("   /|\\ ")
            print("   / \\  ")
            print("\n")
            print("^^^^^^^^^^^")
        elif self._attempts == 2: 
            print("\\    /")
            print("  \\ /")
            print("    O   ")
            print("   /|\\ ")
            print("   / \\  ")
            print("\n")
            print("^^^^^^^^^^^")
        elif self._attempts == 1:
            print("  \\ /")
            print("    O   ")
            print("   /|\\ ")
            print("   / \\  ")
            print("\n")
            print("^^^^^^^^^^^")
        elif self._attempts == 0:
            print("    X   ")
            print("   /|\\ ")
            print("   / \\  ")
            print("\n")
            print("^^^^^^^^^^^")
            
    def ending(self):
        if self._attempts != 0:
            return True
        else:
            print("Sorry You Died! Goodbye")
            return False