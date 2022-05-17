import random
from lion import Lion
from impala import Impala
from baboon import Baboon
from animal import Grid, Grid_size, Animal_lists, Grid_Grass
from rhino import Rhino
from grass import Grass

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
            elif Grid[i][j].name == "Baboon":
                print(3, end=' ')
            elif Grid[i][j].name == "Rhino":
                print(4, end=' ')
        print()
    print()

Animal_class = [Lion, Impala, Baboon, Rhino, Grass]

def init_background():
    for i in range(0, Grid_size):
        for j in range(0, Grid_size):
            Grid[i][j] = 0
            Grid_Grass[i][j] = 0

    for i in Animal_lists:
        i.clear()

def gen_species(idx, num):
    # Animal_Class[idx]의 종을 num만큼 생성
    # 초기 생성 위치는 남은 자리 중에서 랜덤하게, 초기 에너지는 최대 에너지의 절반
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
        a = Animal_class[idx](x, y, int(Animal_class[idx].max_calorie/2))
        Animal_lists[idx].append(a)
        Grid[x][y] = a
        del Grid_tmp[rand]

def gen_animals(lists):
    # lists 내부의 숫자만큼 각 종을 생성
    for i in range(0, len(lists)):
        gen_species(i, lists[i])

def simulate(lists):

    init_background()
    gen_animals(lists)
    cnt = 0
    length = len(lists)
    while(cnt < 1000):
        #print_Grid(cnt)
        print(cnt, end=" ")
        cnt+=1
        # Problem is removing lion during the iteration

        for i in range(0, length-1):
            list_of_animal = Animal_lists[i]
            tmp = len(list_of_animal)
            print(tmp, end =" ")
            j = 0
            while j < len(list_of_animal):
                list_of_animal[j].use_turn()
                j+=1
                if tmp != len(list_of_animal):
                    tmp = len(list_of_animal)
                    j -= 1
                if (tmp == 0):
                    break
        # make grass
        gen_species(length -1, 2)
        print(len(Animal_lists[length-1]), end=" ")

        print()

input = [0, 100, 0, 0, 150]
simulate(input)