import random

class Jumper:
    """The Jumper. 
    
    The responsibility of Jumper is to keep track of the secret information to compare with player's inputs. 
    
    Attributes:
        _secret_word (list): The random word.
        _showed_word (list): The shown information.
        _guesser_letters (list): Letters selected by the player.
        _lives (int): Lives of the player, it starts with a value of four.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """

              
        self._secret_word = []
        self._showed_word = []
        self._guesser_letters = []
        self._lives = 4

        


    def assign_word(self):
        """If there is not a secret word selected, this method will create one.

        Args:
            self (Jumper): An instance of Jumper.
            
        
        """
        list_of_words = ["h o u s e","h o r s e","m o u s e","o r a n g e"]

        if self._secret_word == []:

            word = list_of_words[random.randint(0,3)]
            self._secret_word = word.split(" ")
            
            for i in self._secret_word:
                self._showed_word.append("_")

        else:
            pass
            


    def update_guesser_letters(self, guesser_letters):
        """Updates the player's letters selected.

        Args:
            self (Jumper): An instance of Jumper.
        
        
        """
        self._guesser_letters = guesser_letters


    def parachute_status(self):
        """This method draws the parachute according to the player's lives.

        Args:
            self (Jumper): An instance of Jumper.
        """
        print()
        if self._lives > 3:
            print("  ___ ")
        if self._lives > 2:
            print(" /___\\")
        if self._lives > 1:
            print(" \\   /")
        if self._lives > 0:
            print("  \\ /")
            print("   O")
            print("  /|\\")
            print("  / \\")
            print("^^^^^^^")
        if self._lives == 0:
            print("   x")
            print("  /|\\")
            print("  / \\")
            print("^^^^^^^")
            
        


    def get_secret_word(self):
        """This method allows Director class to access the secret word.

        Args:
            self (Jumper): An instance of Jumper.
        """
        return self._secret_word
    
    def get_showed_word(self):
        """This method allows Director class to access the printing word.

        Args:
            self (Jumper): An instance of Jumper.
        """
        return self._showed_word

    def set_showed_word(self):
        """This method updates the printing word.

        Args:
            self (Jumper): An instance of Jumper.
        """
        showed_word = self._showed_word
        x = 0
        for i in self._secret_word:
            for j in self._guesser_letters:
                if i == j:
                    showed_word[x] = i
                else:
                    pass
            
            x += 1
        self._showed_word = showed_word
    
    def set_lives(self,letter_intent):
        """This method controls the player's live.

        Args:
            self (Jumper): An instance of Jumper.
        """

        if letter_intent not in self._secret_word:
            self._lives -= 1
        
        return self._lives