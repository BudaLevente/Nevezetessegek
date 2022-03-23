f = open("állatok.txt","r",encoding="UTF-8")
nagylista=[]
for sor in f:
    #print(sor)
    kislista=sor[:-1].split(";")
    #print(kislista)
    nagylista.append(kislista)
f.close()
