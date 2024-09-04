# Ordenação Total
lista = [(1, 3), (3, 2), (2, 1), (1, 2)]

#ordena primeiro pelo segundo número, e então pelo primeiro
lista_ordenada_total = sorted(lista, key=lambda x: (x[1], x[0]))
print("Ordenação Total:", lista_ordenada_total)
