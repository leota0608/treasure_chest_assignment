import random
import os
import msvcrt
import time
from tabulate import tabulate
class Tree:
    def __init__(self, name, description):
        #attributes
        self.name = name
        self.description = description
        self.chest = False
        
    def __str__(self):
        return self.name.upper()
    
    def get_description(self):
        return self.description
    
    def place_chest(self):
        self.chest = True


class Player:
    def __init__(self, name, game_map, location):
        self.name = name
        self.game_map = game_map
        self.location = location

    def __str__(self):
        return f"Player is at position [{self.x}, {self.y}]"
        
    def move(self, c, game_map):
        if c == 'w' and self.location[0] > 0:
            self.location[0] -= 1
            self.game_map.print_map(player)
        elif c == 's' and self.location[0] < self.game_map.dimension[0]:
            self.location[0] += 1
            self.game_map.print_map(player)
        elif c == 'a' and self.location[1] > 0:
            self.location[1] -= 1
            self.game_map.print_map(player)
        elif c == 'd' and self.location[1] < self.game_map.dimension[1]:
            self.location[1] += 1
            self.game_map.print_map(player)  
        else:
            self.game_map.print_map(player) 
        for tree in forest:
            if game_map.game_map[self.location[0]][self.location[1]] == tree.name[0].title():
                print(tree)
            
            
class Map:
    def __init__(self):
        self.initialize()
        self.dimension = [len(self.game_map[0])-1, len(self.game_map[0])-1]#(0 ~ n-1)
    
    def initialize(self):
        self.game_map = []
        available_spots = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append("Tree")
                available_spots.append([i, j])
            self.game_map.append(row)
        available_spots.pop(0)
        available_spots.pop(-1)

        for i in range(len(forest)):
            a = random.randint(0, len(available_spots)-1)
            self.game_map[available_spots[a][0]][available_spots[a][1]] = forest[i]
            forest[i].location = [available_spots[a][0], available_spots[a][1]]
            available_spots.pop(a)

    def update(self):
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                self.game_map[i][j] = "Tree"
                for tree in forest:
                    if [i, j] == tree.location:
                        self.game_map[i][j] = tree

                

    def print_map(self, player):
        self.update()
        self.game_map[player.location[0]][player.location[1]] = '#'
        
        print(tabulate(self.game_map, tablefmt = "grid"))
        print("#: player\n**Use wasd to move your charactor**")
        
        for tree in forest:
            if [player.location[0], player.location[1]] == tree.location:
                print(f"Description: This is a {tree}. {tree.get_description()}")
    
    def get_dimentions(self):
        pass
    

oak = Tree("oak", "Nothing here...")
pine = Tree("pine", "Nothing here...")
maple = Tree("maple", "Nothing here...")
birch = Tree("birch", "Nothing here...")
willow = Tree("willow", "Nothing here...")

forest = [oak, pine, maple, birch, willow]

game_map = Map()

player = Player("111", game_map, [0, 0])
game_map.print_map(player)

while True:
    c = input()
    player.move(c, game_map)1

# python main.py