#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
#.lower()

texto = input('Digite uma palavra ou uma frase: ')

maiuscula = 0    # variavel para guardar a quantidade de letras maiusculas
miniscula = 0   # variavel  para guardar a quantidade de letras miniscula
for letra in texto:
    if letra.islower():     #isLower = verifica se a letra e miniscula e entra na condição
        miniscula += 1
    elif letra.isupper():   #isMaiuscula = verifica se a letra e miniscula e entra na condição
        maiuscula += 1

print(f'O texto tem {maiuscula} letras maiuscula e {miniscula} minisculas')