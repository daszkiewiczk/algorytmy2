#Generator losowo wygenerowanych danych dla testow
#w pierwszej linii sa kolejno: liczba pol [p], liczba browarow [b], przelicznik produkcji z jeczmienia na browar oraz liczba polaczen [k]
#w 5 kolejnych wierszach sa przepustowosci cwiartek
#w p kolejnych wierszach sa wspolrzedne pol
#w b kolejnych wierszach sa przepustowosci browarow
#p -> !p    b   k
#b -> !p    !b  k
#k -> !p    b   k

import random

p: int = random.randint(1, 20)
b: int = random.randint(1, 20)
k: int = p + b + random.randint(0, 40)

with open('dane_1.txt','w') as f:
    f.write(str(p) + ' ' + str(b) + ' ' + str(k))



