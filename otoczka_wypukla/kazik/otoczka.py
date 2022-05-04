from math import sqrt

def det(a):
    r = a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]+a[0][2]*a[1][0]*a[2][1] - (a[0][2]*a[1][1]*a[2][0]+a[0][0]*a[1][2]*a[2][1]+a[0][1]*a[1][0]*a[2][2])
    return r
def dst(p1,p2):
    return sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
def usun_nierozwazane(nierozwazane,lista):
    for element in nierozwazane:
        lista.pop(lista.index(element))

class Punkt:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return "("+str(self.x) + ", "+str(self.y)+")"
        
if __name__ == '__main__':
        plik = open("dane.txt","r")
        n = int(plik.readline())
        punkty = []
        ymin = float('inf')
        ymax = float('-inf')
        xmin = float('inf')
        xmax = float('-inf')
        for i in range(n):
            linia = plik.readline()
            x = int(linia.split(" ")[0])
            y = int(linia.split(" ")[1])
            if y < ymin:
                ymin = y
                xmin = x
                imin = i
            elif y == ymin:
                if x < xmin:
                    xmin = x
                    imin = i
            if y > ymax:
                ymax = y
                xmax = x
                imax = i
            elif y == ymax:
                if x > xmax:
                    xmax = x
                    imax = i
            punkty.append(Punkt(x,y))
        otoczka = [punkty[imin]]
        nwk = punkty[imin]
        rozwazane_punkty = punkty.copy()
        rozwazane_punkty.pop(imin)
        indeksy_pktow_otoczki = [imin]
        while nwk != punkty[imax]:
            while len(rozwazane_punkty) > 1:
                A = [[nwk.x, nwk.y, 1], [rozwazane_punkty[0].x, rozwazane_punkty[0].y, 1], [rozwazane_punkty[1].x, rozwazane_punkty[1].y, 1]]
                if det(A) > 0:
                    rozwazane_punkty.pop(0)
                elif det(A) < 0:
                    rozwazane_punkty.pop(1)
                else:
                    if dst(nwk,rozwazane_punkty[0]) > dst(nwk,rozwazane_punkty[1]):
                        rozwazane_punkty.pop(1)
                    else:
                        rozwazane_punkty.pop(0)
            nwk = rozwazane_punkty[0]
            otoczka.append(nwk)
            indeksy_pktow_otoczki.append(punkty.index(nwk))
            rozwazane_punkty = punkty.copy()
            usun_nierozwazane(otoczka,rozwazane_punkty)
        while nwk != punkty[imin]:
            while len(rozwazane_punkty) > 1:
                A = [[nwk.x, nwk.y, 1], [rozwazane_punkty[0].x, rozwazane_punkty[0].y, 1], [rozwazane_punkty[1].x, rozwazane_punkty[1].y, 1]]
                if det(A) > 0:
                    rozwazane_punkty.pop(0)
                elif det(A) < 0:
                    rozwazane_punkty.pop(1)
                else:
                    if dst(nwk,rozwazane_punkty[0]) > dst(nwk,rozwazane_punkty[1]):
                        rozwazane_punkty.pop(1)
                    else:
                        rozwazane_punkty.pop(0)
            nwk = rozwazane_punkty[0]
            if nwk == punkty[imin]:
                break
            otoczka.append(nwk)
            indeksy_pktow_otoczki.append(punkty.index(nwk))
            rozwazane_punkty = punkty.copy()


        print("indeksy punktów należących do otoczki w zadanym zbiorze punktów: ", end="")
        print(indeksy_pktow_otoczki)
        print("punkty należące do otoczki w zadanym zbiorze punktów: ", end="")
        print(*otoczka, sep=", ")