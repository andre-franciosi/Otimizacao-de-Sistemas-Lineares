import canto_noroeste

# Exemplo de uso
oferta = [10, 20, 30]
demanda = [20, 10, 20, 20]
custos = [
    [2, 3, 1, 4],
    [5, 4, 8, 1],
    [7, 2, 6, 2]
]

alocacao_inicial = canto_noroeste.canto_noroeste(oferta, demanda, custos)

print("Alocação inicial:")
for linha in alocacao_inicial:
    print(linha)
