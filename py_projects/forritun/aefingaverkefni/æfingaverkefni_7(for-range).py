#Alexander_Máni_Einarsson
#03/10/19
#æfingaverkefni_7

#Dæmi 1
svar = "j"
while svar == "j" or svar == "J":
    tala_1 = int(input("sláðu inn tölu 1 hér: "))
    tala_2 = int(input("sláðu inn tölu 2 hér: "))
    fradrattur = tala_2 - tala_1
    fradrattur_1 = tala_1 - tala_2
    if fradrattur == 0 or fradrattur == 1 or fradrattur_1 == 1:
        print("Villa !, TÖlunar er u jafn háar eða önnur aðeins jafna há og hin")
        svar = "j"
    else:
        for tala in range(tala_1, tala_2):
            print("Talnaruna: "tala, end=" ")
        svar = "n"

#Dæmi 2
for tala in range(1, 100):
    deiling = tala // 2
    afgangur = tala % 2
    if afgangur != 0:
        print(tala, end=" ")



#Dæmi 3
summa = 0
for tala in range(1,16):
    summa = summa + tala
print(summa)

