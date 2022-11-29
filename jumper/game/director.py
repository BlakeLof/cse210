from game.terminal_service import TerminalService
from game.word import Word
from game.player import Player


class Director:

    def __init__(self):
        self._word = Word()
        self._terminal_service = TerminalService()
        self._is_playing = True
        self._player= Player()
    
    def start_game(self):
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        user = self._terminal_service.read_text("Guess a letter [a-z]: ")
        self._player.guess(user)
    
    def _do_updates(self):
        self._word.compare(self._player)
    
    def _do_outputs(self):

    


    
        

        