# Fésüljünk össze két felhasználó által bekért tömböt majd számoljuk meg hány darab negatív szám van az összefésült tömbben.

tomb_1 = list(
    map(int, input("Adja meg az első tömb elemeit szóközökkel elválasztva: ").split())
)
tomb_2 = list(
    map(int, input("Adja meg a második tömb elemeit szóközökkel elválasztva: ").split())
)


def buborek(tomb):
    n = len(tomb)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if tomb[j] > tomb[j + 1]:
                seged = tomb[j]
                tomb[j] = tomb[j + 1]
                tomb[j + 1] = seged
    return tomb


print("Első rendezett tömb: ", buborek(tomb_1))
print("Második rendezett tömb: ", buborek(tomb_2))


# Összefésülés
def osszefesules(tomb1, tomb2):
    n = len(tomb1)  # 1. tömb hossza
    m = len(tomb2)  # 2. tömb hossza

    # Közös tömb
    ossz = [0] * (n + m)
    i = 0  # tomb_1 tömb indexe
    j = 0  # tomb_2 tömb indexe
    k = -1  # ossz tömb indexe

    while i < n and j < m:
        k = k + 1
        if tomb1[i] < tomb2[j]:
            ossz[k] = tomb1[i]
            i = i + 1
        elif tomb1[i] == tomb2[j]:
            ossz[k] = tomb1[i]
            i = i + 1
            j = j + 1
        elif tomb1[i] > tomb2[j]:
            ossz[k] = tomb2[j]
            j = j + 1

    while i < n:
        k = k + 1
        ossz[k] = tomb1[i]
        i = i + 1

    while j < m:
        k = k + 1
        ossz[k] = tomb2[j]
        j = j + 1

    return ossz


# Megszámolás
def megszamolas():
    ossz = osszefesules(tomb_1, tomb_2)
    neg_szam = 0  # segédváltozó a negatív számok megszámlálásához
    ossz_hossz = len(ossz)  # ossz nevű tömb hossza (tomb_1 + tomb_2)

    for i in range(ossz_hossz):
        if ossz[i] < 0:
            neg_szam = neg_szam + 1
    return neg_szam


print("Összefésült tömb:", osszefesules(tomb_1, tomb_2))
print("Összesen ennyi negatív szám van az összefésült tömbben:", megszamolas())
