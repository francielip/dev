alunos = [{
    "nome": "",
    "turma": "",
    "media": 0.0
} for _ in range(4)]

matriz = [[0 for _ in range(4)] for _ in range(4)]

for linha in range(4):
    alunos[linha]["nome"] = input("Digite o nome do aluno: ")
    alunos[linha]["turma"] = input("Digite a turma do aluno: ")
    for coluna in range(4):
        matriz[linha][coluna] = float(input(f"Digite a nota {coluna + 1} do {alunos[linha]['nome']}: "))

#print(f"Nomes dos alunos: {alunos}")
#print(f"Matriz de notas: {matriz}")

for linha in range (4):
    soma = sum(matriz[linha])
    media = soma/len(matriz[linha])
    alunos[linha]["media"] = media
    print(f"A média do aluno {alunos[linha]["nome"]} é: {media:.2f}")

print(f"Nomes dos alunos: {alunos}")