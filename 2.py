# ========================
# PARTE 2: ALGORITMOS DE BÚSQUEDA
# ========================

pedidos = [
    {"código":"P001","cliente":"Juan Pérez","ciudad":"Lima","peso":10,"prioridad":"Alta","costo":80},
    {"código":"P002","cliente":"María López","ciudad":"Arequipa","peso":8,"prioridad":"Media","costo":60},
    {"código":"P003","cliente":"Carlos Díaz","ciudad":"Cusco","peso":12,"prioridad":"Alta","costo":90},
    {"código":"P004","cliente":"Ana Torres","ciudad":"Piura","peso":5,"prioridad":"Baja","costo":40},
    {"código":"P005","cliente":"Luis Ramos","ciudad":"Trujillo","peso":7,"prioridad":"Media","costo":55},
    {"código":"P006","cliente":"José Ruiz","ciudad":"Chiclayo","peso":9,"prioridad":"Alta","costo":70},
    {"código":"P007","cliente":"Pedro Soto","ciudad":"Lima","peso":11,"prioridad":"Media","costo":85},
    {"código":"P008","cliente":"Lucía Vega","ciudad":"Cusco","peso":6,"prioridad":"Alta","costo":65},
    {"código":"P009","cliente":"Miguel Cruz","ciudad":"Piura","peso":13,"prioridad":"Baja","costo":95},
    {"código":"P010","cliente":"Rosa Flores","ciudad":"Arequipa","peso":4,"prioridad":"Media","costo":35},
    {"código":"P011","cliente":"Jorge León","ciudad":"Lima","peso":15,"prioridad":"Alta","costo":100},
    {"código":"P012","cliente":"Patricia Gil","ciudad":"Trujillo","peso":8,"prioridad":"Media","costo":50},
    {"código":"P013","cliente":"Diego Silva","ciudad":"Cusco","peso":9,"prioridad":"Alta","costo":75},
    {"código":"P014","cliente":"Sandra Moya","ciudad":"Piura","peso":6,"prioridad":"Baja","costo":45},
    {"código":"P015","cliente":"Fernando Paz","ciudad":"Chiclayo","peso":10,"prioridad":"Media","costo":68},
]

# ========================
# BÚSQUEDA LINEAL
# ========================
def busqueda_lineal(pedidos, codigo):
    comparaciones = 0
    for pedido in pedidos:
        comparaciones += 1
        if pedido["código"] == codigo:
            print(f"Búsqueda Lineal: Encontrado en {comparaciones} comparaciones")
            return pedido
    print(f"Búsqueda Lineal: No encontrado en {comparaciones} comparaciones")
    return None

# ========================
# BÚSQUEDA LINEAL ACOTADA
# ========================
def busqueda_lineal_acotada(pedidos, codigo, inicio, fin):
    comparaciones = 0
    for i in range(inicio, min(fin, len(pedidos))):
        comparaciones += 1
        if pedidos[i]["código"] == codigo:
            print(f"Búsqueda Lineal Acotada: Encontrado en {comparaciones} comparaciones")
            return pedidos[i]
    print(f"Búsqueda Lineal Acotada: No encontrado en {comparaciones} comparaciones")
    return None

# ========================
# BÚSQUEDA BINARIA ITERATIVA
# ========================
def busqueda_binaria_iterativa(pedidos, codigo):
    pedidos_ordenados = sorted(pedidos, key=lambda x: x["código"])
    inicio, fin = 0, len(pedidos_ordenados) - 1
    comparaciones = 0
    while inicio <= fin:
        comparaciones += 1
        medio = (inicio + fin) // 2
        if pedidos_ordenados[medio]["código"] == codigo:
            print(f"Búsqueda Binaria Iterativa: Encontrado en {comparaciones} comparaciones")
            return pedidos_ordenados[medio]
        elif pedidos_ordenados[medio]["código"] < codigo:
            inicio = medio + 1
        else:
            fin = medio - 1
    print(f"Búsqueda Binaria Iterativa: No encontrado en {comparaciones} comparaciones")
    return None

# ========================
# BÚSQUEDA BINARIA RECURSIVA
# ========================
def busqueda_binaria_recursiva(pedidos, codigo, inicio, fin, comparaciones=0):
    if inicio > fin:
        print(f"Búsqueda Binaria Recursiva: No encontrado en {comparaciones} comparaciones")
        return None
    medio = (inicio + fin) // 2
    comparaciones += 1
    if pedidos[medio]["código"] == codigo:
        print(f"Búsqueda Binaria Recursiva: Encontrado en {comparaciones} comparaciones")
        return pedidos[medio]
    elif pedidos[medio]["código"] < codigo:
        return busqueda_binaria_recursiva(pedidos, codigo, medio + 1, fin, comparaciones)
    else:
        return busqueda_binaria_recursiva(pedidos, codigo, inicio, medio - 1, comparaciones)

# ========================
# PRUEBAS
# ========================
codigo_buscar = "P007"
print(f"\nBuscando código: {codigo_buscar}")
print("-" * 40)

resultado = busqueda_lineal(pedidos, codigo_buscar)
if resultado:
    print(f"Resultado: {resultado}\n")

resultado = busqueda_lineal_acotada(pedidos, codigo_buscar, 0, 10)
if resultado:
    print(f"Resultado: {resultado}\n")

resultado = busqueda_binaria_iterativa(pedidos, codigo_buscar)
if resultado:
    print(f"Resultado: {resultado}\n")

pedidos_ordenados = sorted(pedidos, key=lambda x: x["código"])
resultado = busqueda_binaria_recursiva(pedidos_ordenados, codigo_buscar, 0, len(pedidos_ordenados)-1)
if resultado:
    print(f"Resultado: {resultado}\n")

# ========================
# ANÁLISIS DE COMPLEJIDAD
# ========================
print("\nANÁLISIS DE COMPLEJIDAD:")
print("-" * 40)
print("Búsqueda Lineal:           O(n) - Peor caso recorre toda la lista")
print("Búsqueda Lineal Acotada:   O(k) - Solo recorre un rango definido")
print("Búsqueda Binaria Iterativa: O(log n) - Divide la lista a la mitad")
print("Búsqueda Binaria Recursiva: O(log n) - Igual pero con recursión")
