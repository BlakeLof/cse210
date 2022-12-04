import random


class Word:

    def _init_(self):
        self.number = random.randint(1, 5)
        self._words = ["apple", "jefferson","brigham","programming","cartridge"]
        self._the_word = self._words[self.number]
        self._letters =  []
        self._guessed = []
        self._right = 0
    
    
    def get_word(self):
        return self._the_word
    
    def split(self, word):
        for letter in word:
            self._letters.append(letter)

    def guessed(self, letter):
        self._guessed.append(letter)

    def display(self):
        for letter in self._letters:
            for item in self._guessed:
                if item == letter:
                    print(item + " ")
                else:
                     print("_ ")
        print("\n")

    def compare(self, guess):
            for letter in self._letters:
              if letter == guess:
                self._right = self._right + 1
                return True
              else:
                return False
    
    def ending(self):
        cache = []
        for letters in self._letters:
            for items in cache:
                if items != letters:
                    cache.append(letters)

        length = len(cache)
        if self._right == length:
            print("You win!!!")
            return False
        else:
             return True


