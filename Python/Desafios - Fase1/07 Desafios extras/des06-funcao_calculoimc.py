# Função - Cálculo de IMC
# Desafio: Crie uma função chamada calcular_imc(peso, altura) que:
# Calcule e retorne o IMC.
# Depois, chame a função com dados inseridos pelo usuário.
# 💡 IMC = peso / altura²

def calculo_imc(p,a):
    imc = p / (a ** 2)
    return imc

peso = float(input("Informe o seu peso (00.0 kgs): "))
altura = float(input("Informe a sua altura (0.00 m): "))

imc_calculado = calculo_imc(peso,altura)

print(f"Com o seu peso de {peso} kgs e a sua altura de {altura} m, o seu IMC ficou em {imc_calculado:.2f}.")