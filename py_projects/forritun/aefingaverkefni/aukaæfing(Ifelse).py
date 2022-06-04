#Alexander_Máni_Einarsson
#12/09/19
#aukaverkefni_(ifelse)

#liður_1_hundaar
print()
print("Þetta forit reiknar út hve gamall þú ert í hundsárum")
ar = float(input("Hve gamall ert þú"))
if ar < 21 and ar > -1:
    ar = ar / 10
    print("Þú ert", ar, "ára í hundsárum")
elif ar > 2:
    ar = ar - 20
    ar = ar / 4
    ar = ar + 2
    print("Þú ert", ar, "ára í hundsárum")
else:
    print("Þetta er ekki réttur aldur")
print()

#liður_2_serhljodi_eda_samhljodi
print()
print("þetta forit segir þér hvort þú hefur slegið inn samhljóað eða sérhljóða")
print("Ath þetta virkar bara fyrir enska stafarófið!")
stafur = input("Sláðu inn staf")
if stafur == "a" or stafur == "e" or stafur == "i" or stafur == "o" or stafur == "u":
    print(stafur,", er sérhljóði")
elif stafur == "y":
    print(stafur,", gæti verið sérhljóði og samhljóði")
else:
    print("þetta er samhljóði")
print()

#liður_3_vikulaun
print()
print("Þetta forit reiknar út launseðil viðkomandi")
nafn = input("Sláðu inn nafn: ")
kt = input("Sláður inn kennitölu: ")
timi = int(input("Sláðu inn vinnutíman þinn námundað upp að klst fyrir síðustu viku: "))
if timi > 60:
    extra_vinna = timi - 60
    extra_laun = extra_vinna * 1200 * 2
    yfir_vinna = 20
    yfir_laun = yfir_vinna * 1200 * 1.5
    dag_vinna = 40
    dag_laun = dag_vinna * 1200
    heildar_laun = dag_laun + yfir_laun + extra_laun
elif timi < 61 and timi > 40:
    yfir_vinna = timi - 40
    yfir_laun = yfir_vinna * 1200 * 1.5
    dag_vinna = 40
    dag_laun = dag_vinna * 1200
    heildar_laun = dag_laun + yfir_laun
elif timi < 41:
    dag_vinna = timi
    dag_laun = timi * 1200
    heildar_laun = dag_laun


print(nafn,"kt:",kt)
print("Heildarlaun þín fyrir vikuna eru: ",heildar_laun," kr")
print("Þú ert með", dag_vinna,"tíma í dagvinnu sem gera: ", dag_laun," kr")
print("Þú ert með", yfir_vinna,"tíma í yfirvinnu sem gera: ", yfir_laun," kr")
print("Þú ert með", extra_vinna,"tíma í extra álagi sem gera: ", extra_laun," kr")