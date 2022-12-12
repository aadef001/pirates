from game.events import Gate_key_code
from game.player import Player
import game.config as config
import time
class GateCode:
    def __init__(self):
        self.game1 = Gate_key_code.GuessingGame()
        self.game1_finished = False
        self.game2 = Gate_key_code.GuessingGame()
        self.game2_finished = False

    def getRules(self):
        return "Enter the two number key to get out of the room. You have 5 guesses, after that if you guess wrong, you die!"
    def allGamesDone(self):
        return self.game1_finished and self.game2_finished
    def printGuessFeedback(self, guess):
        if self.game1_finished == False:
            if self.game1.checkGuess(guess) == 0:
                print("You have found the first number")
                self.game1_finished = True
            if self.game1.checkGuess(guess) == 1:
                print("Your guess is too high")
            elif self.game1.checkGuess(guess) == -1:
                print("Your guess is too low")
        if self.game2_finished == False:
            if self.game2.checkGuess(guess) == 0:
                print("You have found the second number")
                self.game2_finished = True
            if self.game2.checkGuess(guess) == 1:
                print("Your guess is too high")
            elif self.game2.checkGuess(guess) == -1:
                print("Your guess is too low")
                
    def process (self, world):
        x = self.getRules()
        print(x)
        tries = 0
        while tries<6 and self.allGamesDone() == False:
            guess = int(input("Enter your 1st number: "))
            self.printGuessFeedback(guess)
            tries = tries + 1
            if tries == 6:
                config.the_player.gameInProgress = False
                config.the_player.kill_all_pirates("Drowned in the whirlpool")
        result = {}
        result["message"] = "you are out of the room!"
        result["newevents"] = [ ]
        return result

            
