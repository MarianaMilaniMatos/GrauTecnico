# Sistema de Notas para Vários Alunos

# Passo 1: Definir quantos alunos serão cadastrados
quantidade_alunos = int(input("Quantos alunos deseja cadastrar? "))

# Passo 2: Repetir o processo para cada aluno
for i in range(quantidade_alunos):
    print(f"\n--- Cadastro do {i + 1}º aluno ---") # {i+1} = f-strings (ou formatted string literals), usado para formatar strings de forma mais legível e eficiente, permitindo a inclusão de expressões dentro de chaves {}.
    #Sempre que quisermos inserir uma variável dentro de uma string, utilizamos o f antes da string e colocamos a variável entre chaves {}
    
    # Entrada dos dados
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota_trabalho = float(input("Digite a nota do trabalho: "))
    nota_prova = float(input("Digite a nota da prova: "))
    
    # Cálculo da média
    media = (nota_trabalho + nota_prova) / 2
    
    # Exibição dos resultados
    print(f"\nResultado do aluno: {nome}")
    print(f"Média final: {media:.2f}")
    
    # Verificação da situação
    if media >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")
