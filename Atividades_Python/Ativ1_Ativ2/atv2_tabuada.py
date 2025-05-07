numero = int(input("Digite um número: "))

for i in range(11):  # vai de 0 até 10
    #in range sigifica que o loop vai de 0 até 10, ou seja, 11 números
    #range = intervalo
    #in range = dentro do intervalo
    # para cada i dentro do intervalo de 0 a 10 faça:
    # i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(f"{numero} x {i} = {numero * i}")
