entrada = input()

letras = {}

for letra in entrada:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1

impar = 0

for cont in letras.values():
    if (cont % 2 != 0):
        impar += 1

if impar > 1:
    print('FALSO')
else:
    print('VERDADEIRO')