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

def porcentagem(num, por=10):
    if not isinstance(num, (int, float)) or not isinstance(por, (int, float)):
        return None
    return (por / 100) * num
    
def absoluto(n):
    if not isinstance(n, (int, float)):
        return None
    return -n if n < 0 else n

def resto_divisao(num, quo):
    if not isinstance(num, (int, float)) or not isinstance(quo, (int, float)):
        return None
    if quo == 0:
        return None
    return num % quo
