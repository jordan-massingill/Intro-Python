# Implement a class to hold room information. This should have name and
# description attributes.
from item import Light

class Room:
    def __init__(self, name, description, lit, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
        self.lit = lit

    def hasLight(self):
        if self.lit == True:
            print('You have natural light')
            return True
        else:
            for object in self.items:
                if isinstance(object, Light):
                    print('You have a light')
                    return True
                    break
                else: continue
            return False


    def __str__(self):
        if len(self.items) > 0:
            return "\n{name}\n\n {description}\n\nItems in room: {items}\n\n".format(name = self.name, description=self.description, items = ', '.join([item.description for item in self.items]))
        else:
            return "\n{name}\n\n {description}\n\nYou see no items in this room.\n\n".format(name = self.name, description=self.description)


    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def getItemFromRoom(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            return None

    def dropItemInRoom(self, item):
        if len(self.items) != 0:
            if item in self.items:
                return None
            else:
                self.items.append(item)
                return item
        else:
            self.items.append(item)
            return item
