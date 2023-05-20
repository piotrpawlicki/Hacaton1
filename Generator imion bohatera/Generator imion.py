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