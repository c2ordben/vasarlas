f = open('vasarlas.csv', 'r')

for szam in f:
    szam = szam.strip()
    tmp = szam.split(";")

def koltott(tmp):
    napSzam = 0
    for nap in tmp:
        napSzam +=1
    print(napSzam,'nap volt a hónapban')


def nincsKoltes(tmp):
    nulla = 0
    for nap in tmp:
        if nap == 0:
            nulla += 1
        print(nulla, 'nap nem volt költés')
f.close
koltott(tmp)
nincsKoltes(tmp)
