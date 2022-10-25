
import random

def one():
    num = []
    i = 0
    while(len(num) < 10):
        i += 1
        if(i % 2 != 0):
            num.append(i)
    print(num)

def two():
    while(True):
        try:
            N = int(input("Сообщите количество элементов в массиве :"))
            if(N > 1):
                break
            else:
                print("Введено некоректное значение ")
        except ValueError:
            print("Введено некоректное значение ")
    array = []
    num = []

    for i in range(N):
        a = random.randint(0,99)
        array.append(a)

    k = 0
    print(array)
    for i in range(N - 1):
        if(array[i] > array[i + 1] ):
            num.append(i)
            k += 1
    num.sort(reverse=True)
    print("Hомера в порядке их возрастания")
    print(num)
    print("Kоличество таких элементов")
    print(k)

def three():
    A = []

    while(True):
        try:
            K = int(input("Сообщите начальный индекс перестановки K > 1 :"))
            if(K > 1):
                break
            else:
                print("Введено некоректное значение ")
        except ValueError:
            print("Введено некоректное значение ")

    while(True):
        try:
            L = int(input("Сообщите конечный индекс перестановки L > K :"))
            if(L > K):
                break
            else:
                print("Введено некоректное значение ")
        except ValueError:
            print("Введено некоректное значение ")


    while(True):
        try:
            N = int(input("Сообщите количество элементов в массиве N  > L :"))
            if(N  > L):
                break
            else:
                print("Введено некоректное значение ")
        except ValueError:
            print("Введено некоректное значение ")

    for i in range(N):
        a = random.randint(0,99)
        A.append(a)
        
    print(A)
    A[K:L - 1] = A[L-2:K-1:-1]
    print(A)




while(True):
    print("Выбирите задачу : \n1. Сформировать и вывести целочисленный список размера 10, содержащий 10 первых положительных нечетных чисел\n2. Дан список размера N. Найти номера тех элементов списка, которые больше своего правого соседа, и количество таких элементов. Найденные номера выводить в порядке их возрастания.\n3. Дан список A размера N и целые числа K и L (1 < K < L < N). Переставить в обратном порядке элементы списка, расположенные между элементами AK и AL, не включая эти элементы.")
    i = int(input())
    if i == 1:
        one()
    if i == 2:
        two()
    if i == 3:
        three()
    if i == 0:
        break