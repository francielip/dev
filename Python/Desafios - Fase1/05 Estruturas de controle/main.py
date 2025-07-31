# O programa vai ler 4 notas de um aluno e calcular a média.
# Se a média for maior ou igual a 7, o aluno é aprovado.
# Se a média for menor que 7, o aluno é reprovado.
# Se a média for exatamente 10, o aluno é aprovado com louvor.

#Constante para a quantidade de notas que iremos inserir
QUANTIDADE_DE_NOTAS = 4
MEDIA = 7

#Variáveis, com as quatro notas e a média do aluno
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

media_final = (nota1 + nota2 + nota3 + nota4) / QUANTIDADE_DE_NOTAS

print(f"Sua média final é: {media_final:.2f}")

# Estrutura de selecao simples
if (media_final >= MEDIA):
    print("Aluno aprovado!")

# Estrutura de selecao composta
if (media_final >= MEDIA):
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

# Estrutura de selecao encadeada
if (media_final >= MEDIA):
    if (media_final == 10):
        print("Aluno aprovado com louvor!")
    else:
        print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

# Estrutura de seleção múltipla
if (media_final < MEDIA):
    print("Aluno reprovado!")
elif (media_final <= 8):
    print("Aluno aprovado, mas estude mais!")
elif (media_final <= 9):
    print("Aluno aprovado, bom trabalho!")
elif (media_final == 10):
    print("Aluno aprovado com louvor!")
else:
    print("Média inválida!")