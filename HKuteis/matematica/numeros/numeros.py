def eh_primo(n):
    if not isinstance(n, int) or n < 2:
        return False
    from ..utilitarios import raiz
    for num in range(2, int(raiz(n)) + 1):
        if n % num == 0:
            return False
        
    return True

def mdc(a,b):
    if isinstance(a, int) and isinstance(b, int):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    else:
        return None
    
def mmc(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return (a * b) // mdc(a, b)
    return None

def fibonnaci(n):

    if n > 0 and isinstance(n, int):
        nums = [0, 1]
        for c in range(0, n - 2):
            nums.append(nums[-1] + nums[-2])
        return nums
    else:
        return None
    