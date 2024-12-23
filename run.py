# Fésüljünk össze két felhasználó által bekért tömböt majd számoljuk meg hány darab negatív szám van az összefésült tömbben.

tomb_1 = list(
    map(int, input("Adja meg az első tömb elemeit szóközökkel elválasztva: ").split())
)
tomb_2 = list(
    map(int, input("Adja meg a második tömb elemeit szóközökkel elválasztva: ").split())
)

# Segédváltozók
n = len(tomb_1)  # 1. tömb hossza
m = len(tomb_2)  # 2. tömb hossza

# Közös tömb
ossz = [0] * (n + m)

# Első tömb buborék rendezése
for i in range(n - 1):
    for j in range(n - i - 1):
        if tomb_1[j] > tomb_1[j + 1]:
            seged = tomb_1[j]
            tomb_1[j] = tomb_1[j + 1]
            tomb_1[j + 1] = seged


print("Első rendezett tömb: ", tomb_1)

# Második tömb buborék rendezése
for k in range(m - 1):
    for l in range(m - k - 1):
        if tomb_2[l] > tomb_2[l + 1]:
            seged = tomb_2[l]
            tomb_2[l] = tomb_2[l + 1]
            tomb_2[l + 1] = seged

print("Második rendezett tömb: ", tomb_2)


# Összefésülés
i = 0  # tomb_1 tömb indexe
j = 0  # tomb_2 tömb indexe
k = -1  # ossz tömb indexe

while i < n and j < m:
    k = k + 1
    if tomb_1[i] < tomb_2[j]:
        ossz[k] = tomb_1[i]
        i = i + 1
    elif tomb_1[i] == tomb_2[j]:
        ossz[k] = tomb_1[i]
        i = i + 1
        j = j + 1
    elif tomb_1[i] > tomb_2[j]:
        ossz[k] = tomb_2[j]
        j = j + 1

while i < n:
    k = k + 1
    ossz[k] = tomb_1[i]
    i = i + 1

while j < m:
    k = k + 1
    ossz[k] = tomb_2[j]
    j = j + 1


# Megszámolás
neg_szam = 0  # segédváltozó a negatív számok megszámlálásához
ossz_hossz = len(ossz)  # ossz nevű tömb hossza (tomb_1 + tomb_2)

for i in range(ossz_hossz):
    if ossz[i] < 0:
        neg_szam = neg_szam + 1

print("Összefésült tömb:", ossz)
print("Összesen ennyi negatív szám van az összefésült tömbben:", neg_szam)
