# Estrutura de Decisão (if, elif, else)
# Desafio: Programa de classificação etária:
# Solicite a idade da pessoa.
# Diga se ela é criança (até 12), adolescente (13 a 17), adulto (18 a 59) ou idoso (60+).

idade = int(input("Informe a sua idade: "))

if idade <= 12:
    print(f"Você tem {idade} anos, você é uma criança ainda!")
elif ((idade>=13) and (idade<=17)):
    print(f"Você tem {idade} anos, você é um(a) adolescente!")
elif ((idade>=18) and (idade<=59)):
    print(f"Você tem {idade} anos, vcoê é um(a) adulto!")
else:
    print(f"Você tem {idade} anos, chegou na melhor idade! Viva os 60+!!")

# Sugestão sugerida pelo ChatGPT:
# idade = int(input("Informe a sua idade: "))
# 
# if idade <= 12:
#     print(f"Você tem {idade} anos, você é uma criança ainda!")
# elif idade <= 17:
#     print(f"Você tem {idade} anos, você é um(a) adolescente!")
# elif idade <= 59:
#     print(f"Você tem {idade} anos, você é um(a) adulto!")
# else:
#     print(f"Você tem {idade} anos, chegou na melhor idade! Viva os 60+!!")
#
#Por que isso também é bom?
#✅ Não precisa repetir idade >= ... em todas as condições — como o Python avalia de cima para baixo, só entra na próxima condição se a anterior for falsa.
#
#✅ Código mais limpo, sem comprometer o entendimento.
#
#✅ O f-string com o texto ficou ótimo — amigável e personalizado com a idade da pessoa.