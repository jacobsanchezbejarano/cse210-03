from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.guesser import Guesser


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _jumper (Jumper): The game's jumper.
        _is_playing (boolean): Whether or not to keep playing.
        _guesser (Guesser): The game's guesser.
        _terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Updates the player's selections and controls player's live.

        Args:
            self (Director): An instance of Director.
        """
        if self._is_playing:
            if self._jumper.get_secret_word() == []:
                pass
            else:
                letter_intent = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
                self._guesser.set_player_letter(letter_intent)
                lives = self._jumper.set_lives(letter_intent)
                if lives == 0:
                    self._is_playing = False
                self._jumper.set_showed_word()
            
        
    def _do_updates(self):
        """Updates information to show in the screen, and assigns a word to be guest.

        Args:
            self (Director): An instance of Director.
        """
        if self._is_playing:
            if self._jumper.get_secret_word() == []:
                self._jumper.assign_word()
            else:
                self._jumper.update_guesser_letters(self._guesser.get_player_letters())
                self._jumper.set_showed_word()
        
    def _do_outputs(self):
        """Shows the player's selections and the jumper's drawing.

        Args:
            self (Director): An instance of Director.
        """
        if self._is_playing:
           
            
            print(" ".join(self._jumper.get_showed_word()))
            self._jumper.parachute_status()

            if self._jumper.get_showed_word().count("_") == 0:
                print("You Win!")
                self._is_playing = False

        else:
            print(" ".join(self._jumper.get_showed_word()))
            self._jumper.parachute_status()
            print("Game Over!")
            
        
            
            