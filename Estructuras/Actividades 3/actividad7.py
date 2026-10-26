letras = {}
palabra = input("Dime palabra").lower().strip()

for letra in palabra: 
    if letra not in letras:
        letras[letra] = palabra.count(letra)

print(letras)