def moda(*nums):

    contagem = {}
    for n in nums:
        if isinstance(n, (int, float)):
            if n in contagem:
                contagem[n] += 1
            else:
                contagem[n] = 1
            
            
    if len(contagem) == 0:
        return None
    else:
        maximo = max(contagem, key=contagem.get)
        return maximo
    
def mediana(*nums):
    org = []

    for n in nums:
        if isinstance(n, (float, int)):
            org.append(n)
    if len(org) == 0:
        return None
    org.sort(   )
    if len(org) % 2 != 0:
        meio = org[len(org) // 2]
        return meio
    else:
        dire = len(org) // 2
        esq = len(org) // 2 - 1
        meio = (org[esq] + org[dire]) / 2
        return meio
    
def variancia(*nums):
    tot = 0
    validos = []
    for v in nums:
        if isinstance(v, (int, float)):
            validos.append(v)
    if len(validos) < 2:
        return None
    else:
        med = sum(validos) / len(validos)
        
    for n in validos:
        tot += (n - med) ** 2
        
    final = tot / len(validos)
    return final

def desvio_padrao(*nums):
    from ..utilitarios import raiz
    var = variancia(*nums)
    if var is None:
        return None
    return raiz(var)