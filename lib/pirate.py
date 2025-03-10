class Pirate:
    def __init__(self, name, occupation, bounty, wanted_poster):
        self.name = name
        self.occupation = occupation
        self.bounty = bounty
        self.wanted_poster = wanted_poster
    
    def update_bounty(self, amount):
        self.bounty = amount
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name