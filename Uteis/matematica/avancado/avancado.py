def regrade3(n1, n2, n3):
    if any(not isinstance(x, (int, float)) for x in (n1, n2, n3)):
        return None
    if n1 == 0:
        return None

    return (n2 * n3) / n1

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