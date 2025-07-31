nomes = [''] * 4
matriz = [(0 for _ in range(4)) for _ in range(4)] #usa o _ para indicar que o valor não será usado

for linhas in range(4):
    nomes[linhas] = input("Digite o nome do aluno:")
    for coluna in range(4):
        matriz[linhas][coluna] = float(input(f"Digite a nota {coluna + 1} do aluno {nome}: "))

print(f"Nomes dos alunos: {nomes}")
print(f"Matriz de notas: {matriz}")

for linha in range(4):
    soma = sum(matriz[linha])
    media = soma / len(matriz[linha])
    print(f"A média do aluno {nomes[linha]} é: {media:.2f}")