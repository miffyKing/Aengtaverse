import random
from animal import Animals, Grid_size, Grid, Animal, Site_list_random

class Lion(Animals):

    max_life = 300
    min_life = 200
    site = 6
    birth_rate = 0.2
    hunting_rate = 0.8
    predator = []
    food = ["Impala", "Rhino", "Baboon"]
    calorie_waste_rate = 10
    max_calorie = 2000

    name = "Lion"

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
                    a = Lion(child_x, child_y, self.energy_left / 2)
                    Animal[self.name].append(a)
                    self.energy_left /= 2
                    return

    def use_turn(self): # 결국 매 틱 실행되는 함수
        self.check_site()
        if self.energy_left >= self.max_calorie * self.threshold_birth :
            if 1 - self.birth_rate < random.random():
               self.make_child()