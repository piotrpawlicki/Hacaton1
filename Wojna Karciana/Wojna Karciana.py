import random
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
        print(gracz_talia_disp)
        karta_gracza = input(f'\nWybierz kartę z talii: ').upper()
    return karta_gracza

##wybor bota dla gry gdy bot zaczyna
def wybor_bota_bot_pierwszy(talia_bota):
    karta_bota = random.choice(talia_bota)
    return karta_bota

def wybor_bota_bot_drugi(karta_gracza,talia_gracza, talia_bota):
    moc_gracza = wartosc_karty(karta_gracza, talia_gracza)
    karty_bota_moc = sorted(talia_bota.keys())
    for i in karty_bota_moc:
        if i > moc_gracza:
            wybor_bota =  i


def wartosc_karty(karta, talia):
    if karta in talia:
        wartosc = talia[karta]
    return wartosc

def porownaj_karty(moc_gracza, moc_bota):
    if moc_gracza > moc_bota:
        return 'Gracz'
    else:
        return 'Bot'

talia = Talia_kart() #talia jest słownikiem
gracz_talia, bot_talia = (Przypisz_Karty(talia))  #karty bota i gracza to również słowniki
##print(gracz_talia)
karta_gracza = wybor_gracza(gracz_talia) # gracz wybiera kartę ze swojej talii
moc_gracza = wartosc_karty(karta_gracza, gracz_talia)

karta_bota = wybor_bota_bot_pierwszy(bot_talia)
moc_bota = wartosc_karty(karta_bota, bot_talia)
wynik = porownaj_karty(moc_gracza, moc_bota)

print(f'Gracz wybrał {karta_gracza}, a komputer {karta_bota}. Wygrał {wynik}')