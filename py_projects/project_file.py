#Alexander_Máni_Einarsson
#16/09/19
#hlutapróf_1

#Lidur 1
print()
print("Þetta forit segir þér hver langt þú ert frá 2 metrum.")
nafn = input("Hvað heitir þú?: ")
haed_m = float(input("Hve stór ert þú í metrum?: "))
haed_cm = haed_m * 100
if haed_cm < 200:
    vontunn = 200 - haed_cm
    print("Góðan daginn", nafn, ",þú ert", vontunn,"cm frá því að vera tveir metrar")
elif haed_cm > 200:
    vontunn = haed_cm - 200
    print("Góðan daginn", nafn, ",Þú ert", vontunn,"cm stærri en tveir metrar")
elif haed_cm == 200:
    print("Góðan daginn", nafn, ",Þú ert akkúrat tveir metrar")

else:
    print("Þú hefur ekki slegið inn rétt, vinsamlegast reyndu aftur")


#lidur 2
print()
print("Þetta forit tekur við stigafjölda liðs úr körfuboltaleik")
stig = int(input("Skráðu stig liðsins: "))
if stig < 26 and stig > -1:
    print("Úpss þetta hefur ekki endað vel")
elif stig > 25 and stig < 51:
    print("Þetta hefur gengið vel")
elif stig > 49 and stig < 81:
    print("Geggjað vel gert")
elif stig > 80 and stig < 101:
    print("")
else:
    print("Kjaftæði er þetta-þú þarft að vand innsláttinn")

#lidur 3
print()
print("Beðið verður um þrjár tölur og dregið síðustu töluna frá summu fyrstu tveggja talnana og svar síðan birt.")
tala_1 = int(input("Sláðu inn fyrstu töluna: "))
tala_2 = int(input("Sláðu inn aðra töluna: "))
tala_3 = int(input("Sláðu inn þriðju töluna: "))
svar = (tala_1 + tala_2) - tala_3
print("svarið er: (",tala_1,"+",tala_2,") -",tala_3,"=",svar)

#lidur 4
print()
print("Nonni kaupir buxur á 17.735kr.")
verd = 17735
fimmthusund = verd // 5000
afgangur = verd % 5000
thusund = afgangur // 1000
afgangur = afgangur % 1000
fimmhundrad = afgangur // 500
afgangur = afgangur % 500
hundrad = afgangur // 100
afgangur = afgangur % 100
fimmtiu = afgangur // 50
afgangur = afgangur % 50
print("Nonni þarf", fimmthusund,"fimmþúsund krónu seðla,", thusund,"þúsund krónu seðla,", fimmhundrad,"fimmhundrað krónu seðla,", hundrad,"hundrað krónu peninga,", fimmtiu,"fimmtíu krónu peninga og", afgangur,"Krónur")




