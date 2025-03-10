class Pirate:
    def __init__(self, name: str, occupation: str, bounty: int):
        self.name = name
        self.occupation = occupation
        self.bounty = bounty
        self.is_captured = False
    
    def update_bounty(self, amount):
        self.bounty = amount

    def capture(self):
        self.is_captured = True
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name