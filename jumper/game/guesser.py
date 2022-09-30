# TODO: Implement the Guesser class as follows...

# 1) Add the class declaration. Use the following class comment.


class Guesser():

    """The person looking for the Guesser. 
        
        The responsibility of a Guesser is to keep track of its location and distance travelled.
        
        Attributes:
            _player_letters (list): The letters entered by the player.
        """  

# 2) Create the class constructor. Use the following method comment.
    """Constructs a new Guesser.

            Args:
                self (Guesser): An instance of Guesser.
    """

    def __init__(self):
    
        self._player_letters = []
       
# 3) Create the get_player_letters(self) method. Use the following method comment.
        """Allows to access to _player_letters information.

            Args:
                self (Guesser): An instance of Guesser.
        """
    def get_player_letters(self):
        return self._player_letters

# 4) Create the set_player_letters(self) method. Use the following method comment.
    """Appends the letter selected to the _player_letters list.

            Args:
                self (Guesser): An instance of Guesser.
                player_letter (int): The letter entered by the player.
        """
    def set_player_letter(self, player_letter):
        self._player_letters.append(player_letter)