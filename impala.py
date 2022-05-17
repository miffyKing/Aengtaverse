import random
from animal import Animals, Grid_size, Grid, Animal, Site_list_random, Impala_list
from lion import Lion

class Impala(Animals):

    max_life = 100
    min_life = 50
    site = 4
    birth_rate = 0.3
    hunting_rate = 1
    predator = ["Lion"]
    food = ["Grass"]
    calorie = 500
    calorie_waste_rate = 5
    max_calorie = 400
    threshold_birth = 0.7

    name = "Impala"

    def __init__(self, x, y, energy_left):
        self.time_left = random.randint(self.min_life, self.max_life)
        self.energy_left = energy_left
        self.x = x
        self.y = y

    def make_child(self):
        # 일정 칼로리이상이면 번식한다.
        # 움직이고나서 실행된다
        for i in range(1, self.site + 1):
            k = random.randint(0, len(Site_list_random[i]) - 1)
            for j in range(0, len(Site_list_random[i])):
                child_x = self.x + Site_list_random[i][k - j][0]
                child_y = self.y + Site_list_random[i][k - j][1]
                if (child_x >= Grid_size):
                    child_x -= Grid_size
                if (child_y >= Grid_size):
                    child_y -= Grid_size
                if (Grid[child_x][child_y] == 0):
                    a = Impala(child_x, child_y, self.energy_left / 2)
                    Animal[self.name].append(a)
                    self.energy_left /= 2
                    return

    def use_turn(self): # 결국 매 틱 실행되는 함수
        self.check_site()
        #if self.energy_left >= self.max_calorie * self.threshold_birth :
            #if 1 - self.birth_rate < random.random():
            #    self.make_child()

def Impala_Gen(num):
    Grid_tmp = []
    for i in range(0, Grid_size):
        for j in range(0, Grid_size):
            tmp = [i, j]
            if Grid[i][j] == 0:
                Grid_tmp.append(tmp)

    for i in range(0, num):
        rand = random.randint(0, len(Grid_tmp) - 1)
        x = Grid_tmp[rand][0]
        y = Grid_tmp[rand][1]
        a = Impala(x, y, 200)
        Impala_list.append(a)
        Grid[x][y] = a
        del Grid_tmp[rand]