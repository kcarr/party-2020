# Extend the entity class
from entities.entity import Entity


# Define the Virus object by extending entity
class Virus(Entity):
    def __init__(self):
        Entity.__init__(self, "images/covid.png", (25, 25))
    
    def update(self):
        Entity.update(self)