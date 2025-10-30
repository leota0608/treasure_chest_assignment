import random
class Room:
    def __init__(self, coordinate, description):
        #attributes
        self.coordinate = coordinate
        self.description = description
        self.chest = False
        
    def __str__(self):
        return f"This room is at ({self.coordinate[0]}, {self.coordinate[1]})\n{self.description}"
    
    def place_chest(self):
        self.chest = True
 

house = []
for i in range(4):
    a = []
    for j in range(4):
        a.append(Room([i,j], "Nothing here..."))
    house.append(a)
house[0][0].description = "Starting position"
house[3][3].description = "Exit"
def setup():
    global house
    num_chest = 5
    available_spot = []
    for i in range(4):
        for j in range(4):
            if (i == 0 and j == 0) or (i == 3 and j == 3):
                continue
            available_spot.append([i, j])
    for i in range(num_chest):
        a = random.randint(0, len(available_spot)-1)
        house[available_spot[a][0]][available_spot[a][1]].place_chest()
        available_spot.pop(a)
def print_house():
    for i in range(4):
        for j in range(4):
            if (i == 0 and j == 0) or (i == 3 and j == 3):
                print('+', end=' ')
            elif house[i][j].chest:
                print(1, end=' ')
            elif not house[i][j].chest:
                print(0, end=' ')
        print("\n", end='')
