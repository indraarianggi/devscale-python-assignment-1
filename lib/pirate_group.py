from lib.pirate import Pirate

class PirateGroup:
    def __init__(self, name, ship, jolly_roger):
        self.name = name
        self.ship = ship
        self.jolly_roger = jolly_roger
        self.crew = []
    
    def add_crew(self, crew: Pirate):
        self.crew.append(crew)

    def get_total_bounty(self):
        total = 0
        for member in self.crew:
            total += member.bounty
        
        return total
