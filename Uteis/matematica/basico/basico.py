from cores import vermelho, limpa

def soma(*nums):
    soma = 0
    try:
        for n in nums:
            soma += n
    except(ValueError, TypeError):
        print(f'{vermelho}ERRO! valor invalido{limpa}')
    else:
        return soma

def substrair(*nums):
    sub = 0
    try:
        for n in nums:
            sub -= n
    except(ValueError, TypeError):
        print(f'{vermelho}ERRO! valor invalido{limpa}')
    else:
        return sub

def multiplicar(*nums):
    multi = 1
    try:
        for n in nums:
            multi *= n
    except(ValueError, TypeError):
        print(f'{vermelho}ERRO! valor invalido{limpa}')
    else:
        return multi

def dividir(*nums):
    resul = 0
    try:
        for n in nums:
            resul /= n
    except(ValueError, TypeError):
        print(f'{vermelho}ERRO! valor invalido{limpa}')
    except ZeroDivisionError:
        print(f'{vermelho}ERRO! Você tentou dividir por 0{limpa}')
    else:
        return resul
        
def raiz(num):
    from math import sqrt
    try:
        resul = sqrt(num)
    except:
        print(f'{vermelho}Algum erro aconteceu {limpa}')
    else: resul
        
def potencia(num, pote=2):
    try:
        resul = num ** pote
    except(ValueError, TypeError):
        print(f'{vermelho}ERRO! valor invalido{limpa}')
    else:
        return resul