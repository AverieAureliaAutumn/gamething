import random

class Npc():
    def __init__(self):
        self.gen_info()
        self.gen_dialogue()

    def gen_info(self):
        nameArray = ["Bob", "Steve", "Gill", "Wizzo", "Arthur"]
        lastnameArray = ["The Weird", "The Wizard", "The Crazy", "The Evil", "The Loyal"]
        self.health = random.randrange(50)
        for x in range(5):
            #######################
            self.name = nameArray[random.randrange(0, len(nameArray), 1)]
            self.lastName = lastnameArray[random.randrange(0, len(lastnameArray), 1)]
    
    def description(self):
        return self.name + " " + self.lastName
    
    def gen_dialogue(self):
        option = [
            "I am busy here",
            "what do you want with me",
            "get away from me",
            "who do you think you are ?",
            "man, they let anyone get around nowadays"
        ]
        
        self.dialogue = option[random.randrange(len(option)-1)]
