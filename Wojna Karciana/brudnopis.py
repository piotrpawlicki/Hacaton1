slownik_a = {'a': 1}
slownik_b = {'b': 2}

slownik_b.update(slownik_a)

print(slownik_b)

for klucz in slownik_a:
    if klucz in slownik_b:
        del slownik_b[klucz]
print(slownik_b)