import random
from game.player import Player
import game.config as config
class Boss:
    def __init__(self):
        self.name = 'biruk'
    def getRules(self):
        return "You are in the fourth dungeon. You are stuck in a room with a demagog and to leave the room you must Call out its name, remember you have three chances or you all die: "
    def guessCorrect(self, guess):
        if guess == self.name:
            return True
        else:
            return False
    def process(self, world):
        print(self.getRules())
        tries = 0
        while tries < 3:
            guess = str(input("What's its name: "))
            belay = self.guessCorrect(guess)
            if belay == True:
                print("You have got it")
                break
            else:
                print("You have lost")
            tries = tries + 1
            if tries == 3:
                config.the_player.gameInProgress = False
                config.the_player.kill_all_pirates("Drowned in the whirlpool")
        result = {}
        result["message"] = "you are out of the room!"
        result["newevents"] = [ ]
        return result
