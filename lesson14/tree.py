class Tree:
    isPine=False
    def __init__(self,age, spice, height):
        self.a=age
        self.b=spice
        self.c=height

    def print_tree(self):
        print(f'{self.a}, {self.b}, {self.c}')
