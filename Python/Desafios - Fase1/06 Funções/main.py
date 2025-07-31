#def nome_da_funcao(parametros):
#    instrução 1
#    instrução 2
#    ...    
#    return valor_de_retorno (opcional)

def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2
    
    return imposto