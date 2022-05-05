import otoczka

def czy_przynalezy(pkt):
    o = otoczka.znajdz_otoczke()
    #auto
    #intercepts = [ &](QPoint p1, QPoint p2, int y)
    #{
    #if ((p1.y() > y & & p2.y() < y) | | (p1.y() < y & & p2.y() > y))
    #return true;
    #else if ((p1.y() < p2.y() & & p1.y() == y) | | (p2.y() < p1.y() & & p2.y() == y)) return true;
    #else return false;

    return o

class Punkt:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


if __name__ == '__main__':
    pkty = [Punkt(-19,21), Punkt(11,-78),Punkt(6,-64),Punkt(-21,-80),Punkt(-86,15),Punkt(-2,86),Punkt(58,16),Punkt(92,-59),Punkt(-99,-31),Punkt(18,-66)]
    for pkt in pkty:
        czy_przynalezy(pkt)
