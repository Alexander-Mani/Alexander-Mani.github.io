#Alexander_Máni_Einarsson
#03/09/19
#æfingaverkefni_3(heiltöludeiling)

#liður1
gradur = int(input("Sláðu inn gráður"))
hringur = gradur // 360
afgangs = gradur % 360
print("Þettar er", hringur, "hringur og", afgangs, "gráður")

#liður2
maettir = int(input("Hvað eru margir mættir á æfingu?"))
lid = maettir //7
varamenn = maettir % 7
print("þetta verða þá", lid, "lid og", varamenn, "varamenn")

#liður3
sek = int(input("sláðu inn fjölda sekæund"))
min = sek // 60
sek = sek % 60
klst = min // 60
min = min % 60
print("þetta eru þá", klst, "klukkustundir,", min, "mínútur og", sek, "sekúndur")

#liður4
mm = int(input("sláðu inn fjölda millimetra"))
cm = mm // 10
mm = mm % 10
m = cm // 100
cm = cm % 100
print("þetta eru þá", m, "metrar,", cm, "sentímetrar og", mm, "millimetrar")

#liður5
kronur = int(input("Hvað ertu með margar krónur?"))
eittthusund_sedlar = kronur // 1000
kronur = kronur % 1000
fimmhundrud_sedlar = kronur // 500
kronur = kronur % 500
eitthundrad_peningar = kronur //100
kronur = kronur % 100
print("Þetta gerir,", eittthusund_sedlar, "stk 1000 kr seðla,", fimmhundrud_sedlar, "stk 500kr seðla,", eitthundrad_peningar, "stk 100kr peninga og", kronur, "krónur.")

#liður6
tala = int(input("Sláður inn tölu"))
tala // 2
afgangs = tala % 2
if afgangs == 0:
    print("þetta er slétttala")
elif tala == 0:
    print("þetta er 0"")
else:
    print("þetta er oddatala")


