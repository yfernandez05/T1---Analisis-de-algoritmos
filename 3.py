# ========================
# PARTE 3: ALGORITMOS DE ORDENAMIENTO
# ========================

import copy

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
# ORDENAMIENTO BURBUJA
# ========================
def ordenamiento_burbuja(lista):
    datos = copy.deepcopy(lista)
    n = len(datos)
    comparaciones = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1
            if datos[j]["costo"] > datos[j+1]["costo"]:
                datos[j], datos[j+1] = datos[j+1], datos[j]
    print(f"Burbuja - Total comparaciones: {comparaciones}")
    return datos

# ========================
# ORDENAMIENTO POR SELECCIÓN
# ========================
def ordenamiento_seleccion(lista):
    datos = copy.deepcopy(lista)
    n = len(datos)
    comparaciones = 0
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            comparaciones += 1
            if datos[j]["costo"] < datos[minimo]["costo"]:
                minimo = j
        datos[i], datos[minimo] = datos[minimo], datos[i]
    print(f"Selección - Total comparaciones: {comparaciones}")
    return datos

# ========================
# ORDENAMIENTO POR INSERCIÓN
# ========================
def ordenamiento_insercion(lista):
    datos = copy.deepcopy(lista)
    comparaciones = 0
    for i in range(1, len(datos)):
        clave = datos[i]
        j = i - 1
        while j >= 0 and datos[j]["costo"] > clave["costo"]:
            comparaciones += 1
            datos[j+1] = datos[j]
            j -= 1
        comparaciones += 1
        datos[j+1] = clave
    print(f"Inserción - Total comparaciones: {comparaciones}")
    return datos

# ========================
# PRUEBAS Y COMPARACIÓN
# ========================
print("ORDENAMIENTO POR COSTO DE ENVÍO")
print("=" * 40)

print("\n1. BURBUJA:")
resultado_burbuja = ordenamiento_burbuja(pedidos)
for p in resultado_burbuja:
    print(f"  {p['código']} - {p['cliente']} - S/.{p['costo']}")

print("\n2. SELECCIÓN:")
resultado_seleccion = ordenamiento_seleccion(pedidos)
for p in resultado_seleccion:
    print(f"  {p['código']} - {p['cliente']} - S/.{p['costo']}")

print("\n3. INSERCIÓN:")
resultado_insercion = ordenamiento_insercion(pedidos)
for p in resultado_insercion:
    print(f"  {p['código']} - {p['cliente']} - S/.{p['costo']}")

# ========================
# ANÁLISIS COMPARATIVO
# ========================
print("\nANÁLISIS COMPARATIVO:")
print("-" * 40)
print("Burbuja:   O(n²) - Muchas comparaciones, poco eficiente")
print("Selección: O(n²) - Menos comparaciones que burbuja")
