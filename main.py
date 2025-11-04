import random
import os
import msvcrt
import time
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
    def __init__(self, name, game_map, location):
        self.name = name
        self.game_map = game_map
        self.location = location

    def __str__(self):
        return f"Player is at position [{self.x}, {self.y}]"\
        
    def move(self, c):
        if c == 'w' and self.location[0] > 0:
            self.location[0] -= 1
            self.game_map.print_map(player)
        elif c == 's' and self.location[0] < self.game_map.dimension[0]:
            self.location[0] += 1
            self.game_map.print_map(player)
        elif c == 'a' and self.location[1] >0:
            self.location[1] -= 1
            self.game_map.print_map(player)
        elif c == 'd' and self.location[1] < self.game_map.dimension[1]:
            self.location[1] += 1
            self.game_map.print_map(player)  
        else:
            self.game_map.print_map(player)  
            
class Map:
    def __init__(self, _map):
        self.game_map = _map
        self.dimension = [len(_map)-1, len(_map[0])-1]#(0 ~ n-1)
        
    def print_map(self, player):
        os.system('cls')
        for i in range(self.dimension[0]+1):
            for j in range(self.dimension[1]+1):
                if i == player.location[0] and j == player.location[1]:
                    print("Y", end=' ')
                else:
                    print(self.game_map[i][j], end=' ')
            print("\n", end='')
        print("Y: playwe\nO: oak\nP: pine\nB: birch\nW: willow\n**Use wasd to move your charactor**")
    

oak = Tree("oak", "Nothing here...")
pine = Tree("pine", "Nothing here...")
maple = Tree("maple", "Nothing here...")
birch = Tree("birch", "Nothing here...")
willow = Tree("willow", "Nothing here...")

forest = [oak, pine, maple, birch, willow]

game_map = []
available_spots = []
for i in range(4):
    row = []
    for j in range(4):
        row.append(0)
        available_spots.append([i, j])
    game_map.append(row)
available_spots.pop(0)
available_spots.pop(-1)

for i in range(len(forest)):
    a = random.randint(0, len(available_spots)-1)
    game_map[available_spots[a][0]][available_spots[a][1]] = forest[i].name[0].upper()
    available_spots.pop(a)
    
game_map = Map(game_map)
player = Player("111", game_map, [0, 0])
game_map.print_map(player)
while True:
    c = msvcrt.getch().decode('utf-8').lower()
    player.move(c)

# python main.py