def loading(carac='█', vazio='░', temptot=10.0, delay=0.1):
    from time import sleep as dormir
    total = int(temptot / delay)
    
    for i in range(total + 1):
        cheia = carac * i
        faltando = vazio * (total - i)
        print(f'\r{cheia}{faltando}')
        dormir(delay)