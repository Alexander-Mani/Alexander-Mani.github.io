#Alexander_Máni_Einarsson
#06/11/19
#Skilaverkefni

#Föll fyrir lið 1
def lesaskra(s):
    lesaskra_listi = []
    with open(s, "r", encoding="utf-8") as f:
        for line in f:
            lesaskra_listi = line.split(",")
        f.close()
        for x in range(len(lesaskra_listi)):
            print(lesaskra_listi[x], end=" ")
            if x+1 == 3 or x+1 == 6 or x+1 == 9:
                print()


#def summa_5(s):
    #summaskra_listi = []
    #with open(s, "r", encoding="utf-8") as f:
        #for line in f:
            #summaskra_listi = line.split(",")
        #f.close()
        summa = 0
    #for x in range(len(summaskra_listi)):
        #stak = summaskra_listi[x]
        #stak = int(stak)
        #ER orðin geðveikur að reyna finna þetta út 98% af tímanum mínum fór í þetta afhverju er ekki hægt að ger þetta string að int
    #summa = stak + summa


#fyrir lið 2
def prenta_tuples(t):
    for x in range(len(t)):
        print(x+1,"=>",t[x])

#fryrir lið 3
def medaltal(d):
    lyklar = d.keys()
    summa = sum(lyklar)
    medal = summa / len(lyklar)
    return medal

def dict_fall(d,tolur):
    ord_listi = []
    tolu_listi = tolur.split(";")
    for x in range(len(tolu_listi)):
        stak = tolu_listi[x]
        stak = int(stak)
        if stak in d.keys():
            stafur = d.get(stak)
            ord_listi.append(stafur)
    ord = ""
    for x in range(len(ord_listi)):
        x = x +1
        stak = ord_listi[-x]
        ord = stak + ord
    return ord



on = True
while on:
    print()
    print("=-=-=-> Tímaverkefni 2 <-=-=-=")
    print()
    print("1. Skrá")
    print("2. Tuples")
    print("3. Dictionary")
    print("4. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        #.	Búið til skránna skr.txt sem innheldur tölurnar: 152,235,540,4566,5666,6766567,5, 56,567
        with open("skra.txt","w",encoding = "utf-8") as f:
            f.write(str(52))
            f.write(",")
            f.write(str(235))
            f.write(",")
            f.write(str(540))
            f.write(",")
            f.write(str(4566))
            f.write(",")
            f.write(str(5666))
            f.write(",")
            f.write(str(6766567))
            f.write(",")
            f.write(str(5))
            f.write(",")
            f.write(str(56))
            f.write(",")
            f.write(str(567))
            f.write(",")
            f.close()

        #lesa skrá
        lesaskra("skra.txt")

        #Finna summu skrár
        #summa_5("skra.txt")

    elif val == 2:
        print()
        hluta_tuple = ("veiðistöng","fluga","veiðihjól","stígvél","taska","háfur")
        prenta_tuples(hluta_tuple)
        print()
        stafur = input("Sláðu inn upphafsstaf af orði sem þú vilt prenta úr my tuples")
        print()
        for x in range(len(hluta_tuple)):
            stak = hluta_tuple[x]
            if stafur == stak[0] or stafur.upper == stak[0]:
                print(stak)

    elif val == 3:
        print()
        stafrof = {1: "a", 2: "b", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "r", 17: "s", 18: "t", 19: "u", 20: "v", 21: "y"}
        print()
        medal = medaltal(stafrof)
        print("Meðaltal lykkla stafrófsins er: ",medal)
        print()
        print(dict_fall(stafrof,"10;14;13;13;8"))
    elif val == 4:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
