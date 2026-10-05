import random

# 1. Generar aleatoriamente una lista de 5 enteros en el rango [1, 10]
secreto = []
i = 0
while i < 5:
    secreto = secreto + [random.randint(1, 10)]
    i = i + 1

print("Hola campeón. Vamos a jugar.")
print("Déjame que piense ... hummm ... ya he elegido la lista de números")

intentos = 0
ganado = False

# 2. Bucle principal del juego
while not ganado:
    entrada = input("Adivínala: ")
    
    # Comprobar si pide las respuestas (no cuenta como intento)
    if entrada == "respuestas":
        print("Mi respuesta es: La solución es", secreto)
        continue
        
    # Procesar la entrada del usuario sin usar la función split()
    # Limpiamos los corchetes y extraemos los números recorriendo el texto
    intento_actual = []
    num_actual = ""
    j = 0
    while j < len(entrada):
        caracter = entrada[j]
        if caracter >= '0' and caracter <= '9':
            num_actual = num_actual + caracter
        else:
            if num_actual != "":
                intento_actual = intento_actual + [int(num_actual)]
                num_actual = ""
        j = j + 1
    if num_actual != "":
        intento_actual = intento_actual + [int(num_actual)]
        
    # Validar que se han introducido exactamente 5 números
    if len(intento_actual) != 5:
        print("Por favor, introduce una lista válida con 5 números (ejemplo: [1,2,3,4,5])")
        continue

    intentos = intentos + 1
    
    # 3. Calcular la respuesta indicando aciertos con 1 y fallos con 0
    respuesta_juego = []
    aciertos_totales = 0
    k = 0
    while k < 5:
        if intento_actual[k] == secreto[k]:
            respuesta_juego = respuesta_juego + [1]
            aciertos_totales = aciertos_totales + 1
        else:
            respuesta_juego = respuesta_juego + [0]
        k = k + 1
        
    print("Mi respuesta es:", respuesta_juego)
    
    # 4. Comprobar si ha ganado
    if aciertos_totales == 5:
        print("Muy bien!!! Ganaste!!! Has usado", intentos, "intentos.")
        ganado = True
