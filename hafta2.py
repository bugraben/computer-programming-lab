# Soru 1 : Armstrong sayıları, sayıların rakamlarının küplerinin toplamı, sayının kendisine eşit olduğunda oluşur.
# Örneğin, 153 = 1^3 + 5^3 + 3^3 olduğu için bir Armstrong sayısıdır. 1-1000 aralığındaki Armstrong sayılarını bulun.

for i in range(1, 1001):
    sum_of_cubes = 0
    for j in str(i):
        sum_of_cubes += int(j) ** 3
    if i == sum_of_cubes:
        print(i)





# Soru 2 : Fibonacci serisini rekürsif olmayan bir yöntem kullanarak hesaplayın. Liste yapıları ve fonksiyon tanımı
# bulunmayan bir program yazınız.
# Fibonacci serisi, önceki iki terimin toplamıyla oluşturulan bir seridir: 0, 1, 1, 2, 3, 5, 8, 13, …

i = 0
j = 1
for k in range(10):
    print(i, j, end=' ')
    i = i + j
    j = i + j




# Soru 3 : İki farklı organizmanın DNA dizilerini karşılaştırarak benzerliklerini bulan bir program yazın.
# DNA dizileri, dizilmiş nükleotidlerden oluşur: adenin (A), timin (T), sitozin (C) ve guanin (G).
# Verilen iki DNA dizisinin herhangi bir konumdaki karakterleri karşılaştırılır ve eşleşme sayısı hesaplanır.
#
# Örneğin:
#
# Dizgi 1: "ATCGATCGATCG"
# Dizgi 2: "ATCGATAGCTAG"

seq1 = "ATCGATCGATCG"
seq2 = "ATCGATAGCTAG"
similarity = 0
for i in range(len(seq1)):
    if seq1[i] == seq2[i]:
        similarity += 1
print(similarity, similarity/len(seq1))


# Soru 4 : Verilen bir metindeki en uzun kelimeyi bulan bir program yazın.
# Kelimeler boşluklarla ayrılır ve noktalama işaretleri yok sayılır.

def longest(input_string:str):
    str_to_list = input_string.replace('.', '') \
                              .replace(',', '') \
                              .replace(':', '') \
                              .replace(';', '') \
                              .split(' ')
    list_with_len = [(len(i), i) for i in str_to_list]







# Soru 5: Verilen bir kimyasal formülün molar kütlesini hesaplayan bir program yazın.
# Kimyasal formüldeki her bir elementin atom ağırlıklarını kullanarak, formüldeki her bir
# elementin atomlarının toplam kütlesini hesaplayın ve bu değerleri toplayarak formülün
# molar kütle değerini elde edin.
#
# molar_kütle += element_agirliklari[element_sayisi] * int(element_sayisi)
#
# element_agirliklari = {
#     'H': 1.008,
#     'C': 12.011,
#     'O': 15.999,
#     'N': 14.007,
# }
#
# Örneğin:
#
# Giriş: H2O
# Çıkış: Molar kütle: 18.02 g/mol


mass_table = {'H': 1.008,
              'C': 12.011,
              'O': 15.999,
              'N': 14.007}

def molar_mass(molecule:str, table=mass_table):
    sum = 0
    for i in range(len(molecule) - 1, 0, -1):
        print(f'i: {i}')
        if molecule[i].isnumeric():
            sum += int(molecule[i]) * mass_table[molecule[i-1]]
            i -= 1
        elif molecule[i].isalpha():
            sum += mass_table[molecule[i]]
        else:
            raise ValueError
        print(f'Sum: {sum}')



molar_mass('H2O')


