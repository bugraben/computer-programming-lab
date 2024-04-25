d = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

tum_satirlar = [satir.split() for satir in d.split('\n')][1:-1]
toplam = 0

print(tum_satirlar)
for i, satir in enumerate(tum_satirlar):
    print(i, satir)

def sum_max_per_line(tum_satirlar):
    flag = 0
    toplam = 0

    for satir in tum_satirlar:
        if flag > 0:
            satir = satir[flag-1: flag+2]
        else:
            satir = satir[flag: flag+2]
        satir = [int(eleman) for eleman in satir]
        secilen_sayi = max(satir)
        toplam += secilen_sayi
        flag = satir.index(secilen_sayi)

    print(toplam)


def sum_min_per_line(tum_satirlar):
    flag = 0
    toplam = 0

    for satir in tum_satirlar:
        if flag > 0:
            satir = satir[flag - 1: flag + 2]
        else:
            satir = satir[flag: flag + 2]
        satir = [int(eleman) for eleman in satir]
        secilen_sayi = min(satir)
        toplam += secilen_sayi
        flag = satir.index(secilen_sayi)

    print(toplam)

def sum_bizarre(satirlar):
    flag = 0
    toplam = 0

    for i, satir in enumerate(tum_satirlar):
        if flag > 0:
            satir = satir[flag - 1: flag + 2]
        else:
            satir = satir[flag: flag + 2]
        satir = [int(eleman) for eleman in satir]
        if i % 2:
            secilen_sayi = max(satir)
        else:
            secilen_sayi = min(satir)
        toplam += secilen_sayi
        flag = satir.index(secilen_sayi)

    print(toplam)






sum_max_per_line(tum_satirlar)

sum_min_per_line(tum_satirlar)

sum_bizarre(tum_satirlar)




