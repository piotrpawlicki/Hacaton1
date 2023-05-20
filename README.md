# Hackaton 1
> Opis realizowanych zadań podczas zajęć z dnia 20.05.2023

## Spis treści
* [Podsumowanie](#Podsumowanie)
  * [Wisielec](#Wisielec)
  * [Generator_imion_Bohatera](#Generator imion Bohatera)
  
* [Wykorzystane_technologie](#Wykorzystane technologie)
* [Podziękowania](#Podziękowania)
* [Autor](#Autor)


## Podsumowanie
- Zaimplementowano następujace zadania:
  - ### **Wisielec**
  ````
    import random
    GUESSING_WORDS = (
        "adam",
        "bank",
        "czar",
        "dama",
        "elita",
        "fanka",
        "grosz",
        "hobby",
        "idea",
        "jacht",
        "kawa",
        "lampa",
        "mama",
        "niska",
        "okno",
        "panda",
        "rabat",
        "samba",
        "tango",
        "ulica",
        "veto",
        "warta",
        "xerox",
        "yacht",
        "zakop",
        "balkon",
        "czas",
        "dywan",
        "ekran",
        "futro",
        "garaz",
        "haslo",
        "ilustracja",
        "jablko",
        "kanapa",
        "latarka",
        "maska",
        "niedzwiedz",
        "okulary",
        "pilot",
        "rakietka",
        "siekiera",
        "traktor",
        "uniform",
        "wazon",
        "xylofon",
        "yeti",
        "zamek",
        "konik",
        "lampa"
    )
    
    ##konwersja słowa na listę
    def create_list(word):
        return list(word)
    
    ##konwersja wybranego słowa na podkreślenia
    def convert_word(word):
        a = list('X' * len(word))
        return a
    
    ##wyświetlanie prawidłowe
    def display(word_list):
        return ' '.join(word_list)
    
    ##wybór słowa z listy słów
    def select_word(word_list):
        a = len(word_list)
        b = random.randint(0 , a-1)
        result = word_list[b]
        return result
    
    ## user input
    def user_input(bot_world):
        while True:
            a = input("Podaj literę: ")
            if len(a) == 1 and a.isalpha():
                break
            elif a.upper() == bot_world.upper():
                break
            else:
                print('Błąd typu. Podaj literę.')
        return a.upper()
    ##sprawdzenie czy litera jest w słowie
    def check_input(UserInput, word_list):
        indexes = []
        for i in range(len(word_list)):
            if word_list[i] == UserInput:
                indexes.append(i)
        return indexes
    
    
    ##podmienienie znaku w liście
    def change_char(guess_list, indeks, user_input):
        guess_list[indeks] = user_input
    
    def check_results(list1, list2):  ##sprawdzenie czy lista ze słowem zgadywanym jest taka sama jak lista ze słowem od usera
        if list1 == list2:
            return True
        else:
            return False
    
    def hangman(number):
        hangman = [
            '''
               +---+
                   |
                   |
                   |
                   |
                   |
            =======''',
            '''
               +---+
               |   |
                   |
                   |
                   |
                   |
            =======''',
            '''
               +---+
               |   |
               O   |
                   |
                   |
                   |
            =======''',
            '''
               +---+
               |   |
               O   |
               |   |
                   |
                   |
            =======''',
            '''
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
            =======''',
            '''
               +---+
               |   |
               O   |
              /|\  |
                   |
                   |
            =======''',
            '''
               +---+
               |   |
               O   |
              /|\  |
              /    |
                   |
            =======''',
            '''
               +---+
               |   |
               O   |
              /|\  |
              / \  |
                   |
            ======='''
        ]
    
        return hangman[number]
    
    
    def main():
        guess_number = 0
        guess_word = select_word(GUESSING_WORDS).upper()
        guess_word_list = create_list(guess_word)
        hidden_word_list = convert_word(guess_word)
    
        while not check_results(guess_word_list, hidden_word_list):
            print(hangman(guess_number))
            if guess_number == 7:
                break
            else:
                user_char = user_input(guess_word)
                result = check_input(user_char, guess_word_list)
                if user_char != guess_word :
                    if result:
                        for i in result:
                            change_char(hidden_word_list, i , user_char)
                    else:
                        print('Spróbuj jeszcze raz')
                        guess_number += 1
                        print(f'To była Twoja próba numrer {guess_number}')
                elif user_char == guess_word: ##wprowadzenie możliwości podania całego hasła
                    guess_word_list = hidden_word_list
                    break
            print(display(hidden_word_list))
    
        if check_results(guess_word_list, hidden_word_list):
            print('Gratuluję, wygrałeś!')
        else:
            print(f'Wisisz, koleżko. Miałeś odgadnąć słowo {guess_word}')
    
    main()````
  
Gra pozwala na odgadnięcie słowa wylosowanego z listy "GUESSING_WORDS"
Mamy 7 prób - tyle prób przewidziano na wyrysowanie całego wisielca. User ma możliwość odgadnicia całego słowa wcześniej. Enjoy


  - ### **Generator imion Bohatera**
````
    import random

    #lista samogłosek
    VOWELS = [ 'a', 'e', 'u', 'y', 'i']
    #lista spółgłosek
    CONNSONERS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',  'p', 'r', 's',  't', 'w' ]
    ALL_LETTERS = VOWELS + CONNSONERS
    #lista przydomków
    NICKNAMES = ['Ponury',
    'Najeźdźca',
    'Szczerbaty',
    'Krótki',
    'Kulawy',
    'Ostrzyżony',
    'Mocarz',
    'Sęp',
    'Zawzięty',
    'Smoczy',
    'Hufcowy',
    'Waleczny',
    'Zwinny',
    'Rżący',
    'Kulawy',
    'Zuchwały',
    'Rozszalały',
    'Strachliwy',
    'Dzielny',
    'Wspaniały']
    
    def convert_to_roman(number):
        roman = ""
        numbers = [10, 9, 5, 4, 1]
        symbols = ['X', 'IX', 'V', 'IV', 'I']
        i = 0
        while number > 0:
            if number >= numbers[i]:
                roman += symbols[i]
                number -= numbers[i]
            else:
                i += 1
        return roman
    
    def create_name():
        name = ''
        name += random.choice(ALL_LETTERS).upper()
        max = random.randint(3,5)
        for i in range(1,max):
            name += random.choice(VOWELS)
            name += random.choice(CONNSONERS)
        return name
    
    def main():
        first_part = create_name()
        numeral = convert_to_roman(random.randint(1,39))
        nickname = random.choice(NICKNAMES)
        user_name = first_part + ' ' + numeral + ' ' + nickname
        print(user_name)
    
    
    main()
 ````
Program generuje imię bohatera gry RPG. Do wygenerowanego imienia dodaje liczebnik w postaci cyfry rzymskiej (od 1 do 39) oraz przydomek

 - ### **Wojna karciana**
 - ````
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









   ````
   
Program pozwala na grę w wojnę. Karta użyta zostaje wyrzucona. Wynik to liczba wygranych rund. Może zaczynać komputer lub user.
## Wykorzystane technologie
- Python 3.9.13
- PyCharm 2023.1


## Podziękowania

- Instrukcje do zadań zostały przedstawione na https://github.com/ritaly/CODEME-python23/tree/main/hackaton_01
- Many thanks to StackOverFlow and chat.openai.com :)


## Autor
Created by Piotr Pawlicki (piotr.a.pawlicki@gmail.com)
