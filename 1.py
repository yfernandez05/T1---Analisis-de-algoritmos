# ==========================
# BASE DE DATOS DE PEDIDOS
# ==========================

pedidos = [
    {"codigo":"P001","cliente":"Juan Perez","ciudad":"Lima","peso":10,"prioridad":"Alta","costo":80},
    {"codigo":"P002","cliente":"Maria Lopez","ciudad":"Arequipa","peso":8,"prioridad":"Media","costo":60},
    {"codigo":"P003","cliente":"Carlos Diaz","ciudad":"Cusco","peso":12,"prioridad":"Alta","costo":90},
    {"codigo":"P004","cliente":"Ana Torres","ciudad":"Piura","peso":5,"prioridad":"Baja","costo":40},
    {"codigo":"P005","cliente":"Luis Ramos","ciudad":"Trujillo","peso":7,"prioridad":"Media","costo":55},
    {"codigo":"P006","cliente":"Jose Ruiz","ciudad":"Chiclayo","peso":9,"prioridad":"Alta","costo":70},
    {"codigo":"P007","cliente":"Pedro Soto","ciudad":"Lima","peso":11,"prioridad":"Media","costo":85},
    {"codigo":"P008","cliente":"Lucia Vega","ciudad":"Cusco","peso":6,"prioridad":"Alta","costo":65},
    {"codigo":"P009","cliente":"Miguel Cruz","ciudad":"Piura","peso":13,"prioridad":"Baja","costo":95},
    {"codigo":"P010","cliente":"Rosa Flores","ciudad":"Arequipa","peso":4,"prioridad":"Media","costo":35},
    {"codigo":"P011","cliente":"Jorge Leon","ciudad":"Lima","peso":15,"prioridad":"Alta","costo":100},
    {"codigo":"P012","cliente":"Patricia Gil","ciudad":"Trujillo","peso":8,"prioridad":"Media","costo":50},
    {"codigo":"P013","cliente":"Diego Silva","ciudad":"Cusco","peso":9,"prioridad":"Alta","costo":75},
    {"codigo":"P014","cliente":"Sandra Moya","ciudad":"Piura","peso":6,"prioridad":"Baja","costo":45},
    {"codigo":"P015","cliente":"Fernando Paz","ciudad":"Chiclayo","peso":10,"prioridad":"Media","costo":68}
]

# ==========================
# BUSQUEDA POR CLIENTE
# ==========================

def buscar_cliente(texto):
    resultados = []

    for pedido in pedidos:
        if texto.lower() in pedido["cliente"].lower():
            resultados.append(pedido)

    return resultados

# ==========================
# BUSQUEDAS POR CODIGO
# ==========================

def busqueda_lineal(lista, codigo):
    for i in range(len(lista)):
        if lista[i]["codigo"] == codigo:
            return i
    return -1


def busqueda_lineal_acotada(lista, codigo, limite):
    for i in range(min(limite, len(lista))):
        if lista[i]["codigo"] == codigo:
            return i
    return -1


def binaria_iterativa(lista, codigo):

    lista_ordenada = sorted(lista, key=lambda x: x["codigo"])

    inicio = 0
    fin = len(lista_ordenada) - 1

    while inicio <= fin:

        medio = (inicio + fin) // 2

        if lista_ordenada[medio]["codigo"] == codigo:
            return lista_ordenada[medio]

        elif lista_ordenada[medio]["codigo"] < codigo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None

# ==========================
# ORDENAMIENTOS
# ==========================

def burbuja(lista):

    lista = lista.copy()

    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):

            if lista[j]["costo"] > lista[j+1]["costo"]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


def seleccion(lista):

    lista = lista.copy()

    n = len(lista)

    for i in range(n):

        minimo = i

        for j in range(i+1, n):

            if lista[j]["costo"] < lista[minimo]["costo"]:
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]

    return lista


def insercion(lista):

    lista = lista.copy()

    for i in range(1, len(lista)):

        actual = lista[i]
        j = i - 1

        while j >= 0 and lista[j]["costo"] > actual["costo"]:
            lista[j+1] = lista[j]
            j -= 1

        lista[j+1] = actual

    return lista

# ==========================
# MOSTRAR PEDIDOS
# ==========================

def mostrar(lista):

    print("\nLISTA DE PEDIDOS\n")

    for pedido in lista:
        print(
            pedido["codigo"],
            pedido["cliente"],
            pedido["ciudad"],
            "Costo:", pedido["costo"]
        )

# ==========================
# MENU PRINCIPAL
# ==========================

while True:

    try:

        print("\n========== UPN CARGO SAC ==========")
        print("1. Buscar cliente por nombre")
        print("2. Busqueda Lineal por codigo")
        print("3. Busqueda Lineal Acotada")
        print("4. Busqueda Binaria Iterativa")
        print("5. Ordenamiento Burbuja")
        print("6. Ordenamiento Seleccion")
        print("7. Ordenamiento Insercion")
        print("8. Mostrar todos los pedidos")
        print("9. Salir")

        opcion = int(input("\nSeleccione una opcion: "))

        if opcion == 1:

            nombre = input("Ingrese nombre o parte del nombre: ")

            resultado = buscar_cliente(nombre)

            if resultado:
                mostrar(resultado)
            else:
                print("Cliente no encontrado")

        elif opcion == 2:

            codigo = input("Ingrese codigo: ")

            pos = busqueda_lineal(pedidos, codigo)

            if pos != -1:
                print("\nPedido encontrado:")
                print(pedidos[pos])
            else:
                print("Pedido no encontrado")

        elif opcion == 3:

            codigo = input("Ingrese codigo: ")

            try:
                limite = int(input("Ingrese limite de busqueda: "))
            except ValueError:
                print("El limite debe ser un numero.")
                continue

            pos = busqueda_lineal_acotada(
                pedidos,
                codigo,
                limite
            )

            if pos != -1:
                print("\nPedido encontrado:")
                print(pedidos[pos])
            else:
                print("Pedido no encontrado")

        elif opcion == 4:

            codigo = input("Ingrese codigo: ")

            resultado = binaria_iterativa(
                pedidos,
                codigo
            )

            if resultado:
                print("\nPedido encontrado:")
                print(resultado)
            else:
                print("Pedido no encontrado")

        elif opcion == 5:

            mostrar(burbuja(pedidos))

        elif opcion == 6:

            mostrar(seleccion(pedidos))

        elif opcion == 7:

            mostrar(insercion(pedidos))

        elif opcion == 8:

            mostrar(pedidos)

        elif opcion == 9:

            print("Programa finalizado.")
            break

        else:

            print("Debe elegir una opcion entre 1 y 9.")

    except ValueError:

        print("Error: Debe ingresar un numero valido.")

    except KeyboardInterrupt:

        print("\nPrograma interrumpido por el usuario.")
        break

    except Exception as e:

        print("Ocurrio un error inesperado:", e)