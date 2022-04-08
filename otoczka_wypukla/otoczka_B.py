import math


def det(a):
    x = (a[0][0] * a[1][1] * a[2][2]) + (a[1][0] * a[2]
                                         [1] * a[3][2]) + (a[2][0] * a[3][1] * a[4][2])
    y = (a[0][2] * a[1][1] * a[2][0]) + (a[1][2] * a[2]
                                         [1] * a[3][0]) + (a[2][2] * a[3][1] * a[4][0])
    return x - y


def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


n = int(input("ilosc punktow: "))
T = [[0 for x in range(2)] for y in range(n)]

# wprowadzenie punktow oraz szukanie min i max
for i in range(n):
    print(str(i+1) + ":")
    T[i][0] = int(input())
    T[i][1] = int(input())
    if(i == 0):
        max = i
        min = i
    elif(T[i][1] < T[min][1]):
        min = i
    elif(T[i][1] == T[min][1]):
        if(T[i][0] < T[min][0]):
            min = i
    if(T[i][1] > T[max][1]):
        max = i
    elif(T[i][1] == T[max][1]):
        if(T[i][0] > T[max][0]):
            max = i


nast = min+1
print("minimalny punkt: " + str(T[min][0]) + " " + str(T[min][1]))
print("maksymalny punkt: " + str(T[max][0]) + " " + str(T[max][1]))
print("kolejnosc katow: " + str(min+1))

S = T.copy()
n = len(T)
nk = [float('inf')][float('inf')]
detmin = float('inf')

while nk != T[max]:
    for i in range(n):
        for j in range(n):
            A = [[T[min][0], T[min][1], 1],
                 [S[i][0], S[i][1], 1],
                 [S[j][0], S[j][1], 1]]
            if det(A) > 0:
                S.pop(j)
            elif det(A) < 0:
                S.pop(i)
            else:
                if(distance(T[min][0], T[min][1], S[i][0], S[i][1]) > distance(T[min][0], T[min][1], S[j][0], S[j][1])):
                    S.pop(j)
                else:
                    S.pop(i)
            n -= 1
            if(n == 1):
                i = n
                j = n
