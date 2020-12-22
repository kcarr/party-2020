# Extend the entity class
from entities.entity import Entity


# Define the Toilet Paper object by extending entity
class ToiletPaper(Entity):
    def __init__(self):
        Entity.__init__(self, "images/toilet_paper.png", (75, 75))

    def update(self):
        Entity.update(self)