import otoczka
from punkt import Punkt

def przecina(p1,p2,y):
    if (p1.y > y and p2.y < y) or (p1.y < y and p2.y > y):
        return True
    elif (p1.y < p2.y and p1.y == y) or (p2.y < p1.y and p2.y == y):
        return True
    else:
        return False
def x_przeciecia(p1,p2,y):
    if p1.y == p2.y:    #prosta rownolegla do ox
        return 0
    x = p1.x + (y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y)
    return x
def czy_przynalezy(pkt,o):
    if pkt in o:
        return True
    ile_pktow_przeciecia = 0
    for i in range(len(o)):
        p1 = o[i]
        p2 = o[(i+1)%len(o)]
        if przecina(p1,p2,pkt.y):
            if x_przeciecia(p1,p2,pkt.y) > pkt.x:
                ile_pktow_przeciecia += 1
    if ile_pktow_przeciecia%2 == 1:
        return True
    else:
        return False



if __name__ == '__main__':
    pkty = [Punkt(-100,21),Punkt(-19,21), Punkt(11,-78),Punkt(6,-64),Punkt(-21,-80),Punkt(-86,15),Punkt(-2,86),Punkt(58,16),Punkt(92,-59),Punkt(-99,-31),Punkt(18,-66)]
    o = otoczka.znajdz_otoczke()
    for pkt in pkty:
        print(czy_przynalezy(pkt,o))
