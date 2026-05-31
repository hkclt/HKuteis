
def soma(*nums):
    """
    -> Soma todos os números fornecidos.
    :param nums: Números a serem somados.
    :return: O valor da soma de todos os números.
    """
    total = 0
    for n in nums:
        if isinstance(n, (int, float)):
            total += n

    return total

def subtrair(*nums):
    """
    -> Subtrai os números fornecidos em sequência.
    :param nums: Números a serem subtraídos.
    :return: O resultado da subtração em sequência.
    """
    if not nums:
        return None
    sub = nums[0]
    for n in nums[1:]:
        if isinstance(n, (int, float)):
            sub -= n

    return sub

def multiplicar(*nums):
    """
    -> Multiplica todos os números fornecidos.
    :param nums: Números a serem multiplicados.
    :return: O produto de todos os números.
    """
    if not nums:
        return None
    multi = 1
    for n in nums:
        if isinstance(n, (int, float)):
            multi *= n

    return multi

def dividir(*nums):
    """
    -> Divide os números fornecidos em sequência.
    :param nums: Números a serem divididos.
    :return: O resultado da divisão em sequência.
    """
    resul = None

    for n in nums:
        if not isinstance(n, (int, float)):
            continue

        if resul is None:
            resul = n
        elif n != 0:
            resul /= n

    return resul

def media(*nums):
    valores = [n for n in nums if isinstance(n, (int, float))]
    if not valores:
        return None
    return sum(valores) / len(valores)

def valido(*nums):
    validos = []
    for n in nums:
        if isinstance(n, (int, float)):
            validos.append(n)
    return validos

def amplitude(*nums):
    resul = None
    validos = []
    for n in nums:
        if isinstance(n, (float, int)):
            validos.append(n)
    if len(validos) >= 2:
        resul = max(validos) - min(validos)
    return resul

def soma_quadrados(*nums):
    soma = 0 
    for n in nums:
        if isinstance(n, (int, float)):
            soma += n ** 2
    return soma

def inverso_logico(n):
    if n == 0 or not isinstance(n, (int, float)):
        return None
    else:
        resul = 1 / n
        return resul
    
def dif_absoluta(a, b):
    if isinstance(a, (int, float)) and isinstance( b, (int, float)):
        resul = a - b
        if resul < 0:
            return None
        else:
            return resul
    
def produto_seguro(*nums):
    multi = 1
    for n in nums:
        if isinstance(n, (int, float)) and n != 0:
            multi *= n
    return multi
            
def soma_ponderana(*nums, pesos):
    soma = multi = peso = resul = 0
    cont = 0
    for n in nums:
        if isinstance(n, (int, float)):
            multi = n * pesos[cont]
            soma += multi
            peso += pesos[cont]
            cont += 1
            
    resul = soma / peso
    return resul

