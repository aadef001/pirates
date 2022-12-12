from game import event
import random
from game.combat import Combat
from game.combat import Zombie
from game.display import announce
import game.config as config

class Zombies (event.Event):

    def __init__ (self):
        self.name = " zombie attack"

    def process (self, world):
        result = {}
        result["message"] = "the zombies are defeated!"
        monsters = []
        n_appearing = random.randrange(2,5)
        n = 1
        while n <= n_appearing:
            monsters.append(Zombie("Brain-eating Zombies "+str(n)))
            n += 1
        announce ("The crew is attacked by zombies!")
        Combat(monsters).combat()
        if random.randrange(2) == 0:
            result["newevents"] = [ self ]
        else:
            result["newevents"] = [ ]
        config.the_player.ship.food += n_appearing*2
        
        return result
