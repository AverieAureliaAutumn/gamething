from Npc import Npc

class Location:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = []
    
    def set_npc(self,npc):
        self.npc = npc

    def connect(self, connection):
        self.connections.append(connection)
        connection.connections.append(self)

    def look_around(self):
        print(" " + self.description)
        
        if self.has_npc():
            if self.npc.health > 0:
                print(" Here you find " + self.npc.description())
    
    def has_npc(self):
        if 'self.npc' in locals():
            return True
        else:
            return False
    