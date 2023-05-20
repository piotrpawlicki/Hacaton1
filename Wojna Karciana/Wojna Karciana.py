import random

GAME_RANGE = ['B','b','G','g']
def Talia_kart():
    figury = {'AS': 12, 'KRÓL': 11, 'DAMA': 10, 'WALET': 9, '10': 8, '9': 7, '8': 6,'7': 5,'6': 4, '5':3, '4': 2, '3': 1, '2': 0}
    kolory = ['KARO', 'KIER', 'PIK', 'TREFL']
    talia = {}

    for kolor in kolory:
        for figura, wartosc in figury.items():
            figura_n = figura + ' ' + kolor
            wartosc_n = wartosc
            talia[figura_n] = wartosc_n
    return talia


def Przypisz_Karty(talia):
    gracz = {}
    gracz_temp = []
    bot = {}
    bot_temp = []
    talia_temp = list(talia.keys())
    random.shuffle(talia_temp)
    for i in range(0,10):
        gracz_temp.append(talia_temp[i])
    for i in gracz_temp:
        if i in talia:
            gracz[i] = talia[i]
    for i in range(11,21):
        bot_temp.append(talia_temp[i])
    for i in bot_temp:
        if i in talia:
            bot[i] = talia[i]
    return gracz, bot


def sortuj_talie(talia):
    a = dict(sorted(talia.items(), key=lambda x: x[1], reverse=True))
    return a

def wybor_gracza(gracz_talia):
    gracz_talia_disp = list(sortuj_talie(gracz_talia))
    print(gracz_talia_disp)
    karta_gracza = input(f'\nWybierz kartę z talii: ').upper()

    while karta_gracza not in gracz_talia:
        print(f'Nie masz takiej karty\n')
        karta_gracza = input(f'\nWybierz kartę z talii: ').upper()
    moc_gracza = wartosc_karty(karta_gracza, gracz_talia)
    return {karta_gracza : moc_gracza}

##wybor bota dla gry gdy bot zaczyna
def wybor_bota_bot_pierwszy(talia_bota):
    losowa_karta = random.choice(list(talia_bota.keys()))
    losowa_moc = talia_bota[losowa_karta]
    karta_bota = {losowa_karta : losowa_moc}
    return karta_bota

def wybor_bota_bot_drugi(karta_gracza,talia_gracza, talia_bota):
        moc_bota = 0
        #moc_gracza = wartosc_karty(karta_gracza, talia_gracza)
        moc_gracza = list(karta_gracza.values())[0]
        if moc_gracza > max(talia_bota.values()):
            moc_bota = min(talia_bota.values())
        ##elif moc_gracza == max(talia_bota.values()):
          ##  print('remis')
        else:
            ##znajdź ta karty które są większe, posortuj i wywal najmniejszą
            for elem in talia_bota.values():
                if elem > moc_gracza:
                    if elem < moc_bota or moc_bota ==0:
                        moc_bota = elem #moc_bota to klucz
        karta_bota = znajdz_klucz(talia_bota,moc_bota)
        return {karta_bota: moc_bota}

def wartosc_karty(karta, talia):
    if karta in talia:
        val = talia[karta]
        return val
    else:
        return None

def znajdz_klucz(slownik, wartosc):
    for klucz, wart in slownik.items():
        if wart == wartosc:
            return klucz
    return None


def porownaj_karty(moc_gracza, moc_bota):
    if moc_gracza > moc_bota:
        return 'Gracz wygrał'
    elif moc_bota> moc_gracza:
        return 'Bot wygrał'

def usun_karte(talia, karta):
    for key in karta.keys():
        del talia[key]
    return talia

def dodaj_karte(karta_przeciwnika, talia):
    talia.update(karta_przeciwnika)

def start_gry():
    x = input('Kto zaczyna grę Gracz (G) czy Bot (B)? : ')
    while x not in GAME_RANGE:
        x = input('Zły input! Kto zaczyna grę Gracz (G) czy Bot (B)? : ')
    return x
def main():

    talia = Talia_kart() #talia jest słownikiem
    gracz_talia, bot_talia = (Przypisz_Karty(talia))  #karty bota i gracza to również słowniki - tasowanie kart i ich rozdanie
    start = start_gry().upper()
    wynik_gracza = 0
    wynik_bota = 0
    if start == 'G':
        while len(gracz_talia) > 0 and len(bot_talia) > 0:
            gracz_karta = wybor_gracza(gracz_talia)
            print(f'Gracz wybrał kartę {gracz_karta}')
            bot_karta = wybor_bota_bot_drugi(gracz_karta, gracz_talia, bot_talia )
            print(f'Bot wybrał kartę {bot_karta}')

            moc_gracza = list(gracz_karta.values())[0] ##wartosc_karty(gracz_karta, talia)
            moc_bota = list(bot_karta.values())[0]
            wynik = porownaj_karty(moc_gracza, moc_bota)
            print(wynik)
            ##
            if wynik == 'Gracz wygrał' :
                wynik_gracza +=1
                usun_karte(gracz_talia,gracz_karta)
                usun_karte(bot_talia, bot_karta)
                ##usun_karte(list(bot_karta.keys())[0], bot_talia)
            elif wynik == 'Bot wygrał':
                wynik_bota += 1
                usun_karte(gracz_talia, gracz_karta)
                usun_karte(bot_talia, bot_karta)

    else:
        while len(gracz_talia) > 0 and len(bot_talia) > 0:
            bot_karta = wybor_bota_bot_pierwszy(bot_talia)
            print(f'Bot wybrał kartę {bot_karta}')
            gracz_karta = wybor_gracza(gracz_talia)
            print(f'Gracz wybrał kartę {gracz_karta}')
            moc_gracza = list(gracz_karta.values())[0]
            moc_bota = list(bot_karta.values())[0]
            wynik = porownaj_karty(moc_gracza, moc_bota)
            print(wynik)
            if wynik == 'Gracz wygrał':
                wynik_gracza += 1
                usun_karte(gracz_talia, gracz_karta)
                usun_karte(bot_talia, bot_karta)
                ##usun_karte(list(bot_karta.keys())[0], bot_talia)
            elif wynik == 'Bot wygrał':
                wynik_bota += 1
                usun_karte(gracz_talia, gracz_karta)
                usun_karte(bot_talia, bot_karta)

        if wynik_bota > wynik_gracza:
            print('Wojnę wygrał bot')
        elif wynik_gracza > wynik_bota:
            print('Wojnę wygrał gracz')
        else:
            print('padł remis')

main()








