# Laço com FOR - Tabuada
# Desafio: Peça um número ao usuário e mostre a tabuada dele de 1 a 10.

numero = int(input("Informe um número: " ))

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")

# 🔎 Sugestão opcional (estética):
# Você pode alinhar visualmente a saída da tabuada usando str.ljust() ou espaçamento, mas isso é só estética, não é necessário. Exemplo:
# print(f"{numero} x {i:2} = {resultado}")
# Isso alinha os números para melhor leitura quando a tabuada passa de 9. Mas o seu jeito está ótimo e totalmente funcional.