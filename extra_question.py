import random

def gerar_referencia(tamanho, max_pagina=9):
    return [random.randint(0, max_pagina) for _ in range(tamanho)]

def fifo(referencia, num_quadros):
    quadros = []
    falhas = 0
    
    for pagina in referencia:
        if pagina not in quadros:
            falhas += 1
            if len(quadros) < num_quadros:
                quadros.append(pagina)
            else:
                quadros.pop(0)
                quadros.append(pagina)
    
    return falhas

def lru(referencia, num_quadros):
    quadros = []
    falhas = 0
    tempo_uso = {}
    
    for tempo, pagina in enumerate(referencia):
        if pagina not in quadros:
            falhas += 1
            if len(quadros) < num_quadros:
                quadros.append(pagina)
            else:
                lru_pagina = min(quadros, key=lambda p: tempo_uso[p])
                quadros.remove(lru_pagina)
                quadros.append(pagina)
        tempo_uso[pagina] = tempo 
    
    return falhas

def testar_com_varios_quadros(referencia, max_quadros):
    print(f"String de referência: {referencia}")
    
    for num_quadros in range(1, max_quadros + 1):
        falhas_fifo = fifo(referencia, num_quadros)
        falhas_lru = lru(referencia, num_quadros)
        
        print(f"\nNúmero de quadros: {num_quadros}")
        print(f"FIFO - Falhas de página: {falhas_fifo}")
        print(f"LRU  - Falhas de página: {falhas_lru}")
        
        if falhas_fifo < falhas_lru:
            print("FIFO teve menos falhas.")
        elif falhas_fifo > falhas_lru:
            print("LRU teve menos falhas.")
        else:
            print("Ambos os algoritmos tiveram o mesmo número de falhas.")

tamanho_referencia = 20 
max_quadros = 5 
referencia = gerar_referencia(tamanho_referencia) 

testar_com_varios_quadros(referencia, max_quadros)
