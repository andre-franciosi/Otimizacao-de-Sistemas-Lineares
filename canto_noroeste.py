def canto_noroeste(oferta, demanda, custos):
    m = len(oferta)
    n = len(demanda)
    
    alocacao = [[0] * n for _ in range(m)]
    
    i, j = 0, 0
    
    while i < m and j < n:
        if oferta[i] == 0:
            i += 1
            continue
        if demanda[j] == 0:
            j += 1
            continue
        
        quantidade = min(oferta[i], demanda[j])
        alocacao[i][j] = quantidade
        
        oferta[i] -= quantidade
        demanda[j] -= quantidade
        
        if oferta[i] == 0:
            i += 1
        if demanda[j] == 0:
            j += 1
    
    return alocacao


