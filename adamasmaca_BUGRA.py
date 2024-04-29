# BUGRA ISIKDEMIR

import random

## Diger bir cozum yolu
# kalan round sayisini harf sayisina esitleyip dogru cevaplarda round sayisini bir artirmak
# round sayisi bittiginde tum harfler acilmissa basarili

# degiskenleri globaldan locala cek

sozluk = ['ELMA', 'ARMUT', 'KAĞIT', 'KALEM']
kelime = random.choice(sozluk)
tahmin_edilen = list('_' * len(kelime))
game_over = 0 # 0 devam, 1 basarisiz, 2 basarili
guess_remaining = 6
wrong_list = []

def kontrol(harf):
    '''
    :param harf:
    :return: Boolean

    Kullanicidan alinan harfin kelime icinde yer alip almama durumunu kontrol eder. Tum harfler tahmin edilmisse
    game_over flagini 2 yapar.
    '''
    global game_over
    if len(harf) > 1:
        print('HATA: Tek harf giriniz.')
    elif harf in kelime:
        for i, char in enumerate(kelime):
            if harf == char:
                tahmin_edilen[i] = harf
                if ''.join(tahmin_edilen).isalpha():
                    game_over = 2
        print(f'Dogru Harf! {harf}')
        return True
    else:
        wrongAnswer(harf)
        return False


def wrongAnswer(inp):
    '''
    :param inp: string
    :return: None

    Hatali tahmin edilmis harfi yanlis tahmin edilenler listesine ekler, bir hakki azaltir, ekrana yanlis harf metni
    bastirir, tahmin hakki bitmisse game_over flagini 1'e cevirir.
    '''

    global wrong_list, guess_remaining, game_over
    if inp not in wrong_list:
        wrong_list.append(inp)
        guess_remaining -= 1
        print(f'Yanlis harf! {inp}')
    if guess_remaining == 0:
        game_over = 1

def refreshScreen():
    '''
    :return: None

    Ekrana arayuzu bastirir.
    '''

    print(f'''
        = = = = = = = = = = =
Tahmin edilen kelime: {tahmin_edilen}
Kalan tahmin hakki: {guess_remaining}
Kullanilmis harfler: {set(wrong_list)}
    ''', flush=True)

if __name__ == '__main__':
    while (game_over == 0):
        refreshScreen()
        harf = input('Bir harf tahmin edin: ').upper()
        kontrol(harf)

    print(('Oyun bitti, basaramadiniz.', 'Tebrikler, basardiniz.')[game_over - 1]) ##havali print
    print('Kelime:', kelime)
    print('Oyun Bitti')