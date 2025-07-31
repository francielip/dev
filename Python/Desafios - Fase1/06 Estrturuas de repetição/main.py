# O programa vai ler 4 notas de um aluno e calcular a média.
# Se a média for maior ou igual a 7, o aluno é aprovado.
# Se a média for menor que 7, o aluno é reprovado.
# Se a média for exatamente 10, o aluno é aprovado com louvor.

#Constante para a quantidade de notas que iremos inserir
QUANTIDADE_DE_NOTAS = 4
MEDIA = 6

# Exemplo 1
while True:
    #Variáveis, com as quatro notas e a média do aluno
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))

    media_final = (nota1 + nota2 + nota3 + nota4) / QUANTIDADE_DE_NOTAS

    print(f"A média do aluno é: {media_final:.2f}")

    # Estrutura de repetição
    if (media_final>=MEDIA):
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")
    
    continuar = input("Deseja continuar a leitura <s/n>?").lower()
    
    if continuar != 's':
        break

print("Programa encerrado.")

# Exemplo 2
for i in range (5):
    print(f"Leitura do aluno {i+1}!")
    #Variáveis, com as quatro notas e a média do aluno
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))

    media_final = (nota1 + nota2 + nota3 + nota4) / QUANTIDADE_DE_NOTAS

    print(f"A média do aluno é: {media_final:.2f}")

    # Estrutura de repetição
    if (media_final>=MEDIA):
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")
    
print("Programa encerrado.")