class Fraction(object):
    ''' Makes a fraction object '''

    def __init__(self, num = 0, denom = 1):
        ''' runs when object instantiated '''
        self.num = num
        self.denom = denom

    def __repr__(self):
        ''' tells python how to represent the object '''
        return "{0}/{1}".format(self.num,self.denom)

    def add(self, other):
        ''' defines the add function '''
        if self.denom == other.denom:
            return Fraction(self.num + other.num, self.denom)
        else:
            self_num = self.num * other.denom
            other_num = other.num * self.denom
            self_denom = self.denom * other.denom
            other_denom = other.denom * self.denom
            while(self_num%2 == 0  and self_denom%2 == 0):
                self_num /= 2
                self_denom /= 2
            while(other_num%2 == 0  and other_denom%2 == 0):
                other_num /= 2
                other_denom /= 2
            return Fraction(self_num + other_num, self_denom)

    def __add__(self, other):
        ''' overload the + operator '''
        return self.add(other)

if __name__ == '__main__':
    f1 = Fraction(num = 2, denom = 3)
    f2 = Fraction(num = 1, denom = 5)
    f3 = f1 + f2
    print(f3)

    # What attributes will a Fraction object have?

    # Can I display a Fraction object?  Why or why not?

    # If I uncomment all the code, what methods will a Fraction object have?

    # What could be done to allow adding fractions with different denominators?
