# Vetores - Lista de Nomes
# Desafio: Crie uma lista com o nome de 5 pessoas usando for. Depois exiba todos os nomes com um for.

nomes = [""] * 5

for i in range(5):
    nomes[i] = input("Informe o seu nome: ")

for i in range(5):
    print(f"Seu nome é {nomes[i]}")

# nomes = []
# 
# for i in range(5):
#     nome = input(f"Informe o nome da pessoa {i+1}: ")
#     nomes.append(nome)
# 
# print("\nLista de nomes informados:")
# for nome in nomes:
#     print(f"- {nome}")
# 
# O for direto na lista (for nome in nomes) é mais claro e típico em Python.
# Como as listas crescem dinamicamente, é mais "pythônico" usar append() para adicionar nomes.