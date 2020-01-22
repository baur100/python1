from homeworks.hw17.fungi import Fungi
from homeworks.hw17.bacteria import Bacteria
from homeworks.hw17.plants import Plants
from homeworks.hw17.animals import Animals
from homeworks.hw17.invertebrates import Invertebrates
from homeworks.hw17.vertebrate import Vertebrates
from homeworks.hw17.fish import Fish
from homeworks.hw17.amphibians import Amphibians
from homeworks.hw17.birds import Birds
from homeworks.hw17.mammals import Mammals
from homeworks.hw17.carnivores import Carnivores
from homeworks.hw17.primates import Primates
from homeworks.hw17.seals import Seals
from homeworks.hw17.rodens import Rodens
from homeworks.hw17.whales import Whales
from homeworks.hw17.herbivores import Herbivores
from homeworks.hw17.lion import Lion
from homeworks.hw17.blue_whale import Blue_whale
from homeworks.hw17.wolf import Wolf

yeast = Fungi("Yeasts")
bacteria = Bacteria("E.Coli")
maple = Plants("red_maple")
snake = Animals("Python")
turtle = Invertebrates("Turtle")
lizard = Vertebrates("Lizard")
zebra = Mammals("Zebra")
glow = Fish("Glofish")
salam = Amphibians("Salamander")
peng = Birds("Penguin")
tigah = Carnivores, Mammals, Animals("Tiger")
slow = Primates, Vertebrates, Animals, ("Slow loris")
earless = Seals, Vertebrates, Animals("Earless seal")
ham = Rodens, Mammals, Vertebrates, Animals("Hamster")
k_whale = Whales, Mammals, Vertebrates, Animals("Killer whale")
capybara = Herbivores, Mammals, Vertebrates, Animals("Capybara")
congo = Lion, Carnivores, Mammals,Animals("Congo Lion")
balaenoptera_musculus = Blue_whale, Mammals,Vertebrates,Animals("Balaenoptera musculus")
wolf = Wolf, Carnivores,Mammals,Vertebrates,Animals("Arctic wolf")

