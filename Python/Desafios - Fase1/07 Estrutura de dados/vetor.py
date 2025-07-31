# Constante
QDE = 4
# Vetor
notas = [0.0] * QDE  # Inicializa um vetor de 4 posições com 0.0

# Estrutura
for i in range (len(notas)): # Percorre o vetor, com tamanho definido por len(notas)
    notas[i] = float(input(f"Digite a nota {i + 1} do aluno: "))

print(f"Notas: {notas}")

soma = sum(notas)  # Soma as notas
media = soma / len(notas)  # Calcula a média

print(f"A média do Aluno é: {media:.2f}")