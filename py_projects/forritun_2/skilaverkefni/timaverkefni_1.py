#Alexander_Máni_Einarsson
#24/02/20
#tímaverkefni

import random

#fyrir lið 1
def randomListi(fjListi, randbyrjun, randendir):
    for x in range(20):
        rando_tala = random.randint(randbyrjun,randendir)
        if len(fjListi) != 20:
            fjListi.append(rando_tala)
    return fjListi

#Fyrir lið 2
def fjoldiOrda(strengur):
    ord = 1
    for x in range(len(strengur)):
        stafur = strengur[x]
        if stafur == " ":
            ord = ord +1
    return ord

def fjoldiB(strengur):
    b_teljari = 0
    for x in range(len(strengur)):
        stafur = strengur[x]
        if stafur == "b" or stafur == "B":
            b_teljari = b_teljari + 1
    return b_teljari

def snuaVid(strengur):
    strengur_ofugt = strengur[::-1]
    return strengur_ofugt

# Fyrir lið 3
def flatarmal(lengd, breidd):
    flotur = lengd * breidd
    return flotur

def heildarFlatarmal(*herbergi):
    heildar_flotur = 0
    for x in range(len(herbergi)):
        heildar_flotur = heildar_flotur + herbergi[x]
    return heildar_flotur





on = True
while on:
    print()
    print("=-=-=-> Tímaverkefni 1 <-=-=-=")
    print()
    print("1. Listi")
    print("2. Strengir")
    print("3. Föll")
    print("4. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        talnalisti = []
        byrjun = 10
        endir = 20
        talnalisti = randomListi(talnalisti,byrjun,endir)
        #A
        print()
        for x in range(len(talnalisti)):
            print(talnalisti[x],end="-")
        #B
        print()
        print(talnalisti)
        while 15 in talnalisti:
            talnalisti.remove(15)
        print(talnalisti)
        #C
        print()
        print("Þetta er breytti listinn með engum 15ánum")
        for x in range(len(talnalisti)):
            print(talnalisti[x])
        #D
        print()
        while 12 in talnalisti:
            stadur = talnalisti.index(12)
            talnalisti.remove(12)
            talnalisti.insert(stadur,22)
        #E
        print()
        print("Þetta er breytti listinn með 22 í stað 12")
        for x in range(len(talnalisti)):
            print(talnalisti[x])
        #F
        print()
        medaltal = sum(talnalisti)/len(talnalisti)
        print("Meðaltalið er", round(medaltal,2))
        #G
        print()
        tiu_teljari = 0
        for x in range(len(talnalisti)):
            tala = talnalisti[x]
            if tala == 10:
                tiu_teljari = tiu_teljari +1
        print("Tíu kemur fyrir",tiu_teljari,"Sinnum.")


    elif val == 2:
        print()
        texti = input("Sláðu inn setningu")
        #A
        print()
        print("Fjöldi orða er: ",fjoldiOrda(texti))
        #B
        print()
        print("Fjöldi b/B-a er/u: ", fjoldiB(texti))
        #C
        print()
        tolur = 0
        for x in range(len(texti)):
            stafur = texti[x]
            if stafur.isdigit():
                tolur = tolur + 1
        print("Það eru svona margar tölur: ",tolur)
        #D
        print()
        print("Svona er textinn öfugur: ",snuaVid(texti))

    elif val == 3:
        print()
        l_listi = []
        b_listi = []
        print("Sláðu inn lengd og breidd fjagra herbergja")
        for x in range(4):
            print("Herbergi", x+1)
            l = int(input("Sláðu inn lengd: "))
            b = int(input("Sláðu inn breidd: "))
            l_listi.append(l)
            b_listi.append(b)
        #A
        f_listi = []
        for x in range(len(b_listi)):
            herb = flatarmal(l_listi[x],b_listi[x])
            print("Herbergi",x+1,"er",herb,"fermetrar")
            f_listi.append(herb)
        #B
        heild = heildarFlatarmal(f_listi[0], f_listi[1], f_listi[2], f_listi[3])
        print("Heildar flatarmálið er: ", heild)
        #C
        medaltal = heild/4
        print("Meðaltalherbergjana er: ", round(medaltal, 2))
        if medaltal > 15:
            print("Vá stór herbergi")
        elif medaltal > 6 and medaltal < 16:
            print("Meðaltal meðaltal")
        elif medaltal < 7:
            print("Hvílíkur kompur")
        else:
            print("Villa koma upp")

    elif val == 4:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
