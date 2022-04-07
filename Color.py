#A class to store colors and text formating
class Color:
    
    #Without the Self attribute, and outside of the constructor
    #Theses are Static variables, they are the same for all objects
    #And if changed, all object will have the value changed
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    #No constructor for a Static class
    #It avoids the class to be instantied as an Object, and stay
    #Purely as a static Class
    
    @classmethod
    def bold(self, text):
        return self.BOLD + text + self.END