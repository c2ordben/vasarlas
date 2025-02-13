f = open('vasarlas.csv', 'r')


for szam in f:
    szam = szam.strip()
    tmp = szam.split(";")
    
    print(tmp)

f.close