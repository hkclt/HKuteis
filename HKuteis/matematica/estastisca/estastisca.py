def moda(*nums):

    contagem = {}
    for n in nums:
        if n in isinstance(n, (int, float)):
            if n in contagem:
                contagem[n] += 1
            else:
                contagem[n] = 1
            
            
    if len(contagem) == 0:
        return None
    else:
        return max(contagem)