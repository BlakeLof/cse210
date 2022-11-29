import random


class Word:

    def _init_(self):
        self.number = random.randint(1, 5)
        self._words = ["apple", "jefferson","brigham","programming","cartridge"]
        self._the_word = self._words[self.number]
    
    def new_word(self):
        self.number = random.randint(1,5)
        self._the_word = self._words[self.number]   
    
    def get_word(self):
        return self._the_word
    
    


