import random


# 동물 리스트 혹은 디

# 빈칸 or 동물 객체
Grid_size = 10
Grid = [[0] * Grid_size for i in range(Grid_size)]

# 동물 종 마다 list가 필요하다고 생각하는데
Lion_list = []
Food_list = []
Impala_list = []

Animal = {"Lion" : Lion_list, "Food" : Food_list, "Impala" : Impala_list}

Site_list_random = [ [0]  for i in range(0, 5)]
Site_list_ordered = [ [0]  for i in range(0, 5)]

def make_Site_list_random(k):
    for i in range(-k, k+1):
        for j in range(-k, k+1):
            tmp = [i, j]
            if i**2 + j**2 >= k**2 :
                Site_list_random[k].append(tmp)
    Site_list_random[k].remove(0)

def make_Site_list_ordered(k):
    for i in range(0, k+1):
        for j in range(0, k+1):
            tmp = [i, j]
            if(i**2 + j**2 >= k**2):
                Site_list_ordered[k].append(tmp)
    Site_list_ordered[k].remove(0)

for i in range(1, 5):
    make_Site_list_random(i)
    make_Site_list_ordered(i)

class Animals:

    x = 0  # 동물의 X좌표
    y = 0  # 동물의 Y좌표
    energy_left = 0  # 동물의 남은 에너지(칼로리)
    time_left = 0  # 동물의 남은 수명 (단위: tick)
    calorie = 0  # 동물이 먹혔을 때 포식자가 얻는 칼로리
    site = 0  # 동물의 시야 범위
    birth_rate = 0  # 동물의 번식율 (%)
    hunting_rate = 0  # 동물의 사냥 성공 확률 (%)
    predator = ["Lion"]  # class의 객체의 포식자 name 담고 있을 list
    food = []  # class의 먹이 name를 담고 있을 list
    calorie_waste_rate = 0  # 동물의 tick 당 칼로리 소모량
    max_life = 0
    min_life = 0

    max_calorie = 0
    threshold_birth = 0
    flag_newborn = False

    name = "Animals"

    def __init__(self, x, y, energy_left):
        self.time_left = random.randint(self.min_life, self.max_life)
        self.energy_left = energy_left
        self.x = x
        self.y = y

    def move(self, x, y):  # 동물의 이동 함수 (사실상 뭐 인자로 업데이트만 하는거)

        #이 부분은 이동후 공통 -> 원래 좌표 지우고, 새좌표로 이동하고, 이동 칼로리 감소
        Grid[self.x][self.y] = 0
        self.x = self.x + x
        self.y = self.y + y
        Grid[self.x][self.y] = self
        self.energy_left -= self.calorie_waste_rate #이동하느라 에너지 소모
        self.time_left -= 1 # 수명 깍임

        if self.time_left <= 0 or self.energy_left <= 0: #  수명 다 살았다면
            #여기서 죽는거 구현, 애니멀 리스트에서 빼주고, 좌표 0으로 바꿔주기git add
            Grid[self.x][self.y] = 0
            Animal[self.name].remove(self)
            return
        if self.x < 0:
            self.x += Grid_size
        if self.y < 0:
            self.y += Grid_size

    def eat_food(self, x, y):
        # (x, y)의 있는 먹이를 먹어서 본인의 칼로리를 올리고, 해당 Grid의 원소를 0으로 바꾼다.
        self.energy_left += Grid[x][y].calorie
        Grid[x][y] = 0
        # 해당 리스트 역시 순회해서

    def check_site(self):  # 틱에서 결국 실행되는 함수
        # 포식자 검색 & 먹이 검색
        # temp 로 표시 된 것 string으로 바꼈으니까 . grid[][]로 바꿔야함

        # 포식자 검색도 일단 가까이부터 하도록 변경
        for i in range(1, self.site + 1):
            k = random.randint(0, len(Site_list_random[i]) - 1)
            for j in range(0, len(Site_list_random[i])):
                next_x = self.x + Site_list_random[i][k - j][0]
                next_y = self.y + Site_list_random[i][k - j][1]
                if (next_x >= Grid_size):
                    next_x -= Grid_size
                if (next_y >= Grid_size):
                    next_y -= Grid_size

                if Grid[next_x][next_y] != 0:
                    for temp in self.predator:  # 포식자 검색
                        if Grid[next_x][next_y] != 0 and Grid[next_x][next_y].name == temp:
                            if Grid[next_x][next_y].hunting_rate > random.random():  # 포식자 감지 성공
                                # next_x, y가 포식자의 위치
                                # self.move(self.x - next_x, self.y - next_y, 2)
                                # 검사할 사분면의 결정
                                if (self.x - next_x < 0):
                                    x_sign = -1
                                else:
                                    x_sign = 1
                                if (self.y - next_y < 0):  #
                                    y_sign = -1
                                else:
                                    y_sign = 1

                                for a in range(1, int(self.site/2) + 1):
                                    t = random.randint(0, len(Site_list_ordered[a]) - 1)
                                    for b in range(0, len(Site_list_ordered[a])):
                                        # 비어있음을 검사
                                        temp_x = self.x + x_sign * Site_list_ordered[a][t - b][0]
                                        temp_y = self.y + y_sign * Site_list_ordered[a][t - b][1]
                                        if(temp_x >= Grid_size or temp_y >= Grid_size):
                                            temp_x = temp_x % Grid_size
                                            temp_y = temp_y % Grid_size
                                        if (Grid[temp_x][temp_y] == 0):
                                            self.move(temp_x - self.x, temp_y - self.y)
                                            return
                                # 포식자 검사에는 성공했지만, 도망가는 방향에 빈자리가 하나도 없어서 제자리에 정지
                                self.move(0, 0)
                                return

        for i in range(1, self.site + 1):
            k = random.randint(0, len(Site_list_random[i]) - 1)
            for j in range(0, len(Site_list_random[i])):
                next_x = self.x + Site_list_random[i][k - j][0]
                next_y = self.y + Site_list_random[i][k - j][1]
                if (next_x >= Grid_size):
                    next_x -= Grid_size
                if (next_y >= Grid_size):
                    next_y -= Grid_size

                    min_distance = self.site + 1  # 먹이 탐색 최소 거리의 초기값 설정
                    min_dirx = 0
                    min_diry = 0
                    for temp in self.food:  # 먹이 list 순회
                        if Grid[next_x][next_y] != 0 and Grid[next_x][next_y].name == temp:  # 해당 칸에 먹이 존재시
                            if max(abs(i), abs(j)) < min_distance:  # 최소 거리 먹이 검사
                                min_distance = max(abs(i), abs(j))
                                min_dirx = next_x
                                min_diry = next_y
                    if min_distance != self.site + 1:  # 발견한 경우, eat하고 move한다
                        self.eat_food(next_x, next_y)
                        self.move(min_dirx - self.x, min_diry - self.y)
                        return

        # 포식자도 없고, 먹이 못 찾았을 경우
        for i in range(1, self.site + 1):
            k = random.randint(0, len(Site_list_random[i]) - 1)
            for j in range(0, len(Site_list_random[i])):
                next_x = self.x + Site_list_random[i][k - j][0]
                next_y = self.y + Site_list_random[i][k - j][1]
                if (next_x >= Grid_size):
                    next_x -= Grid_size
                if (next_y >= Grid_size):
                    next_y -= Grid_size
                if (Grid[next_x][next_y] == 0):
                    self.move(next_x - self.x, next_y - self.y)
                    return

        # 만약 이동하려햇는데 주변이 다 차있는 경우에는 제자리 이동
        self.move(0, 0)

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
                    a = Animals(child_x, child_y, self.energy_left / 2)
                    self.energy_left /= 2
                    return

class Lion(Animals):

    max_life = 100
    min_life = 50
    site = 4
    birth_rate = 0
    hunting_rate = 0.7
    predator = []
    food = ["Impala", "Rhino"]
    calorie_waste_rate = 10
    max_calorie = 200
    threshold_birth = 0.7

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
        #if self.energy_left >= self.max_calorie * self.threshold_birth :
            #if 1 - self.birth_rate < random.random():
            #    self.make_child()

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
                    a = Lion(child_x, child_y, self.energy_left / 2)
                    Animal[self.name].append(a)
                    self.energy_left /= 2
                    return

    def use_turn(self): # 결국 매 틱 실행되는 함수
        self.check_site()
        #if self.energy_left >= self.max_calorie * self.threshold_birth :
            #if 1 - self.birth_rate < random.random():
            #    self.make_child()


def Lion_Gen(num):
    Grid_tmp = []
    for i in range(0, Grid_size):
        for j in range(0, Grid_size):
            tmp = [i, j]
            Grid_tmp.append(tmp)

    for i in range(0, num):
        rand = random.randint(0, len(Grid_tmp) - 1)
        x = Grid_tmp[rand][0]
        y = Grid_tmp[rand][1]
        a = Lion(x, y, 200)
        Lion_list.append(a)
        Grid[x][y] = a
        del Grid_tmp[rand]

def Impala_Gen(num):
    Grid_tmp = []
    for i in range(0, Grid_size):
        for j in range(0, Grid_size):
            tmp = [i, j]
            Grid_tmp.append(tmp)

    for i in range(0, num):
        rand = random.randint(0, len(Grid_tmp) - 1)
        x = Grid_tmp[rand][0]
        y = Grid_tmp[rand][1]
        a = Impala(x, y, 200)
        Impala_list.append(a)
        Grid[x][y] = a
        del Grid_tmp[rand]

cnt = 0
def print_Grid(cnt):
    print("Printing Grid ", cnt)
    for i in range(0, Grid_size):
        for j in range(0, Grid_size):
            if(Grid[i][j] == 0) :
                print(0, end=' ')
            elif Grid[i][j].name == "Lion":
                print(1, end=' ')
            elif Grid[i][j].name == "Impala":
                print(2, end=' ')
        print()
    print()

Lion_Gen(20)
Impala_Gen(20)

while(len(Lion_list) > 0 or len(Impala_list) > 0):
    print_Grid(cnt)
    cnt+=1
    # Problem is removing lion during the iteration
    tmp = len(Lion_list)
    i = 0
    while i < len(Lion_list):
        Lion_list[i].use_turn()
        i+=1
        if tmp != len(Lion_list):
            tmp = len(Lion_list)
            i -= 1
        if (tmp == 0):
            break

    tmp = len(Impala_list)
    i = 0
    while i < len(Impala_list):
        Impala_list[i].use_turn()
        i += 1
        if tmp != len(Impala_list):
            tmp = len(Impala_list)
            i -= 1
        if (tmp == 0):
            break