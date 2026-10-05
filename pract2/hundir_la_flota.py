import random

LISTA_LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
MAP_LETRAS = { 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9 }

def crear_tablero():
    return [["-" for _ in range(10)] for _ in range(10)]

def imprimir_tablero(tablero, mostrar_barcos=False):
    print("   " + " ".join(LISTA_LETRAS))
    for i in range(10):
        fila_str = f"{i+1:2} "
        for j in range(10):
            val = tablero[i][j]
            if val == "B" and not mostrar_barcos:
                fila_str += "- "
            else:
                fila_str += f"{val} "
        print(fila_str)

def celda_libre(tablero, i, j):
    if not (0 <= i < 10 and 0 <= j < 10):
        return False
    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if 0 <= r < 10 and 0 <= c < 10:
                if tablero[r][c] == "B":
                    return False
    return True

def colocar_barco(tablero, n):
    colocado = False
    while not colocado:
        vertical = random.randint(0, 1)
        if vertical:
            i = random.randint(0, 10 - n)
            j = random.randint(0, 9)
        else:
            i = random.randint(0, 9)
            j = random.randint(0, 10 - n)
        
        libres = True
        for k in range(n):
            ri = i + k if vertical else i
            cj = j if vertical else j + k
            if not celda_libre(tablero, ri, cj):
                libres = False
                break
        
        if libres:
            for k in range(n):
                ri = i + k if vertical else i
                cj = j if vertical else j + k
                tablero[ri][cj] = "B"
            colocado = True

def inicializar_flota(tablero):
    barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for b in barcos:
        colocar_barco(tablero, b)

def convertir_coordenada(texto):
    if len(texto) < 2:
        return None
    letra = texto[0].upper()
    if letra not in MAP_LETRAS:
        return None
    try:
        fila = int(texto[1:]) - 1
        columna = MAP_LETRAS[letra]
        if 0 <= fila < 10 and 0 <= columna < 10:
            return (fila, columna)
    except ValueError:
        return None
    return None

def jugar():
    print("Bienvenido a Hundir la Flota!!!")
    tablero_pc = crear_tablero()
    inicializar_flota(tablero_pc)
    
    tablero_usuario_vistas = crear_tablero()
    
    pdt = []
    for i in range(10):
        for j in range(10):
            pdt.append((i, j))
            
    print("Voy a distribuir mis barcos")
    print("Ya está. Podemos empezar:")
    
    ultimo_disparo_pc = None
    ultimo_resultado_pc = "agua"
    
    while True:
        imprimir_tablero(tablero_usuario_vistas)
        jugada_str = input("Introduce tu jugada (ej. A1): ")
        coord = convertir_coordenada(jugada_str)
        
        if not coord:
            print("Coordenada inválida. Prueba otra vez.")
            continue
            
        fi, ci = coord
        if tablero_pc[fi][ci] == "B":
            print("¡Tocado! Has dado a un barco.")
            tablero_usuario_vistas[fi][ci] = "X"
            tablero_pc[fi][ci] = "X"
        else:
            print("Agua. Has fallado.")
            tablero_usuario_vistas[fi][ci] = "+"
            
        if ultimo_resultado_pc == "tocado" and ultimo_disparo_pc:
            fi_p, ci_p = ultimo_disparo_pc
            candidatos = [(fi_p-1, ci_p), (fi_p+1, ci_p), (fi_p, ci_p-1), (fi_p, ci_p+1)]
            vecinos_validos = [c for c in candidatos if c in pdt]
            if vecinos_validos:
                p = random.randint(0, len(vecinos_validos) - 1)
                i_pc, j_pc = vecinos_validos[p]
                pdt.remove((i_pc, j_pc))
            else:
                n = len(pdt)
                p = random.randint(0, n - 1)
                i_pc, j_pc = pdt.pop(p)
        else:
            n = len(pdt)
            p = random.randint(0, n - 1)
            i_pc, j_pc = pdt.pop(p)
            
        letra_pc = LISTA_LETRAS[j_pc]
        print(f"Ahora tiro yo: {letra_pc}{i_pc + 1}")
        res_pc = input("¿Cómo ha resultado mi disparo (A:agua, T:tocado, H:hundido)?: ").strip().upper()
        
        ultimo_disparo_pc = (i_pc, j_pc)
        if res_pc == "T" or res_pc == "H":
            ultimo_resultado_pc = "tocado"
            print("Jaja, voy a por ti")
        else:
            ultimo_resultado_pc = "agua"

if __name__ == "__main__":
    jugar()
