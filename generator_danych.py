#Generator losowo wygenerowanych danych dla testow
#w pierwszej linii sa kolejno: liczba pol [p], liczba browarow [b], przelicznik produkcji z jeczmienia na browar oraz liczba skrzyzowan [k]
#w 5 kolejnych wierszach sa przepustowosci cwiartek
#w p kolejnych wierszach sa wspolrzedne pol
#w b kolejnych wierszach sa przepustowosci browarow
#p -> !p    b   k   !S  !T
#b -> !p    !b  !k  !S  T
#k -> !p    b   k   !S  !T

import random

p: int = random.randint(1, 20)
b: int = random.randint(1, 20)
k: int = random.randint(0, 40)

with open('dane_1.txt','w') as f:
    f.write(str(p) + ' ' + str(b) + ' ' + str(0.5) + ' ' + str(k))

    for i in range(5):
        f.write('\n' + str(random.randint(1, 10)))

    for i in range(p):
        f.write('\n' + str(random.randint(-500,500)) + ' ' + str(random.randint(-500,500)))

    for i in range(b):
        f.write('\n' + str(random.randint(1,10)))

    for i in range(p):
        skrz='b'
        x=b
        if (random.randint(1,2)==2):
            skrz='k'
            x=k
        f.write('\np' + str(i+1) + ' ' + skrz + str(random.randint(1,x)))

    for i in range(b):
        skrz='p'
        x=p
        if (random.randint(1,2)==2):
            skrz='k'
            x=k
        f.write('\n' + skrz + str(random.randint(1,x)) + ' b' + str(i+1))

    for i in range(k):
        skrz='b'
        x=b
        skrz1='p'
        x1=p
        if (random.randint(1, 2) == 2):
            skrz='k'
            x=k
        if (random.randint(1, 2) == 2):
            skrz1='k'
            x1=k

        f.write('\nk' + str(i+1) + ' ' + skrz + str(random.randint(1,x)))
        f.write('\n' + skrz1 + str(random.randint(1,x1)) + ' k' + str(i+1))
