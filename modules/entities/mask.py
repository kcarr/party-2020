# Extend the entity class
from modules.entities.entity import Entity


# Define the Mask object by extending entity
class Mask(Entity):
    def __init__(self):
        Entity.__init__(self, "images/mask.png", (75, 75))
    
    def update(self):
        Entity.update(self)