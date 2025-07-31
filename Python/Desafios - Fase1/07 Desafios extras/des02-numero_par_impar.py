# Número par ou ímpar
# Desafio: Peça ao usuário um número e diga se ele é par ou ímpar.
# 💡 Dica: Use o operador % para verificar o resto da divisão.
# Se o resto for 0, o número é par
# Se for diferente de 0, é ímpar

numero = int(input("Informe um número: "))

resto = numero % 2

if resto == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

# Por que usar % e não /?
# / retorna o quociente da divisão (o resultado da conta).
# % retorna o resto da divisão (o que sobra), que é exatamente o que define par ou ímpar.