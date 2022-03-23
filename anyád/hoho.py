a=open("hoho.txt","r",encoding="UTF-8")
nagylista=[]
for sor in a:
    kislista=sor[:-1].split(";")
    nagylista.append(kislista)

orszagok=[nagylista[0][1]],nagylista[1][1],nagylista[2][1],nagylista[3][1],nagylista[4][1],nagylista[5][1],nagylista[6][1],nagylista[7][1],nagylista[8][1],nagylista[9][1]
nevezetesegek=[nagylista[0][0],nagylista[1][0],nagylista[2][0],nagylista[3][0],nagylista[4][0],nagylista[5][0],nagylista[6][0],nagylista[7][0],nagylista[8][0],nagylista[9][0]]
evszam=[nagylista[0][2],nagylista[1][2],nagylista[2][2],nagylista[3][2],nagylista[4][2],nagylista[5][2],nagylista[6][2],nagylista[7][2],nagylista[8][2],nagylista[9][2]]


te=input("Miről szeretnél tudni? nevezetességek/országok/évszámok ")
if te == 'országok':
    sertes=input("milyen ország??? ")
    if sertes == "USA":
        print(nagylista[0],nagylista[7])
    elif sertes == 'Brazília':
        print(nagylista[1])
    elif sertes == 'Olaszország':
        print(nagylista[2])
    elif sertes == 'India':
        print(nagylista[3])
    elif sertes == 'Panamaváros':
        print(nagylista[4])
    elif sertes == 'Ausztrália':
        print(nagylista[5])
    elif sertes == 'Japán':
        print(nagylista[6],nagylista[9])
    elif sertes == 'Magyarország':
        print(nagylista[8])
    else:
        print("Nem adtál meg helyes cuccot :(")

elif te == "évszámok":
    sertes=input("milyen évszám??? ")
    if sertes == "1937":
        print(nagylista[0])
    elif sertes == '1935':
        print(nagylista[1])
    elif sertes == '1965':
        print(nagylista[2])
    elif sertes == '1653':
        print(nagylista[3])
    elif sertes == '1914':
        print(nagylista[4])
    elif sertes == '1973':
        print(nagylista[5])
    elif sertes == '1958':
        print(nagylista[6])
    elif sertes == '2014':
        print(nagylista[7])
    elif sertes == '1904':
        print(nagylista[8])
    elif sertes == '1920':
        print(nagylista[9])
    else:
        print("Nem adtál meg helyes cuccot :(")
    
elif te == "nevezetességek":
    sertes=input("milyen nevezetesség??? ")
    if sertes == "Golden Gate híd":
        print(nagylista[0])
    elif sertes == 'A Megváltó Krisztus szobra':
        print(nagylista[1])
    elif sertes == 'Milánói dóm':
        print(nagylista[2])
    elif sertes == 'Taj Mahal':
        print(nagylista[3])
    elif sertes == 'Panama-csatorna':
        print(nagylista[4])
    elif sertes == 'Operaház':
        print(nagylista[5])
    elif sertes == 'Tokyo tower':
        print(nagylista[6])
    elif sertes == 'Szeptember 11. emlékmű':
        print(nagylista[7])
    elif sertes == 'Parlament':
        print(nagylista[8])
    elif sertes == 'Meiji szentély':
        print(nagylista[9])
    else:
        print("Nem adtál meg helyes cuccot :(")
    
else:
    print("Nem adtál meg helyes cuccot :(")
    
    
    
    
    
    
    
    
