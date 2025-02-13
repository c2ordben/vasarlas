f = open('vasarlas.csv', 'r')
nulla = 0

def koltott():
    napSzam = 0
    for szam in f:
        szam = szam.strip()
        tmp = szam.split(";")
        for nap in tmp:
            napSzam +=1
        print(napSzam,'nap volt a hónapban')

koltott()


f.close
