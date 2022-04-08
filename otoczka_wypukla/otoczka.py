from math import sqrt


def det(a):
    r = a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]+a[0][2]*a[1][0]*a[2][1] - (a[0][2]*a[1][1]*a[2][0]+a[0][0]*a[1][2]*a[2][1]+a[0][1]*a[1][0]*a[2][2])
    return r
def dst(p1,p2):
    return  sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
def usun_nierozwazane(nierozwazane,lista):
    for element in nierozwazane:
        lista.pop(element)


class Punkt:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return "punkt o wspolrzednych ("+str(self.x) + ", "+str(self.y)+")"
        
if __name__ == '__main__':
        #max_size = 1024
        plik = open("dane.txt","r")
        n = int(plik.readline())
        #print(n)
        punkty = []
        ymin = float('inf')
        ymax = float('-inf')
        xmin = float('inf')
        xmax = float('-inf')
        #imin
        #punkt1 = Punkt(1,2)
        #punkt2 = Punkt(3,4)
        #punkt3 = Punkt(5,6)
        #punkty.append(punkt1)
        #punkty.append(punkt2)
        #punkty.append(punkt3)
        #for i in range(3):
        #   print(punkty[i])
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
            
                    
            #punkt = Punkt(x,y)
            
            punkty.append(Punkt(x,y))
        
        otoczka = [punkty[imin]]
        #nwk = Punkt(float('inf'),float('inf'))
        nwk = punkty[imin]
        rozwazane_punkty = punkty.copy()
        rozwazane_punkty.pop(imin)
        najmniejszy_kat = float('inf')
        indeksy_pktow_otoczki = [imin]

        while nwk != punkty[imax]:
            #for i in range(len(rozwazane_punkty)):
            #    for j in range(len(rozwazane_punkty)):
            #        A = [[punkty[imin].x,punkty[0].y,1],[punkty[imin].x,punkty[1].y,1],[punkty[2].x,punkty[2].y,1]]
            #        print(det(A))
            #indeks_nastepnego_pktu_otoczki = 0
            while len(rozwazane_punkty) > 1:
                #print(*rozwazane_punkty, sep=", ")
                # A = [[punkty[imin].x, punkty[imin].y, 1], [rozwazane_punkty[0].x, rozwazane_punkty[0].y, 1], [rozwazane_punkty[1].x, rozwazane_punkty[1].y, 1]]
                A = [[nwk.x, nwk.y, 1], [rozwazane_punkty[0].x, rozwazane_punkty[0].y, 1], [rozwazane_punkty[1].x, rozwazane_punkty[1].y, 1]]
                if det(A) > 0:
                    rozwazane_punkty.pop(0)
                    #indeks_nastepnego_pktu_otoczki += 1
                elif det(A) < 0:
                    rozwazane_punkty.pop(1)
                else:
                    #if dst(punkty[imin], rozwazane_punkty[0]) > dst(punkty[imin], rozwazane_punkty[1]):
                    if dst(nwk,rozwazane_punkty[0]) > dst(nwk,rozwazane_punkty[1]):
                        rozwazane_punkty.pop(1)
                    else:
                        rozwazane_punkty.pop(0)
                        #indeks_nastepnego_pktu_otoczki += 1
            nwk = rozwazane_punkty[0]
            otoczka.append(nwk)
            #indeksy_pktow_otoczki.append(indeks_nastepnego_pktu_otoczki)
            indeksy_pktow_otoczki.append(punkty.index(nwk))
            #nwk = punkty[imax]
            rozwazane_punkty = punkty.copy()
            #print(indeksy_pktow_otoczki)
            usun_nierozwazane(indeksy_pktow_otoczki,rozwazane_punkty)
            #print(*rozwazane_punkty, sep=", ")
        print(indeksy_pktow_otoczki)
        print("otoczka po pierwsyzm kroku alg jarvisa: ",end="")
        print(*otoczka, sep=", ")
        while nwk != punkty[imin]:
            #for i in range(len(rozwazane_punkty)):
            #    for j in range(len(rozwazane_punkty)):
            #        A = [[punkty[imin].x,punkty[0].y,1],[punkty[imin].x,punkty[1].y,1],[punkty[2].x,punkty[2].y,1]]
            #        print(det(A))
           #indeks_nastepnego_pktu_otoczki = 0
            while len(rozwazane_punkty) > 1:
                #print(*rozwazane_punkty, sep=", ")
                # A = [[punkty[imin].x, punkty[imin].y, 1], [rozwazane_punkty[0].x, rozwazane_punkty[0].y, 1], [rozwazane_punkty[1].x, rozwazane_punkty[1].y, 1]]
                A = [[nwk.x, nwk.y, 1], [rozwazane_punkty[0].x, rozwazane_punkty[0].y, 1], [rozwazane_punkty[1].x, rozwazane_punkty[1].y, 1]]
                if det(A) > 0:
                    rozwazane_punkty.pop(0)
                    #indeks_nastepnego_pktu_otoczki += 1
                elif det(A) < 0:
                    rozwazane_punkty.pop(1)
                else:
                    #if dst(punkty[imin], rozwazane_punkty[0]) > dst(punkty[imin], rozwazane_punkty[1]):
                    if dst(nwk,rozwazane_punkty[0]) > dst(nwk,rozwazane_punkty[1]):
                        rozwazane_punkty.pop(1)
                    else:
                        rozwazane_punkty.pop(0)
                        #indeks_nastepnego_pktu_otoczki += 1
            nwk = rozwazane_punkty[0]
            if nwk == punkty[imin]:
                break
            otoczka.append(nwk)
            #indeksy_pktow_otoczki.append(indeks_nastepnego_pktu_otoczki)
            indeksy_pktow_otoczki.append(punkty.index(nwk))
            #nwk = punkty[imax]
            rozwazane_punkty = punkty.copy()
            #print(indeksy_pktow_otoczki)
            #usun_nierozwazane(indeksy_pktow_otoczki,rozwazane_punkty)
            #print(*rozwazane_punkty, sep=", ")

        print(indeksy_pktow_otoczki)
        print("otoczka: ", end="")
        print(*otoczka, sep=", ")
        #szukamy punkty o najmniejsyzm kacie
        #A = [[punkty[0].x,punkty[0].y,1],[punkty[1].x,punkty[1].y,1],[punkty[2].x,punkty[2].y,1]]
        #print(det(A))
        #for i in range(n):
        #    print(i)
        #    print(punkty[i])
        #print(imin)
        #print(imax)
        #print(punkty[imin].x,punkty[imin].y)
        #print(punkty[imin])
        #print(punkty[imax])