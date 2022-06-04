#Alexander_Máni_Einarsson
#27/08/19
#Æfingaverkefni_1c(if else)

#liður 1
tala_1 = int(input("Sláðu inn tvær tölu. Fyrri töluna hér:"))
tala_2 = int(input("Seinni töluna hér:"))
if tala_1 < tala_2:
    print("Seinni talan er stærri en fyrri talan")
elif tala_1 > tala_2:
    print("Fyrri talan er stærri en seinni talan")
else:
    print("tölunar eru jafn stórar")

#liður 2
afram = input("Nú verður haldið í lið 2")
man = str(input("Sláðu inn mánuð,vinsamlegast skrifið fyrstu þrjá stafi mánaðarins í lágstöfum án kommustafa, takk fyrir."))


if man == str("jan"):
    print("1 mánuður ársins")
elif man == str("feb"):
    print("2 mánuður ársins")
elif man == str("mar"):
    print("3 mánuður ársins")
elif man == str("apr"):
    print("4 mánuður ársins")
elif man == str("mai"):
    print("5 mánuður ársins")
elif man == str("jun"):
    print("6 mánuður ársins")
elif man == str("jul"):
    print("7 mánuður ársins")
elif man == str("agu"):
    print("8 mánuður ársins")
elif man == str("sep"):
    print("9 mánuður ársins")
elif man == str("okt"):
    print("10 mánuður ársins")
elif man == str("nov"):
    print("11 mánuður ársins")
elif man == str("dec"):
    print("12 mánuður ársins")
else:
    print("Tölvan þekkir ekki þennan mánuð(ATH Þörf er á að rita einungis fyrstu þrjá stafi mánuðarins í lágstöfum án kommustafa)")

#liður 3
aldur = int(input("Hve gamall/gömul ert þú?"))
if aldur > -1 and aldur < 7:
    print("Nú, svo þú ferð að byrja í skóla?")
elif aldur > 6 and aldur < 16:
    svar = str(input("Ætlar þú í menntaskóla?(J/N)"))
    if svar == str("J") or svar == str("j"):
        print("Gangi þér vel í menntaskóla")
    elif svar == ("N") or svar == str("n"):
        print("Tölvan vill minna á að stúdentspróf er mikilvægt til upphækkunar í starfi, gangi þér að eingu síðu vel")
    else:
        print("þú hefur ekki valið rétt svar")
elif aldur > 15 and aldur < 106:
    print("Gangi þér vel í framtíðinni!")
else:
    print("Þú ert annað hvort fáranlega gamall/gömul eða hefur svarð vitlaust")

#liður 4


tala3 = int(input("Sláðu inn heila tölu á bilinu 0 til 25"))
if tala3 > -1 and tala3 < 26:
    tala4 = tala3*float(1.7)
    print("Talana þín margfölduð með tölunni 1,7 er:", tala4)
else:
    print("Þú hefur ekki slegið inn heiltölu á bilin 0 til 25")

#liður 5

svar2 = str(input("Viltu lesa brandara?(J/N)"))
if svar2 == str("J") or svar2 == str("j"):
    print("Ísland vann fleiri orustur en ítalía á 20 öldinni")
elif svar2 == str("N") or svar2 == str("n"):
    print("Allt í lagi, kannski seinna")
else:
    print("þú hefur ekki svarað eins og beðið var um")

