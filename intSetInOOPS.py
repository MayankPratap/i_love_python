class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self,other):
        """Assume other is an intSet
           And Return a new intSet containing elements that appear in both sets.

        """
        commonSet=intSet()
        # Go through values in set

        for val in self.vals:
            # Check if each value is a member of other set

            if other.member(val):
                commonSet.insert(val)

        return commonSet

    def __len__(self):
        return len(self.vals)


a=intSet()
a.insert(4)
a.insert(5)
a.insert(4)
a.insert(8)

b=intSet()
b.insert(8)
b.insert(9)

print a.intersect(b)
