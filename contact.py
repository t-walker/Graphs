from vertex import Vertex

class Contact(Vertex):
    def __init__(self, name="", number=""):
        self.name = name
        self.number = number

    def __repr__(self):
        return 'Name:%s Number: %s' % (repr(self.name), repr(self.number))
        
    __str__ = __repr__
