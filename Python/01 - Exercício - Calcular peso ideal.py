#########################################################################
# Exercício: Calcular Peso Ideal
#########################################################################
# Tendo como dados de entrada a altura e o sexo de uma pessoa, contrua um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7 * altura) - 58
# Para mulheres: (62.1 * altura) - 44.7
# Entrada de dados

altura = input ("Informe a sua altura (X,XX m): ")
sexo = input ("Informe o seu sexo (M/F): ").upper()

if sexo == 'F' {
    peso_ideal = (62,1 * altura) - 44.7
} else if sexo == 'M' {
    peso_ideal = (72,7 * altura) - 58
}

print("Seu peso ideal é: " peso_ideal)