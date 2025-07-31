# WHILE - Menu Simples
# Desafio: Crie um menu que repita até o usuário escolher sair:
# 1 - Ver saudação
# 2 - Ver data fictícia
# 3 - Sair
# 💡 Dica: Use while True: e break para sair.

while True:
    opcao = int(input("Escolha uma opção (1 - Ver saudação | 2 - Ver data | 3 - Sair): "))
    if opcao == 1:
        print(f"Você escolheu a opção {opcao} - Ver saudação.")
    elif opcao == 2:
        print(f"Você escolheu a opção {opcao} - Ver data.")
    elif opcao == 3:
        print(f"Você escolheu a opção {opcao} - Sair.")
        break
    else:
        print(f"Opção inválida. Digite novamente.")

# 💡 Diferença entre if e elif:
# if sempre testa a condição, mesmo que um if anterior já tenha sido verdadeiro.
# elif só testa se os anteriores forem falsos.
# 🤔 E se usasse só if em tudo?
# ⚠️ Nesse caso, mais de um bloco pode ser executado se as condições não forem bem controladas. E o else estaria ligado apenas ao último if, o que pode gerar resultados inesperados ou incorretos.