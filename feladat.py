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


def osszesKoltes(tmp):
    osszesen = 0
    for nap in tmp:
        nap = int(nap)
        osszesen += nap
    print(osszesen,'volt az össz költekezés1')


def sorozatKoltesNelkul(tmp):
    sor = 0
    for i in range(len(tmp)):
        if int(tmp[i]) == int(tmp[i-1]):
            sor += 1
    print(sor, 'nap volt a leghosszabb sorozat vásárlás nélkül')

f.close


koltott(tmp)
nincsKoltes(tmp)
atlagKoltes(tmp)
legKisebb(tmp)
legNagyobb(tmp)
osszesKoltes(tmp)
sorozatKoltesNelkul(tmp)