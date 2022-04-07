class Player:
    
    def __init__(self):
        self.name = ""
        self.health = 0
        self.inventory = {}
        self.alive = True
    
    #A simple Get Set
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
    def starter_pack(self):
        self.health = 50
        self.inventory = {
            "gold": 100,
            "weapon": "Sword",
            "potion": 5
        }
    
    def look_inventory(self):
        print(
        " You have:" + 
        " Gold:" + str(self.inventory["gold"]) +
        " Weapon:" + self.inventory["weapon"] +
        " Potion:" + str(self.inventory["potion"])
        )
    
    # def attack(self,enemy):
        # hit = random.randrange(10)
        # enemy.health -= hit

        # print(": You attack for: "+ hit)
        
