import random


# 동물 리스트 혹은 디

# 빈칸 or 동물 객체
Grid_size = 100
Grid = [[0] * Grid_size for i in range(Grid_size)]


class Animals:

    def __init__(self):
        self.x = 0  # 동물의 X좌표
        self.y = 0  # 동물의 Y좌표
        self.energy_left = 0  # 동물의 남은 에너지(칼로리)
        self.time_left = 0  # 동물의 남은 수명 (단위: tick)
        self.calorie = 0  # 동물이 먹혔을 때 포식자가 얻는 칼로리
        self.site = 0  # 동물의 시야 범위
        self.birth_rate = 0  # 동물의 번식율 (%)
        self.hunting_rate = 0  # 동물의 사냥 성공 확률 (%)
        self.predator = []  # class의 객체의 포식자 class를 담고 있을 list
        self.food = []  # class의 먹이 class를 담고 있을 list
        self.calorie_waste_rate = 0  # 동물의 tick 당 칼로리 소모량

    def __del__(self):
        return

    def move(self, x, y):  # 동물의 이동 함수 (사실상 뭐 인자로 업데이트만 하는거)
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
                        if Grid[self.x + i][self.y + j] == temp:
                            if temp.hunting_rate > random.random():  # 사냥 실패
                                self.move(-i, -j)
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
                        self.move(self.x + min_dirx, self.y + min_diry)
                    else:  # 포식자도 감지 못 하고, 먹이 못 찾은 경우 random하게 이동
                        self.move(self.x + random.randint(-1, 1), self.y + random.randint(-1, 1))

class Lion (Animals):   #이렇게 상속하는게 맞노
    def __init__(self, x, y, energy_left, time_left, calorie, site, birth_rate, hunting_rate, predator, food, calorie_waste_rate):
        self.x = 0
        self.y = 0
        self.energy_left = 100
        self.time_left = 50
        self.calorie = 100
        self.size = 3
        self.birth_rate = 30
        self.hunting_rate = 70
        self.predator = [""]
        self.food = ["byounghwa", "hwanju"]
        self.calorie_waste_rate = 10






