# Generator losowych danych dla testow

# pole [p] ->           !p      b       !k      d
# browar [b] ->         !p      !b      k       d
# karczma [k] ->        !p      !b      !k      !d
# skrzyzowanie [d] ->   !p      b       k       d

import random

p: int = random.randint(1, 20)
b: int = random.randint(1, 20)
k: int = random.randint(1, 20)
d: int = random.randint(0, 20)

with open('dane_1.txt', 'w') as f:
    # w pierwszej linii sa kolejno: liczba pol [p], liczba browarow [b], liczba karczm [k],
    # liczba skrzyzowan [d], przelicznik produkcji z browaru z jeczmienia [0.5]
    f.write(str(p) + ' ' + str(b) + ' ' + str(k) + ' ' + str(d) + ' 0.5')

    # w 5 kolejnych wierszach losowane sa przepustowosci cwiartek
    for i in range(5):
        f.write('\n' + str(random.randint(5, 20)))

    # w p kolejnych wierszach losowane sa wspolrzedne pol
    for i in range(p):
        f.write('\n' + str(random.randint(-500, 500)) + ' ' + str(random.randint(-500, 500)))

    # w b kolejnych wierszach losowane sa przepustowosci browarow
    for i in range(b):
        f.write('\n' + str(random.randint(1, 10)))

    # w k kolejnych wierszach losowane sa przepustowosci karczm
#    for i in range(k):
#        f.write('\n' + str(random.randint(1, 10)))

    # generowanie miejsca docelowego dla kazdego pola
    for i in range(p):
        wierzch = 'b'
        x = b
        if random.randint(1, 2) == 2:
            wierzch = 'k'
            x = k
        f.write('\np' + str(i + 1) + ' ' + wierzch + str(random.randint(1, x)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' 1')

    # generowanie miejsca startowego i docelowego dla kazdego browaru
    for i in range(b):
        wierzch = 'p'
        wierzch1 = 'k'
        x = p
        x1 = k
        if random.randint(1, 2) == 2:
            wierzch = 'd'
            x = d
        if random.randint(1, 2) == 2:
            wierzch1 = 'd'
            x1 = d
        f.write('\n' + wierzch + str(random.randint(1, x)) + ' b' + str(i + 1) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' 1')
        f.write('\nb' + str(i + 1) + ' ' + wierzch1 + str(random.randint(1, x1)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' 1')

    # generowanie miejsca startowego dla kazdej karczmy
    for i in range(k):
        wierzch = 'b'
        x = b
        if random.randint(1, 2) == 2:
            wierzch = 'd'
            x = d
        f.write('\n' + wierzch + str(random.randint(1, x)) + ' k' + str(i + 1) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' 1')

    # generowanie miejsca startowego i docelowego dla kazdego skrzyzowania
    for i in range(d):
        wierzch = 'd'
        wierzch1 = 'd'
        x = d
        x1 = d
        rand = random.randint(1, 3)
        rand1 = random.randint(1, 3)
        if rand == 2:
            wierzch = 'p'
            x = p
        elif rand == 3:
            wierzch = 'b'
            x = b
        if rand1 == 2:
            wierzch1 = 'k'
            x1 = k
        elif rand1 == 3:
            wierzch1 = 'b'
            x1 = b
        f.write('\n' + wierzch + str(random.randint(1, x)) + ' d' + str(i + 1) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' 1')
        f.write('\nd' + str(i + 1) + ' ' + wierzch1 + str(random.randint(1, x1)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' 1')
