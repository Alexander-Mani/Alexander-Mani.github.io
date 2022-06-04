#Alexander_Máni_Einarsson
#06/11/19
#Skilaverkefni

#Fyrir verkefni 1
def skrifa_ut(listi):
    print(listi)

def staersta(listi):
    staerst = 0
    for x in listi:
        if x > staerst:
            staerst = x
    return staerst

def minnsta(listi):
    minnst = 100000000000000
    for x in listi:
        if x < minnst:
            minnst = x
    return minnst

def summa(listi):
    summan = 0
    for x in listi:
        summan = x + summan
    return summan

def medaltal(listi):
    summan = 0
    teljari = 0
    for x in listi:
        summan = x + summan
        teljari = teljari +1
    summan = summan/teljari
    return summan

def setning(starf_grein="smiðurinn",nafn='konni',adgerd='sefur',hlutur='rólega'):
    print(starf_grein,nafn,adgerd,hlutur)

def tolur(*innset):
    teljari = 0
    sum = 0
    for x in range(len(innset)):
        sum = sum + x
        teljari = teljari +1
    sum = sum/teljari
    return sum

def texas(texti,ord):
    teljari = 0
    for x in range(len(texti[teljari])):
        print(texti[teljari])
        teljari = teljari +1

        if ord == x:
            print("Þetta orð er í textanum")
        else:
            print("Þetta orð er ekki í textanum")


on = True
while on:
    print()
    print("=-=-=-> Skilaverkefni <-=-=-=")
    print()
    print("1. Fimm föll")
    print("2. fallið")
    print("3. ")
    print("4. ")
    print("5. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        talnalisti = []
        print("Skrifaðu inn 5 tölur")
        for x in range(5):
            nafn = int(input("Skrafðu tölu"))
            talnalisti.append(nafn)
        skrifa_ut(talnalisti)
        print("Stærsta talan er: ",staersta(talnalisti))
        print("Minnsta talan er: ",minnsta(talnalisti))
        print("Summan er: ", summa(talnalisti))
        print("Meðaltalið er: ", medaltal(talnalisti))


    elif val == 2:
        print()
        setning()
        setning(starf_grein="forritari")
        setning(starf_grein="forritarinn",nafn="halldór")
        setning(starf_grein="forritarinn", nafn="halldór",hlutur="fast")
        setning(starf_grein="forritarinn", nafn="halldór", hlutur="fast",adgerd="slær")

    elif val == 3:
        print()
        talna = int(input("Sláðu inn fjöld talna"))

        medal = tolur(talna)+tolur(talna*2)
        print(medal)

    elif val == 4:
        print()
        textin = input("Sláðu inn texta")
        ordid = input("Sláðu inn orð")
        texas(textin,ordid)


    elif val == 5:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
