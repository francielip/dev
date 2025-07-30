#########################################################################
# Python - Entrada e Saída de Dados
#########################################################################

# Exemplo de entrada de dados em Python
# O caracter "=" é usado para atribuir valores a variáveis
nome = input ("Digite o seu  nome: ")
sobrenome = input ("Digite o seu sobrenome: ")

# Constante declarada em maiúsculas
ANO_ATUAL = 2025
# Exemplo de entrada de dados com tipo específico (tipo de dados inteito)
idade = int(input("Digite a sua idade: "))

ano_nascimento = ANO_ATUAL - idade

# Exemplo de saída de dados em Python
print("Olá!", nome , "Seja bem vindo!")

# Exeplo de saída de dados com sobrenome. O caracter "+" é usado para concatenar strings
print("Olá! " + nome + " " + sobrenome + " Seja bem vindo!")

print(f"Olá, {nome}! Você nasceu em {ano_nascimento}.")