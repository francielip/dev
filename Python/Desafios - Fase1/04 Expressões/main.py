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

# Operação relacional == (igualdade) compara se a média é igual a 10
if media_final == 10:
    print("Aprovado com louvor!")
# Operação relacional >= (maior ou igual) compara se a média é maior ou igual a 7
elif media_final >= MEDIA:
    #A parte :.2f dentro da f-string (f"...") significa que você quer formatar o número com duas casas decimais
    print(f"Aprovado! Com média: {media_final:.2f}")
else:
    print(f"Reprovado! Com média: {media_final:.2f}")

#Operação relacional e logica com and/e
print(f"A nota esta entre 5 e 8? {(media_final >= 5) and (media_final <= 8)}")

#Operação relacional e logica com or/ou
print(f"A segunda nota ou a quarta estao acima da media? {(nota2 >= MEDIA) or (nota4 >= MEDIA)}")
