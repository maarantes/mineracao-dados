dados = [100, 150, 200, 250, 300, 350]

n = len(dados)
meio = n // 2

if n % 2 == 0:
    parte_inferior = dados[:meio]
    parte_superior = dados[meio:]
else:
    parte_inferior = dados[:meio]
    parte_superior = dados[meio+1:]

def mediana(lista):
    m = len(lista)
    meio = m // 2
    if m % 2 == 0:
        return (lista[meio - 1] + lista[meio]) / 2
    else:
        return lista[meio]

q1 = mediana(parte_inferior)
q3 = mediana(parte_superior)

print("Parte inferior:", parte_inferior)
print("Parte superior:", parte_superior)
print("Q1:", q1)
print("Q3:", q3)