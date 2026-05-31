
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
    if not nums:
        return None

    resul = nums[0]
    
    for n in nums[1:]:
        if isinstance(n, (int, float)) and n != 0 :
            resul /= n

    return resul

        
def raiz(num):
    """
    -> Calcula a raiz quadrada de um número.
    :param num: O número a ter a raiz calculada.
    :return: O valor da raiz quadrada do número.
    """

    from math import sqrt
    if isinstance(num, (int, float)) and num >= 0:
        resul = sqrt(num)
        return resul
        
def potencia(num, pote=2):
    """
    -> Calcula a potência de um número.
    :param num: A base da potência.
    :param pote: (opcional) O expoente da potência. Padrão: 2.
    :return: O valor de num elevado a pote.
    """

    if isinstance(num, (int, float)) and isinstance(pote, (int, float)):
        resul = num ** pote
        return resul
    
def media(*nums):
    if not nums:
        return None
    cont = 0
    tot = 0
    resul = 0
    for n in nums:
        if isinstance(n, (float, int)):
            tot +=  n
            cont += 1
    resul = dividir(tot / cont)
    return resul

def porcentagem(num, por=10):
    if not num:
        return None
    if isinstance((por, (int, float)), (num, (int, float))):
        resul = (por / 100) * num
        return resul
    
def absoluto(n):
    if not n:
        return None
    if n == 0:
        return 0
    elif n < 0:
        n = n * -1
    return n

def resto_divisao(num, quo):
    if not num or not quo:
        return None
    if num != 0 or quo != 0:
        resul = num // quo
        return resul
    else:
        return 0
    
def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return o Valor do Fatorial de um número n.
    """
    
    r = 1
    texto = []
    text = ''

    while n > 1:
        r = r * n
        texto.append(n)
        n -= 1
    
    if show:
        texto.append(1)
        print('-' * 30)
        for c in texto:
            if c == texto[-1]:
                text = text + str(c) + ' = ' + str(r)
            else:
                text = text + str(c) + ' X '
            
        return text
    else:
        return r
    
def regrade3(n1,n2,n3):
    x = n2
    if not n1 or not n2 or not n3:
        return None