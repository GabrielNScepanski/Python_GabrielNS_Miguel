# Ordenação Customizada
lista = ["cabra","cavalo","tigre","guaxinim"]

# Ordena pela última letra
def ultima_letra(s):
    return s[-1]

lista_ordenada_custom = sorted(lista, key=ultima_letra)
print("Ordenação Customizada:", lista_ordenada_custom)
