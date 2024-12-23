## Feladat megoldása függvények használata nélkül

tomb_1:= []\
tomb_2:= []

// Segédváltozók a buborékrendezéshez és az összefésüléshez\
n // tomb_1 nevű tömb hossza\
m // tom_2 nevű tömb hossza\
ossz // közös tömb, hossza tomb_1 és tomb_2 tömbök hosszának összege

// Első tömb buborék rendezése\
CIKLUS i = n-1 TŐL 1 IG\
&nbsp;&nbsp;&nbsp; CIKLUS J = 0 TÓL i-1 IG\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; HA tomb_1[j] > tomb_1[j+1] AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; seged:= tomb_1[j]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tomb_1[j]:= tomb_1[j+1]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tomb_1[j+1]:= seged\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ELÁGAZÁS VÉGE\
&nbsp;&nbsp;&nbsp;CIKLUS VÉGE\
CIKLUS VÉGE

// Második tömb buborék rendezése\
CIKLUS k = m-1 TŐL 1 IG\
&nbsp;&nbsp;&nbsp; CIKLUS l = 0 TÓL k-1 IG\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; HA tomb_2[l] > tomb_2[l+1] AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; seged:= tomb_2[l]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tomb_2[l]:= tomb_2[l+1]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tomb_2[l+1]:= seged\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ELÁGAZÁS VÉGE\
&nbsp;&nbsp;&nbsp; CIKLUS VÉGE\
CIKLUS VÉGE

// Összefésülés\
i:=0 // tomb_1 indexe\
j:=0 // tomb_2 indexe\
k:=-1 // ossz tömb indexe\

CIKLUS AMÍG i < n ÉS j < m\
&nbsp;&nbsp;&nbsp; k:= k + 1\
&nbsp;&nbsp;&nbsp; HA tomb_1[i] < tomb_2[j] AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ossz[k]:= tomb_1[i]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i:= i + 1\
&nbsp;&nbsp;&nbsp; ELLENBEN\
&nbsp;&nbsp;&nbsp; HA tomb_1[i] == tomb_2[j] AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ossz[k]:= tomb_1[i]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i:= i + 1\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; j:= j + 1\
&nbsp;&nbsp;&nbsp; ELLENBEN\
&nbsp;&nbsp;&nbsp; HA tomb_1[i] > tomb_2[j] AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ossz[k]:= tomb_2[j]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; j:= j + 1\
&nbsp;&nbsp;&nbsp; ELÁGAZÁS VÉGE\
CIKLUS VÉGE

CIKLUS AMÍG i < n\
&nbsp;&nbsp;&nbsp; k:= k + 1\
&nbsp;&nbsp;&nbsp; ossz[k]:= tomb_1[i]\
&nbsp;&nbsp;&nbsp; i:= i + 1\
CIKLUS VÉGE\

CIKLUS AMÍG j < m\
&nbsp;&nbsp;&nbsp; k:= k+1\
&nbsp;&nbsp;&nbsp; ossz[k]:= tomb_2[j]\
&nbsp;&nbsp;&nbsp; j:= j + 1\
CIKLUS VÉGE

// Megszámolás\
neg_szam:= 0 // segédváltozó a negatív számok megszámlálásához\
ossz_hossz // ossz nevű tömb hossza (tomb_1 + tomb_2)

CIKLUS i = 0 TÓL ossz_hossz-1 IG\
&nbsp;&nbsp;&nbsp; HA ossz[i] < 0 AKKOR\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; neg_szam:= neg_szam + 1\
&nbsp;&nbsp;&nbsp;ELÁGAZÁS VÉGE\
CIKLUS VÉGE
