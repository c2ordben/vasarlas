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
        if nap == '0':
            nulla += 1
    print(nulla, 'nap nem volt költés')


def atlagKoltes(tmp):
    atlag = 0
    for nap in tmp:
        atlag += int(nap)
    print('átlag költés:', atlag/len(tmp))


def legKisebb(tmp):
    legkisebb = 10000
    for nap in tmp:
        if int(nap) != 0:
            if int(nap) < legkisebb:
                legkisebb = int(nap)
    print(legkisebb,'volt a legkisebb vásárlás')


def legNagyobb(tmp):
    legnagyobb = 1
    for nap in tmp:
        if int(nap) > legnagyobb:
            legnagyobb = int(nap)
    print(legnagyobb,'volt a legnagyobb vásárlás')

f.close


koltott(tmp)
nincsKoltes(tmp)
atlagKoltes(tmp)
legKisebb(tmp)
legNagyobb(tmp)