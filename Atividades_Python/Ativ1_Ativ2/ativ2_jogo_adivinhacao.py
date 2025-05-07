numero_secreto= 7
tentativas= 0
contagem_tentativas= 0
print ("Bem-vindo ao jogo de adivinhação!")
print ("Tente adivinhar o número secreto entre 1 e 10.")
while tentativas !=7:
    numero= int(input("Digite um número: "))
    contagem_tentativas = contagem_tentativas +1
    if numero== numero_secreto:
        print ("Parabéns! Você adivinhou o número secreto.")
        print (f"Você precisou de {contagem_tentativas} tentativas.")
        break
    elif numero<numero_secreto:
        print ("O número secreto é maior.")
    else:
        print ("O número secreto é menor.")