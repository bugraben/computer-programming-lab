WORD = 'MASKE'

## Diger bir cozum yolu
# kalan round sayisini harf sayisina esitleyip dogru cevaplarda round sayisini bir artirmak
# round sayisi bittiginde tum harfler acilmissa basarili



game_over = 0 # 0 devam, 1 basarisiz, 2 basarili
guess_remaining = 6
guessed_list = list('_' * len(WORD))
wrong_list = []

def declareWord():
    word = list(input('Tahmin edilecek kelimeyi giriniz: ').title())
    return


def getLetter():
    inp = input('Bir harf tahmin edin: ').upper()
    print()
    return inp

def checkLetter(inp):
    if len(inp) > 1:
        print('HATA: Tek harf giriniz.')
    elif inp in WORD:
        for i, l in enumerate(WORD):
            if inp == l:
                guessed_list[i] = inp
        print(f'Dogru Harf! {inp}')
        return True
    else:
        wrongAnswer(inp)
        return False


def wrongAnswer(inp):
    global wrong_list, guess_remaining, game_over
    if inp not in wrong_list:
        wrong_list.append(inp)
        guess_remaining -= 1
        print(f'Yanlis harf! {inp}')
    if guess_remaining == 0:
        game_over = 1
    return


def refreshScreen():
    print(f'''
        = = = = = = = = = = =
Tahmin edilen kelime: {guessed_list}
Kalan tahmin hakki: {guess_remaining}
Kullanilmis harfler: {set(wrong_list)}
    ''', flush=True)
    return


if __name__ == '__main__':
    while (game_over == 0):
        refreshScreen()
        letter = getLetter()
        checkLetter(letter)

    print('Oyun Bitti')