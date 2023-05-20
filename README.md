# Hackaton 1
> Opis realizowanych zadań podczas zajęć z dnia 20.05.2023

## Spis treści
* [Podsumowanie](#Podsumowanie)
  * [Wisielec](Wisielec)
  * [Generator imion Bohatera](Generator imion Bohatera)
* [Wykorzystane technologie](#Wykorzystane technologie)
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


## Wykorzystane technologie
- Python 3.9.13
- PyCharm 2023.1


## Podziękowania

- Instrukcje do zadań zostały przedstawione na https://github.com/ritaly/CODEME-python23/tree/main/hackaton_01
- Many thanks to StackOverFlow and chat.openai.com :)


## Autor
Created by Piotr Pawlicki (piotr.a.pawlicki@gmail.com)
