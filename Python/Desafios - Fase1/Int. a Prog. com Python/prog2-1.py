# Programa 2.1 - Primeiro programa com variáveis
a = 2
b = 3
print(a + b)

# Programa 2.2 - Cálculo de aumento de salário
salario = 1500
aumento = 5
print(salario + (salario * aumento / 100))

# Exercício 2.3 - Faça um programa que exiba seu nome na tela.
nome = "Francieli"
print(nome)

# Exercício 2.4 - EScreva um programa que exiba o resultado de 2a x 3b, em que a vale 3 e b vale 5.
a = 3
b = 5
print(2*a * 3*b)

# Exercício 2.5 - Modifique o programa 2.2, de forma que ele calcule um aumento de 15% para um salário de R$ 750,00.
salario = 750
aumento = 15
print(salario + (salario * aumento / 100))

# Exercício 3.4 - Escreva uma expressão para detemrinar se uma pessoa deve ou não pagar impostos.
# Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.
# salario = float(input("Informe o salário: R$ "))
salario = 1300
paga_imposto = salario > 1200
print("Deve pagar imposto?", paga_imposto)

# Exercício 3.5 - Calcule o resultado da expressão A > B and C or D, utilizando os valores da tabela a seguir:
a = 5
b = 1
c = True
d = True
resultado = a > b and c or d
print(resultado)

# Exercício 3.6 - Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
# Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
# Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis:
materia1 = 8
materia2 = 9
materia3 = 8
aprovado = materia1 > 7 and materia2 > 7 and materia3 > 7
print("Aluno aprovado?", aprovado)

# Exercício 3.7 - Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.
numero1 = int(input("Informe o primeiro número inteiro: "))
numero2 = int(input("Informe o segundo número inteiro: "))
soma = numero1 + numero2
print("A soma dos dois números é:", soma)