ételek=["mandarin","csirkehús","burgonya","rizs","tejföl"]
n=False
for i in range(0,len(ételek)):
    if ételek[i]=="burgonya":
        print(i)
        n=True
if n==False:
    print("Nincs")
