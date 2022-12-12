
from game import location
from game import config
from game.display import announce
from game.events import *
from game.items import Cutlass
from game.items import Flintlock
from game.events import Bossfight  
from game.events import Gate_key
from game.events import Army_of_dead
from game.items import AlkemSword

class Island (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "dungeon island"
        self.symbol = 'DI'
        self.visitable = True
        self.starting_location = Beach_with_ship(self)
        self.locations = {}
        self.locations["beach"] = self.starting_location
        #self.locations["trees"] = Trees(self)
        self.locations["dungeon1"] = Dungeon1(self)
        self.locations["dungeon2"] = Dungeon2(self)
        self.locations["dungeon3"] = Dungeon3(self)
        self.locations["dungeon4"] = Dungeon4(self)
        self.locations["dungeon5"] = Dungeon5(self)

    def enter (self, ship):
        print ("arrived at the dungeon island")

    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Beach_with_ship (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "beach"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        #self.event_chance = 50
        #self.events.append (seagull.Seagull())
        #self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce ("arrive at the beach. Your ship is at anchor in a small bay to the south.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["dungeon1"]


class Dungeon1 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "dungeon1"
        self.event_chance = 100
        self.events.append(Gate_key.GateCode())

    def enter (self):
        print ("Enter the code for the gate.")
        #Gate_key.GateCode().process(world)
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["dungeon2"]

class Dungeon2 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "dungeon2"
        self.event_chance = 100
        self.events.append(Army_of_dead.Zombies())

    def enter (self):
        print ("You are in the second dungeon and there are zombies.")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["dungeon3"]
            
class Dungeon3 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "dungeon3"

    def enter (self):
        print("You come into the room and a mysterious figure appears and warns you of the dangers in the next room\nHe says If you pursue this path, you will face the demon whose name I shall not say\n You defeat it if you call out its name\n Its name is written in code you need to decipher\n It is: 2 9 18 21 11")
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["dungeon4"]
class Dungeon4 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "dungeon4"
        self.event_chance = 100
        self.events.append(Bossfight.Boss())

    def enter (self):
        print('you have 3 chances')        
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["dungeon5"]
class Dungeon5 (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "dungeon5"
        self.verbs['take'] = self
        self.item_in_treasure = AlkemSword()

    def enter (self):
        #item = 'sword'
        
        print("you have reached your final destination. You have won the infamous sword of the dungeon island. Do you want to take it!")

    def process_verb (self, verb, cmd_list, nouns):
        item = self.item_in_treasure
        if (verb == 'take') and self.item_in_treasure != None:
            print("You pick up the "+item.name+": the strongest item in the dungeon island.")
            config.the_player.add_to_inventory([item])
            self.item_in_tree = None
        elif self.item_in_treasure == None:
            print('nothing is there to take')
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["beach"]

            
