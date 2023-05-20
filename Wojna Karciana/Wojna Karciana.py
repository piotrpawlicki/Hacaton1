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
    karta_bota = random.choice(list(talia_bota.keys()))
    return karta_bota

def wybor_bota_bot_drugi(karta_gracza,talia_gracza, talia_bota):
      moc_gracza = wartosc_karty(karta_gracza, talia_gracza)
      print(talia_bota)
      print(talia_gracza)
      moc_bota, karta_bota = min(talia_bota.items(), key=lambda x:(x[1] > moc_gracza, x[1]))
      return {karta_bota, moc_bota}
def wartosc_karty(karta, talia):
    if karta in talia:
        val = talia[karta]
    return val

def porownaj_karty(moc_gracza, moc_bota):
    if moc_gracza > moc_bota:
        return 'Gracz'
    elif moc_bota > moc_gracza:
        return 'Bot'
    else:
        return 'Remnis'


talia = Talia_kart() #talia jest słownikiem
gracz_talia, bot_talia = (Przypisz_Karty(talia))  #karty bota i gracza to również słowniki
karta_gracza = wybor_gracza(gracz_talia) # gracz wybiera kartę ze swojej talii

a = wybor_bota_bot_drugi(karta_gracza, gracz_talia, bot_talia)
print(a)

