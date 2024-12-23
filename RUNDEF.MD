## Feladat megoldása függvények használatával

tomb_1:= []\
tomb_2:= []

// Buborék rendezés\
BUBOREK (TOMB)\
&nbsp;&nbsp;&nbsp; n = // TOMB hossz\
&nbsp;&nbsp;&nbsp; CIKLUS i = n-1 TŐL 1 IG\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CIKLUS J = 0 TÓL i-1 IG\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; HA TOMB[j] > TOMB[j+1] AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; seged:= TOMB[j]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TOMB[j]:= TOMB[j+1]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TOMB[j+1]:= seged\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ELÁGAZÁS VÉGE\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CIKLUS VÉGE\
&nbsp;&nbsp;&nbsp; CIKLUS VÉGE\
ELJÁRÁS VÉGE

// Összefésülés\
OSSZEFESULES (TOMB1, TOMB2)\
&nbsp;&nbsp;&nbsp; n = // TOMB1 hossza\
&nbsp;&nbsp;&nbsp; m = // TOMB2 hossza\
&nbsp;&nbsp;&nbsp; ossz = // közös tömb\
&nbsp;&nbsp;&nbsp; i:=0 // TOMB1 indexe\
&nbsp;&nbsp;&nbsp; j:=0 // TOMB2 indexe\
&nbsp;&nbsp;&nbsp; k:=-1 // ossz tömb indexe\

&nbsp;&nbsp;&nbsp; CIKLUS AMÍG i < n ÉS j < m\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; k:= k + 1\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; HA TOMB1[i] < TOMB2[j] AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ossz[k]:= TOMB1[i]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i:= i + 1\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ELLENBEN\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; HA TOMB1[i] == TOMB2[j] AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ossz[k]:= TOMB1[i]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i:= i + 1\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; j:= j + 1\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ELLENBEN\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; HA TOMB1[i] > TOMB2[j] AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ossz[k]:= TOMB2[j]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; j:= j + 1\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ELÁGAZÁS VÉGE\
&nbsp;&nbsp;&nbsp; CIKLUS VÉGE\

&nbsp;&nbsp;&nbsp; CIKLUS AMÍG i < n\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; k:= k + 1\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ossz[k]:= TOMB1[i]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i:= i + 1\
&nbsp;&nbsp;&nbsp; CIKLUS VÉGE\

&nbsp;&nbsp;&nbsp; CIKLUS AMÍG j < m
k:= k+1\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ossz[k]:= TOMB2[j]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; j:= j + 1\
&nbsp;&nbsp;&nbsp; CIKLUS VÉGE\
ELJÁRÁS VÉGE

// Megszámolás\
MEGSZAMOLAS\
&nbsp;&nbsp;&nbsp; ossz // összesített tömb amit az OSSZEFESULES nevű eljárás ad vissza\
&nbsp;&nbsp;&nbsp; neg_szam:= 0 // segédváltozó a negatív számok megszámlálásához\
&nbsp;&nbsp;&nbsp; ossz_hossz // ossz nevű tömb hossza (tomb_1 + tomb_2)

&nbsp;&nbsp;&nbsp; CIKLUS i = 0 TÓL ossz_hossz-1 IG\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; HA ossz[i] < 0 AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; neg_szam:= neg_szam + 1\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ELÁGAZÁS VÉGE\
&nbsp;&nbsp;&nbsp; CIKLUS VÉGE\
ELJÁRÁS VÉGE\
