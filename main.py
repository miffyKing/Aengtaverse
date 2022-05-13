import random


# 동물 리스트 혹은 디

# 빈칸 or 동물 객체
Grid_size = 100
Grid = [[0] * Grid_size for i in range(Grid_size)]

# 동물 종 마다 list가 필요하다고 생각하는데
Lion_list = []
Food_list = []

Animal = {"Lion" : Lion_list, "Food" : Food_list}

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

    def move(self, x, y, move_flag):  # 동물의 이동 함수 (사실상 뭐 인자로 업데이트만 하는거)

        #이 부분은 이동후 공통 -> 원래 좌표 지우고, 새좌표로 이동하고, 이동 칼로리 감소
        Grid[self.x][self.y] = 0
        self.x = self.x + x
        self.y = self.y + y
        Grid[self.x][self.y] = self
        self.energy_left -= self.calorie_waste_rate #이동하느라 에너지 소모
        self.time_left -= 1 # 수명 깍임
        if self.time_left <= 0: #  수명 다 살았다면
            #여기서 죽는거 구현, 애니멀 리스트에서 빼주고, 좌표 0으로 바꿔주기git add 
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
                        if Grid[next_x][next_y].name == temp:
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

                                for a in range(1, self.site / 2 + 1):
                                    t = random.randint(0, len(Site_list_ordered) - 1)
                                    for b in range(0, len(Site_list_ordered[a])):
                                        # 비어있음을 검사
                                        temp_x = self.x + x_sign * Site_list_ordered[i][t - j][0]
                                        temp_y = self.y + y_sign * Site_list_ordered[i][t - j][1]
                                        if (Grid[temp_x][temp_y] == 0):
                                            self.move(temp_x - self.x, temp_y - self.y, 2)
                                            return
                                # 포식자 검사에는 성공했지만, 도망가는 방향에 빈자리가 하나도 없어서 제자리에 정지
                                self.move(0, 0, 4)
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
                        if Grid[next_x][next_y].name == temp:  # 해당 칸에 먹이 존재시
                            if max(abs(i), abs(j)) < min_distance:  # 최소 거리 먹이 검사
                                min_distance = max(abs(i), abs(j))
                                min_dirx = next_x
                                min_diry = next_y
                    if min_distance != self.site + 1:  # 발견한 경우, eat하고 move한다
                        self.eat_food(next_x, next_y)
                        self.move(self.x + min_dirx, self.y + min_diry, 3)
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
                    self.move(next_x - self.x, next_y - self.y, 4)
                    return

        # 만약 이동하려햇는데 주변이 다 차있는 경우에는 제자리 이동
        self.move(0, 0, 4)

    def make_child(self, Lists):
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
                    Lists.append(a)
                    self.energy_left /= 2


class Lion(Animals):

    max_life = 10
    min_life = 1
    site = 4
    birth_rate = 0.3
    hunting_rate = 0.5
    predator = []
    food = []
    calorie_waste_rate = 5
    max_calorie = 100
    threshold_birth = 0.7

    name = "Lions"


    def __init__(self, x, y, energy_left):
        self.time_left = random.randint(self.min_life, self.max_life)
        self.energy_left = energy_left
        self.x = x
        self.y = y

    def move(self, x, y, move_flag):  # 동물의 이동 함수 (사실상 뭐 인자로 업데이트만 하는거)
        # 최대 바운더리도 생각해야한다.
        # 내가 이동하려는 칸에 이미 동물이 존재하는 경우 생각
        # move에서 가려는 칸에 먹이가 있으면 사냥하는거까지 해야함
        Grid[self.x][self.y] = 0
        self.x = self.x + x
        self.y = self.y + y
        self.energy_left -= self.calorie_waste_rate


    def eat_food(self, x, y):  # (x, y)의 있는 먹이를 먹어서 본인의 칼로리를 올리고, 해당 Grid의 원소를 0으로 바꾼다.
        self.energy_left += Grid[x][y].calorie
        Grid[x][y] = 0

    def check_site(self):  # 틱에서 결국 실행되는 함수
        # 포식자 검색 & 먹이 검색
        for i in range(-1 * self.site, self.site):
            for j in range(-1 * self.site, self.site):
                if i == 0 and j == 0: continue
                if Grid[self.x + i][self.y + j] != 0:
                    for temp in self.predator:  # 포식자 검색
                        if Grid[self.x + i][self.y + j].name == temp:
                            if Grid[self.x + i][self.y + j].hunting_rate > random.random():  # 사냥 실패
                                self.move(-i, -j, 2)        #포식자 인식, 도망 flag 2
                                return

                    min_distance = self.site + 1  # 먹이 탐색 최소 거리의 초기값 설정
                    min_dirx = 0
                    min_diry = 0
                    for temp in self.food:  # 먹이 list 순회
                        if Grid[self.x + i][self.y + j] == temp:  # 해당 칸에 먹이 존재시
                            if max(abs(i), abs(j)) < min_distance:  # 최소 거리 먹이 검사
                                min_distance = max(abs(i), abs(j))
                                min_dirx = i;
                                min_diry = j
                    if min_distance != self.site + 1:  # 발견한 경우, eat하고 move한다
                        self.eat_food(self.x + min_dirx, self.y + min_diry)
                        self.move(self.x + min_dirx, self.y + min_diry, 3)      #먹이 추적, 3
                    else:  # 포식자도 감지 못 하고, 먹이 못 찾은 경우 random하게 이동
                        self.move(self.x + random.randint(-1, 1), self.y + random.randint(-1, 1), 4)   #그냥 랜덤, 4


    def make_child(self):
        # 일정 칼로리이상이면 번식한다.
        # 움직이고나서 실행된다

        # 새로 태어날 동물의 좌표 시야내에 랜덤하게 생성
        child_x = random.randint(-self.site, self.site)
        child_y = random.randint(-self.site, self.site)
        if child_x == 0 and child_y == 0:
            child_x = 1

        # 새로운 동물 생성
        # 충돌 검사 필요
        new_lion = Lion(self.x + child_x, self.y + child_y, self.energy_left / 2)
        new_lion.move(new_lion.x, new_lion.y, 1)       #새로 새끼 생성
        Lion_list.append(new_lion)
        new_lion.flag_newborn = True
        Grid[self.x + child_x][self.y + child_y] = new_lion
        self.energy_left /= 2

        # Problem 1 : 새로 태어난 동물은 턴을 실행하지 않는다.

    def use_turn(self): # 결국 매 틱 실행되는 함수
        if self.flag_newborn:
            return
        self.check_site()

        if self.energy_left >= self.max_calorie * self.threshold_birth :
            if self.birth_rate < random.random():
                self.make_child()



        # Problem 1 : 새로 태어난 동물은 턴을 실행하지 않는다.