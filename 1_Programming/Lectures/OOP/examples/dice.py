import random
class Dice(object):
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
        self.value = random.randint(1,num_sides)

    def __repr__(self):
        ''' tells python how to represent the object '''
        return "{0} sided die showing {1}".format(self.num_sides, self.value)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    @property
    def sides(self):
        print(num_sides)

    @property
    def face(self):
        print(value)

    def roll(self):
        self.value = random.randint(1,self.num_sides)
