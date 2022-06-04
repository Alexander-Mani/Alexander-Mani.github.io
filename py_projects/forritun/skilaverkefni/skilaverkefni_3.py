#Alexander_Máni_Einarsson
#24/09/19
#Skilaverkefni_3
2
#liður_1
svar = ""
#Hér er while lykkja sem heldur áfram að ganga þar til svar verður eh annað en "J" eða "j"
while svar == "J" or svar == "j":
    tala = int(input("Vinsamlegast sláðu inn heiltölu:"))
    print("Talan sem þú hefur valið er", tala)
    svar = input("Viltu velja aðra tölU(J/N)?: ")

#liður_2
svar = "j"
print("Hér reiknar foritið flatarmál ferhyrnings")
#Hér er while lykkja sem heldur áfram að ganga þar til svar verður eh annað en "J" eða "j"
while svar == "j" or svar == "j":
    l = int(input("Sláðu inn lengd ferhyrningsins: "))
    b = int(input("Sláðu inn breidd ferhyrningsins: "))
    #Jafna flatarmál
    f = l * b
    print("Flatarmál ferhyrningsins er", f)
    svar = input("Viltu velja aðrar stærðir(J/N)?: ")

#liður_3
leyniord = ""
#Hér er while lykkja sem heldur áfram að keyrast þar til leyniord verður "lest"
while leyniord != "lest":
    leyniord = input("Sláðu inn leyniorðið: ")
    if leyniord != "lest":
        print("Villa kom upp! Rangt leyniorð.")
    else:
        break
print("Rétt! velkominn lengra í gegnum foritið")

#liður_4
#Hér er jafna fyrir upphæð af krónum sem deilir sig niður í stærstu mögulega gjaldeyri og heldur áfram með afganginn
kronur = int(input("Hvað ertu með margar krónur?"))
fimmthusund_sedlar = kronur // 5000
kronur = kronur % 5000
eittthusund_sedlar = kronur // 1000
kronur = kronur % 1000
fimmhundrud_sedlar = kronur // 500
kronur = kronur % 500
eitthundrad_peningar = kronur // 100
kronur = kronur % 100
fimmtiukronu_peningar = kronur // 50
kronur = kronur % 50
tiukronu_peningar = kronur // 10
kronur = kronur % 10
fimmkronu_peningar = kronur // 5
kronur = kronur % 5
print("Þetta gerir: ")
#Hér er fullt af if setningum sem bannar foritinu að prenta tiltekið gljadeyri ef það er = 0
if fimmthusund_sedlar != 0:
    print(fimmthusund_sedlar, "stk fimmþúsund krónu seðla")
if eittthusund_sedlar != 0:
    print(eittthusund_sedlar, "stk eittþúsund krónu seðla,")
if fimmhundrud_sedlar != 0:
    print(fimmhundrud_sedlar, "stk fimmhundruð krónu seðla,")
if eitthundrad_peningar != 0:
    print(eitthundrad_peningar, "stk hundraðkrónu skyldinga")
if fimmtiukronu_peningar != 0:
    print(fimmtiukronu_peningar, "stk fimmtíukrónu skyldinga")
if tiukronu_peningar != 0:
    print(tiukronu_peningar, "stk tíukrónu skyldinga")
if fimmkronu_peningar != 0:
    print(fimmkronu_peningar, "stk fimmkrónu skyldinga")
if kronur != 0:
    print(kronur, "stk einakrónu skyldinga")
else:
    print("Villa komu upp! þú hefur ekki slegið inn rétt.")

#liður_5
keyrsla = 0
#Hér er while lykkja sem er alltaf á fyrr en slökkt er á foritnu
on = True
while on:
    #Jafna sem reiknar hve oft foritið verður keyrt
    keyrsla = keyrsla + 1
    print()
    print("1. Finna summu og meðaltal 10 talna")
    print("2. Finna út hvort tala sé jöfntala eða oddatala")
    print("3. Hætta")
    svar = input("Veldu möguleika: ")
    print()
    if svar == "1":
        print()
        tala_1 = int(input("Sláðu inn fyrstu töluna hér: "))
        tala_2 = int(input("Sláðu inn aðra töluna hér: "))
        tala_3 = int(input("Sláðu inn þriðju töluna hér: "))
        tala_4 = int(input("Sláðu inn fjórðu töluna hér: "))
        tala_5 = int(input("Sláðu inn fimmtu töluna hér: "))
        tala_6 = int(input("Sláðu inn sjöttu töluna hér: "))
        tala_7 = int(input("Sláðu inn sjöundi töluna hér: "))
        tala_8 = int(input("Sláðu inn áttundu töluna hér: "))
        tala_9 = int(input("Sláðu inn níundu töluna hér: "))
        tala_10 = int(input("Sláðu inn tíundu töluna hér: "))
        summa = tala_1 + tala_2 + tala_3 + tala_4 + tala_5 + tala_6 + tala_7 + tala_8 + tala_9 + tala_10
        medaltal = summa / 10
        print()
        print("Summa talnana er",summa)
        print("Meðaltal talnanan er",medaltal)
        print()
    elif svar == "2":
        print()
        tala = int(input("Sláðu inn tölu"))
        deiling = tala // 2
        if tala % 2 != 0:
            print("Talan er oddatala")
        else:
            print("Talan er slétttala")
        print()
    elif svar == "3":
        print()
        teljari = 0
        #While lykkja sem prentar út setningu 10 sinnum
        while teljari < 10:
            teljari = teljari + 1
            print("Ég er frábær foritari")
        print("Foritið var keyrt",keyrsla,"sinnum.")
        quit()
    else:
        print()
        print("Þú hefur ekki valið rétt")
        print()