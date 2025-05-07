ano_atual= 2025
ano_nascimento= int(input("Digite o ano de nascimento: "))
idade= ano_atual - ano_nascimento
print("Você tem", idade, "anos.")
if idade < 16:
    print("Você não pode votar.")
elif idade < 18 or idade > 70:
    print("Seu voto é opcional.")
elif idade >= 18:
    print("Seu voto é obrigatório.")