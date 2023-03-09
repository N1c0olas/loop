#armazena um numero pequeno
maior_numero = 999999

#entra com o primeiro numero
number = int(input("Entre com um numero ou digite -1 parar:"))

#se o numero não for igual a -' continua
while number != -1:  #!= igual a 'diferente'
    # o numero é maior que o maior_numero.
    if number > maior_numero:
        #Sim, atualiza maior_numero.
        maior_numero = number
        #entre com o proximo numero.
    number = int(input("Entre com um numero ou digite -1 para parar: "))

#imprime o maior numero
print("O maior numro é: "), maior_numero