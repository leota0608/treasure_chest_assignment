import random
class Tree:
    def __init__(self, name, description):
        #attributes
        self.name = name
        self.description = description
        self.chest = False
        
    def __str__(self):
        return self.name.title()
    
    def place_chest(self):
        self.chest = True


class Player:
    def __init__(self, map, x, y):
        self.map = map
        self.x = x
        self.y = y
    def __str__(self):
        return f"Player is at position [{self.x}, {self.y}]"
    

oak = Tree("oak", "Nothing here...")
pine = Tree("pine", "Nothing here...")
maple = Tree("maple", "Nothing here...")
birch = Tree("birch", "Nothing here...")
willow = Tree("willow", "Nothing here...")

forest = [oak, pine, maple, birch, willow]

map = []
available_spots = []
for i in range(4):
    row = []
    for j in range(4):
        row.append(0)
        available_spots.append([i, j])
    map.append(row)
available_spots.pop(0)
available_spots.pop(-1)
player = Player(map, 0, 0)

for i in range(len(forest)):
    a = random.randint(0, len(available_spots)-1)
    map[available_spots[a][0]][available_spots[a][1]] = forest[i]
    available_spots.pop(a)

for i in range(4):
    for j in range(4):
        print(map[i][j], end=' ')
    print("\n", end='')