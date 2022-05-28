# Generator losowych danych dla Królestwa bez podziału na strefy

# Dokąd może prowadzić droga z danego miejsca:
# pole [p] ->           p      b      k      d
# browar [b] ->         p      b      k      d
# karczma [k] ->        p      b      k      d
# skrzyzowanie [d] ->   p      b      k      d

import random

p: int = random.randint(1, 20)
b: int = random.randint(1, 20)
k: int = random.randint(1, 20)
d: int = random.randint(1, 20)

with open('dane_2.txt', 'w') as f:
    # w pierwszej linii sa kolejno: liczba pol [p], liczba browarow [b], liczba karczm [k],
    # liczba skrzyzowan [d], przelicznik produkcji browaru z jeczmienia [0.5]
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

    # generowanie miejsca docelowego i startowego dla kazdego pola
    for i in range(p):
        wierzch = 'p'
        wierzch1 = 'p'
        x = p
        x1 = p
        rand = random.randint(1, 4)
        rand1 = random.randint(1, 4)
        if rand == 2:
            wierzch = 'b'
            x = b
        elif rand == 3:
            wierzch = 'k'
            x = k
        elif rand == 4:
            wierzch = 'd'
            x = d
        if rand1 == 2:
            wierzch1 = 'b'
            x1 = b
        elif rand1 == 3:
            wierzch1 = 'k'
            x1 = k
        elif rand1 == 4:
            wierzch1 = 'd'
            x1 = d
        f.write('\n' + wierzch + str(random.randint(1, x)) + ' p' + str(i + 1) + ' ' + str(
            random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(1, 100)))
        f.write('\np' + str(i + 1) + ' ' + wierzch1 + str(random.randint(1, x1)) + ' ' + str(
            random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(1, 100)))

    # generowanie miejsca docelowego i startowego dla kazdego browaru
    for i in range(b):
        wierzch = 'p'
        wierzch1 = 'p'
        x = p
        x1 = p
        rand = random.randint(1, 4)
        rand1 = random.randint(1, 4)
        if rand == 2:
            wierzch = 'b'
            x = b
        elif rand == 3:
            wierzch = 'k'
            x = k
        elif rand == 4:
            wierzch = 'd'
            x = d
        if rand1 == 2:
            wierzch1 = 'b'
            x1 = b
        elif rand1 == 3:
            wierzch1 = 'k'
            x1 = k
        elif rand1 == 4:
            wierzch1 = 'd'
            x1 = d
        f.write('\n' + wierzch + str(random.randint(1, x)) + ' b' + str(i + 1) + ' ' + str(
            random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(1, 100)))
        f.write('\nb' + str(i + 1) + ' ' + wierzch1 + str(random.randint(1, x1)) + ' ' + str(
            random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(1, 100)))

    # generowanie miejsca docelowego i startowego dla kazdej karczmy
    for i in range(k):
        wierzch = 'p'
        wierzch1 = 'p'
        x = p
        x1 = p
        rand = random.randint(1, 4)
        rand1 = random.randint(1, 4)
        if rand == 2:
            wierzch = 'b'
            x = b
        elif rand == 3:
            wierzch = 'k'
            x = k
        elif rand == 4:
            wierzch = 'd'
            x = d
        if rand1 == 2:
            wierzch1 = 'b'
            x1 = b
        elif rand1 == 3:
            wierzch1 = 'k'
            x1 = k
        elif rand1 == 4:
            wierzch1 = 'd'
            x1 = d
        f.write('\n' + wierzch + str(random.randint(1, x)) + ' k' + str(i + 1) + ' ' + str(
            random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(1, 100)))
        f.write('\nk' + str(i + 1) + ' ' + wierzch1 + str(random.randint(1, x1)) + ' ' + str(
            random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(1, 100)))

    # generowanie miejsca docelowego i startowego dla kazdego skrzyzowania
    for i in range(d):
        wierzch = 'p'
        wierzch1 = 'p'
        x = p
        x1 = p
        rand = random.randint(1, 4)
        rand1 = random.randint(1, 4)
        if rand == 2:
            wierzch = 'b'
            x = b
        elif rand == 3:
            wierzch = 'k'
            x = k
        elif rand == 4:
            wierzch = 'd'
            x = d
        if rand1 == 2:
            wierzch1 = 'b'
            x1 = b
        elif rand1 == 3:
            wierzch1 = 'k'
            x1 = k
        elif rand1 == 4:
            wierzch1 = 'd'
            x1 = d
        f.write('\n' + wierzch + str(random.randint(1, x)) + ' d' + str(i + 1) + ' ' + str(
            random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(1, 100)))
        f.write('\nd' + str(i + 1) + ' ' + wierzch1 + str(random.randint(1, x1)) + ' ' + str(
            random.randint(0, 10)) + ' ' + str(random.randint(0, 10)) + ' ' + str(random.randint(1, 100)))
