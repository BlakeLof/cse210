from game.terminal_service import TerminalService
from game.word import Word
from game.player import Player


class Director:

    def __init__(self):
        self._word = Word()
        self._terminal_service = TerminalService()
        self._is_playing = True
        self._player= Player()
        self.guess =" "
    
    def start_game(self):
        the_word = self._word.get_word
        self._word.split(the_word)
        self._word.display() 
        self._player.parachute()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):

       self._word.display() 
       self._player.parachute()
      
       self.guess = self._terminal_service.read_text("Guess a letter [a-z]: ")
       self.guess.lower()
       self._word.guessed(self.guess)

    
    def _do_updates(self):
       check = self._word.compare(self.guess)
       if check == False:
            self._player.bad_attempt()
        
    
    def _do_outputs(self):
        self._word.display()
        self._player.parachute()
        self._is_playing = self._player.ending()
        self._is_playing = self._word.ending()
    
     


    
        

        