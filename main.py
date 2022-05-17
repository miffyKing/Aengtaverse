import random
from lion import Lion, Lion_Gen
from impala import Impala, Impala_Gen
from baboon import Baboon, Baboon_Gen
from animal import Grid, Grid_size, Lion_list, Impala_list, Baboon_list, Rhino_list
from rhino import Rhino, Rhino_Gen
# 동물 리스트 혹은 디

# 빈칸 or 동물 객체


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




Lion_Gen(20)
Impala_Gen(10)
Baboon_Gen(10)
Rhino_Gen(10)

while(len(Lion_list) > 0 or len(Impala_list) > 0 or len(Baboon_list) > 0 or len(Rhino_list) > 0):
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

    tmp = len(Baboon_list)
    i = 0
    while i < len(Baboon_list):
        Baboon_list[i].use_turn()
        i += 1
        if tmp != len(Baboon_list):
            tmp = len(Baboon_list)
            i -= 1
        if (tmp == 0):
            break

    tmp = len(Rhino_list)
    i = 0
    while i < len(Rhino_list):
        Rhino_list[i].use_turn()
        i += 1
        if tmp != len(Rhino_list):
            tmp = len(Rhino_list)
            i -= 1
        if (tmp == 0):
            break