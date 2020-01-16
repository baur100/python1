from lesson14.pc import Pc
from lesson14.tree import Tree
from lesson14.cat import Cat
from lesson14.dog import Dog


pc = Pc(16,'i7',1000,'samsung')
print(f"{pc.memory}, {pc.cpu}, {pc.monitor}, {pc.ssd}")

maple = Tree(20,"maple",50)
maple.print_tree()

fir_tree = Tree(10, "fir", 5)
fir_tree.isPine=True

barsik = Cat("Barsik",3)
print(barsik)

# dunder __method_name__
# private _private_method_or_field
# mangling __field_name

doggy = Dog("sharik",50)

