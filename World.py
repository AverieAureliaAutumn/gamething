from Location import Location
from Npc import Npc

class World:
    
    #All locations ------------------------------------------------
    Campfire = Location("Campfire","You wake up near a campfire, in a unfamiliar place.")
    Town = Location("Town","You find yourself near an entrance to the town. It is a dirt path that takes you straight to the inn")
    Forest = Location("Forest","You explore the forest and find yourself in a strange place.\n The sounds of birds disappears, as everything around you seems to fade in mist.\n Magical blue mushrooms light the way, as you gently follow a trail lit; you make your way to a local inn.")
    Inn = Location("Inn","You arrive at the Inn. A fireplace is burning, and the atmosphere is jolly")
    ForestInn = Location("Forest Inn","Secluded in the forest, you enter the Inn.")
    Elune = Location("Elune","You arrive at a place indescribable.This is the realm of the gods")
    
    currentLocation = Campfire
    
    story_step = 0
    story = {
        "Introduction": " Dreams are a funny thing isn't it? a world full of wonders and weirdness, but this was nothing like this, this time, it was a Nightmaire...",
        "Chapter 1": " You finally know a bit more about this place you find yourself in, full of monsters and magic. The old wizard told you about the gem of shadows, will you be able to get it ?"
    }
    
    #The prefix @classmethod make the Method Static, and can be called without an instance of said Class, here exemple you can simply say: World.read_story()
    @classmethod
    def read_story(self):
        match self.story_step:
            case 0:
                print(self.story["Introduction"])
            case 1:
                print(self.story["Chapter 1"])
            case _:
                print("HOW THE FUCK DID YOU GET HERE")
    
    @classmethod
    def load(self):
        self.gen_npcs(self)
        self.gen_connections(self)
    
    def gen_npcs(self):
        self.Town.set_npc(Npc())
        self.Forest.set_npc(Npc())
        self.Inn.set_npc(Npc())
        self.ForestInn.set_npc(Npc())
    
    def gen_connections(self):
        self.Campfire.connect(self.Town)
        self.Campfire.connect(self.Forest)
        self.Town.connect(self.Inn)
        self.Forest.connect(self.ForestInn)
        self.Elune.connect(self.Forest)
    
    @classmethod
    def travel(self, destination):
        for location in self.currentLocation.connections:
            if destination == location.name:
                self.currentLocation = location
                return True
        
        #if it's not on the list
        return False