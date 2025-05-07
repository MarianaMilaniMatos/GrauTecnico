# Atividade 1 - Padaria
# Inicialização das variáveis de opção e quantidades de cada tipo de pão
opcao = "0"
qt_frances = 0
qt_integral = 0
qt_doce_liso = 0
qt_farofa = 0
qt_pao_forma = 0

# Inicialização das variáveis de valor total de cada tipo de pão
valor_frances = 0
valor_integral = 0
valor_doce_liso = 0
valor_farofa = 0
valor_forma = 0

while opcao !=6:
    print("------------PADARIA------------")
    print("[1] Pão Frances")
    print("[2] Pão Integral")
    print("[3] Pão Doce Liso")
    print("[4] Pão Doce Farofa")
    print("[5] Pão de Forma")
    print("[6] Fim da compra.")
    print("-------------------------------")
    opcao = input("Escolha sua opção: ")
    print("-------------------------------")
   
    if opcao == "1": #"1" string
        qt_frances = int(input("Digite a quantidade de pão francês que você quer: "))
        valor_frances = qt_frances * 1.04
    elif opcao == "2":
        qt_integral = int(input("Digite a quantidade de pão integral que você quer: "))
        valor_integral = qt_integral * 1.04
    elif opcao == "3":
        qt_doce_liso = int(input("Digite a quantidade de pão doce liso que você quer: "))
        valor_doce_liso = qt_doce_liso * 1.08
    elif opcao == "4":
        qt_farofa = int(input("Digite a quantidade de pão doce farofa que você quer: "))
        valor_farofa = qt_farofa * 1.11
    elif opcao == "5":
        qt_pao_forma = int(input("Digite a quantidade de pão de forma que você quer: "))
        valor_forma = qt_pao_forma * 0.95
    elif opcao == "6":
        print("Obrigado pela compra.")
        break
print("-------------------------------")
print("    Resumo da compra:")
if qt_frances > 0:
        print(f"Pão francês: {qt_frances} x R$ 1.04 = R$ {valor_frances:.2f}")
if qt_integral > 0:
        print(f"Pão Integral: {qt_integral} x R$ 1.04 = R$ {valor_integral:.2f}")
if qt_doce_liso > 0:
        print(f"Pão Doce Liso: {qt_doce_liso} x R$ 1.04 = R$ {valor_doce_liso:.2f}")
if qt_farofa > 0:
        print(f"Pão francês: {qt_farofa} x R$ 1.04 = R$ {valor_farofa:.2f}")
if qt_pao_forma > 0:
        print(f"Pão francês: {qt_pao_forma} x R$ 1.04 = R$ {valor_forma:.2f}")
print("-------------------------------")
print(f"Total da compra: R$ {(valor_frances + valor_integral + valor_doce_liso + valor_farofa + valor_forma):.2f}")
print("-------------------------------")


