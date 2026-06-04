import sys
import os

# Garante que o pacote Uteis seja encontrado independente de onde o script é executado
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from HKuteis import *

# ============================================================
# CORES E ESTILOS
# ============================================================
print(f"\n{negrito}{azul}{'=' * 50}{limpa}")
print(f"{negrito}{azul}        TESTES DO PACOTE HKuteis{limpa}")
print(f"{negrito}{azul}{'=' * 50}{limpa}\n")

# ============================================================
# LINHAS DECORATIVAS
# ============================================================
print(f"{negrito}{amarelo}[ LINHAS DECORATIVAS ]{limpa}")
linha(0, tam=40)        # ---
linha(1, tam=40)        # ===
linha(6, tam=40)        # ***
linha(45, tam=40)       # ★★★
linha(47, tam=40)       # ███
print()

# ============================================================
# MATEMÁTICA BÁSICA
# ============================================================
print(f"{negrito}{amarelo}[ MATEMÁTICA BÁSICA ]{limpa}")
linha(0)

print(f"  soma(1, 2, 3, 4)         = {verde}{soma(1, 2, 3, 4)}{limpa}")
print(f"  subtrair(10, 3, 2)       = {verde}{subtrair(10, 3, 2)}{limpa}")
print(f"  multiplicar(2, 3, 4)     = {verde}{multiplicar(2, 3, 4)}{limpa}")
print(f"  dividir(100, 4, 5)       = {verde}{dividir(100, 4, 5)}{limpa}")
print(f"  media(10, 20, 30)        = {verde}{media(10, 20, 30)}{limpa}")
print(f"  amplitude(5, 15, 3, 20)  = {verde}{amplitude(5, 15, 3, 20)}{limpa}")
print(f"  soma_quadrados(3, 4)     = {verde}{soma_quadrados(3, 4)}{limpa}")
print(f"  valido(1, 'x', 2, None)  = {verde}{valido(1, 'x', 2, None)}{limpa}")
print(f"  inverso_logico(4)        = {verde}{inverso_logico(4)}{limpa}")
print(f"  dif_absoluta(10, 3)      = {verde}{dif_absoluta(10, 3)}{limpa}")
print(f"  produto_seguro(2,0,5)    = {verde}{produto_seguro(2, 0, 5)}{limpa}")
print(f"  soma_ponderana(3,5,pesos=[2,3]) = {verde}{soma_ponderana(3, 5, pesos=[2, 3])}{limpa}")
print()

# ============================================================
# UTILITÁRIOS
# ============================================================
print(f"{negrito}{amarelo}[ UTILITÁRIOS ]{limpa}")
linha(0)

print(f"  potencia(3, 3)           = {verde}{potencia(3, 3)}{limpa}")
print(f"  raiz(144)                = {verde}{raiz(144)}{limpa}")
print(f"  porcentagem(200, 15)     = {verde}{porcentagem(200, 15)}{limpa}")
print(f"  absoluto(-42)            = {verde}{absoluto(-42)}{limpa}")
print(f"  resto_divisao(17, 5)     = {verde}{resto_divisao(17, 5)}{limpa}")
print()

# ============================================================
# AVANÇADO
# ============================================================
print(f"{negrito}{amarelo}[ AVANÇADO ]{limpa}")
linha(0)

print(f"  fatorial(6)              = {verde}{fatorial(6)}{limpa}")
print(f"  fatorial(5, show=True)   = {verde}{fatorial(5, show=True)}{limpa}")
print(f"  regrade3(2, 8, 5)        = {verde}{regrade3(2, 8, 5)}{limpa}")
print()

# ============================================================
# LOADING
# ============================================================
print(f"{negrito}{amarelo}[ BARRA DE LOADING ]{limpa}")
linha(0)
print("  Carregando...")
loading(carac='█', vazio='.', temptot=3.0, delay=0.1)
print(f"\n{negrito}{verde}  Todos os testes concluídos!{limpa}\n")



loading(carac='█', vazio='.', temptot=3.0, delay=0.1)