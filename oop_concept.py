"Creating Class A"
class A():

    """
    Create an instance variables
    """
    def __init__(self, product, length, width):
        self.product = product
        self.length  = length
        self.width   = width

    "Return the production properties"
    def get_size(self):
        return self.product, self.length, self.width

"Create a Class B"
class B():

    def __init__(self, person, skill):
        self.person = person
        self.skill = skill

    def get_skill(self):
        return self.person, self.skill

a1 = A("Mobile", 5.5, 2.5)
print(a1.get_size())
b1 = B("Tommy", "Android Developer")
print(b1.get_skill())


