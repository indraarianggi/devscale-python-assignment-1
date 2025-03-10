from lib.pirate import Pirate

class PirateGroup:
    def __init__(self, name: str, ship: str):
        self.name = name
        self.ship = ship
        self.crew = []
    
    def add_crew(self, crew: Pirate):
        self.crew.append(crew)
    
    def remove_crew(self, crew: Pirate):
        self.crew.remove(crew)
    
    def get_crew_list(self):
        return self.crew
