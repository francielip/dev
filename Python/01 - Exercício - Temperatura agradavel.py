#Constante para temperatura agradável
TEMP_AGRADAVEL = 30

#Variaveis
temp_atual = int(input("Informe a temperatura atual: "))

#Condicionais
if temp_atual < TEMP_AGRADAVEL:
    print("A temperatura está abaixo do ideal.")
elif temp_atual > TEMP_AGRADAVEL:
    print("A temperatura está acima do ideal.")
else:
    print("A temperatura está agradável.")