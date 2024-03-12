def solver(a, b, c):
    if a == 0:
        return None
    return (c-b)/a


solver(3, 2, 8)


def mean_art_hrm(a, b, c):
    mean_arithmetic = (a + b + c) / 3
    mean_harmonic = 3 / (1/a + 1/b + 1/c)
    return (mean_arithmetic, mean_harmonic)


arithm, harm = mean_art_hrm(2, 4, 6)


def surface(a, b, c):
    return 2 * (a*b + b*c + c*a)


surface(2, 2, 2)


def convert_f_to_c(fahrenheit):
    return (fahrenheit-32) / 1.8

convert_f_to_c(50.2)

def convert_c_to_f(celsius):
    return celsius * 1.8 + 32


convert_c_to_f(50.2)


def prim_hesapla(T, P):
    return T * P


def salary(hours, wage):
    print('Brut', wage * hours, '\n'
          'Net', wage * hours * 0.85)


salary(8, 69)


def diameter_to_perimeter(d):
    pi = 22/7
    return d * pi



# Bir inşaat de çalışan Ayhan ve Mustafa isimlerindeki karo ustaları saatte K1 ve K2 sayıda karo
# döşemektedirler. Birlikte çalıştıkları zaman N tane karoyu kaç saatte döşediklerini hesaplayan
# bir program yazınız.

def karo_time(K1, K2, N):
    return N / (K1 + K2)



# Bir futbol takımı yeni transfer ettiği oyuncu için 3 yıllık sözleşme karşılığı N lira ödeme yapacaktır.
# Ödemenin yüzde olarak Y1 oranındaki miktarı ilk yıl, Y2 oranındaki miktarı ikinci yıl ve kalanı üçüncü yıl
# yapılacaktır. Futbolcuya her yıl ödenecek para miktarını hesaplayan bir program yazınız.


def contract(N, Y1, Y2):

    print(f'Toplam Para {N} \n'
          f'Birinci Yil {N * Y1/100} \n'
          f'Ikinci Yil {N * Y2/100} \n'
          f'Ucuncu Yil {N * (100 - Y1 - Y2)/100} \n')


contract(1000, 10, 20)



while __name__ == '__main__':
    inp = input('$')
    if inp != '':
        print(eval(inp))


# Kullanıcıdan üç kenar uzunluğunu girmesini isteyen ve bu uzunlukların bir üçgen
# belirtip belirtmediğini gösteren, belirtiyor ise üçgenin türünü belirleyen bir program yazınız.
# Üçgen kuralı: a,b,c kenar uzunlukları olmak üzere: “a+b > c ve a+c > b ve b+c > a” koşulu
# sağlanmalı.

def isTriangle(a, b, c):
    if ((a+b) > c) and ((a+c) > b) and ((b+c) > a):
        return True
    return False


print(isTriangle(3, 4, 7))


# Kullanıcıdan 3 farklı sayı girmesini isteyen ve bu sayıların en büyüğünü ekrana
# yazdıran bir program yazınız.

def bMax(a, b, c):
    return (max(a, b, c))

def bMax2(a, b, c):
    ret = a
    if b > ret:
        ret = b
    if c > ret:
        ret = c
    return ret

def bMax3(a, b, c):
    return print(max(a, b, c))



print(bMax(1, 2, 3))
bMax2(1, 2, 4)


# Sıcaklığı input olarak alınız. Her bir bakteri için optimaldir ve optimal değildir çıktılarını alacak
# programı yazınız. Termometrenin ölçüm aralığı -20 ile +100 arasındadır. Bu değerler dışında
# bir değer girildiğinde uyarı mesajı versin. Bakteriler ve optimal yaşama sıcaklıkları aşağıda
# verilmiştir.
# Streptococcus thermophilus: 40–45 °C
# Lactobacillus acidophilus: 35-38°C
# Escherichia Coli: 35-40°C

optimalTemp = {'S. thermophilus': (40, 45),
               'L. acidophilus': (35, 38),
               'E. coli': (35, 40)}

def isOptimalTemp(temp, organism, table):
    if temp > -20 and temp < 100:
        if temp > table[organism][0] and temp < table[organism][1]:
            return True
        return False
    raise ValueError('temp argument must be in the range (-20, 100)')


isOptimalTemp(43, 'S. thermophilus', optimalTemp)


# Bir kıyafete verilen fiyata göre, indirim yapılıp yapılmayacağını belirleyen ve
# yapılacak ise indirimli fiyatı gösteren bir program yazınız. İndirim oranı ve indirim eşiği keyfi
# sayılardır.

def ok_for_discount(price, th, rate):
    if price > th:
        ret = price * (100-rate) / 100
        print(f'New Price {ret}')
        return ret
    print('Not suitable for discount')


ok_for_discount(1000, 900, 10)


# Sizden istenilen ondalıklı sayının kesirli ifadesini bulunuz ve bu sayının 1/10 birimlik
# aralıkta hangi iki kesir arasında olduğunu belirleyiniz.

from fractions import Fraction

def float_to_fraction(flt: float):
    flt_r = round(flt, 1)
    if flt < flt_r:
        return (Fraction(str(flt)), (Fraction(str(flt_r - 0.1)), Fraction(str(flt_r))))
    return (Fraction(str(flt)), (Fraction(str(flt_r)), Fraction(str(flt_r + 0.1))))


float_to_fraction(0.15)


# Aynı noktadan ters yönlerde harekete geçen iki aracın gittiği mesafeleri input olarak
# giriniz. (Doğu: negatif, Batı: pozitif olacak şekilde) Program hangi aracın daha fazla mesafe
# gittiğini versin.

def faster(negative, positive):
    if negative > positive:
        print('First is the fastest')
        return
    print('Second is the fastest')

def faster1(negative, positive):
    if -negative > positive:
        print('First is the fastest')
    else:
        print('Second is the fastest')


faster1(-100, 200)



# Kullanıcıdan istenen boy kilo bilgisi ile vücut kitle indeksini hesaplayınız. 18.5’ten
# küçük ise zayıf, 18.5 -25 arasında ise normal, 25 - 30 arasında ise kilolu 30’dan fazla ise
# obez olarak belirtiniz.
# vki = kilogram / metre^2
# örneğin : kg= 50, boy = 1.70 ise vki = 17.30

def calcBDI(mass, height):
    bdi = mass / (height * height)
    bdi_class = 'Normal'
    if bdi < 18.5:
        bdi_class = 'Thin'
    elif bdi > 30:
        bdi_class = 'Fat'
    return (bdi_class, bdi)


calcBDI(50, 1.70)

def isLeapYear(year):
    if year // 4 == year / 4:
        if year // 100 == year / 100:
            if year // 400 == year / 400:
                return True
    return False


isLeapYear(1992)


def canDivideByZero(number):
    if number // 6 == number / 6:
        return True
    return False


## HIZ TESTI

def func1(inp):
    ret = True
    if inp == False:
        ret = False
    return ret


def func2(inp):
    if inp == True:
        ret = True
    else:
        ret = False
    return ret


def func3(inp):
    if inp == True:
        ret = True
    elif inp == False:
        ret = False
    return ret



from timeit import Timer, timeit
import pandas as pd

t_func1_True = Timer(lambda: func1(True)).timeit()
t_func2_True = Timer(lambda: func2(True)).timeit()
t_func3_True = Timer(lambda: func3(True)).timeit()

t_func1_False = Timer(lambda: func1(False)).timeit()
t_func2_False = Timer(lambda: func2(False)).timeit()
t_func3_False = Timer(lambda: func3(False)).timeit()

