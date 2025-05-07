#Tipo de variáveis: int = inteiro, float = decimal, str = string, bool = booleano (True ou False)
# quando quisermos solicitar dados ao usuário, colocamos a estrutura input() e dentro do seu parênteses, colocamos a mensagem que queremos que apareça para o usuário. 
# Solicita os dados do usuário
nome = input("Digite seu nome: ") #na declaração de variáveis, não é necessário colocar o tipo da variável, o python já faz isso automaticamente
idade = int(input("Digite sua idade: ")) #o input já retorna uma string, então não é necessário colocar o tipo da variável, mas se você quiser, pode usar o int() para converter a string em inteiro
notaTrabalho = float(input("Digite sua nota de trabalho: "))
notaProva = float(input("Digite sua nota de prova: "))

# Calcula a média
media = (notaTrabalho + notaProva) / 2

# Exibe a média e o resultado
print(f"Sua média é: {media:.2f}") #Sempre que quisermos inserir uma variável dentro de uma string, utilizamos o f antes da string e colocamos a variável entre chaves {}
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
