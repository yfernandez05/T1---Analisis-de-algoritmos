def viaticos(monto):

    billetes = [200,100,50,20,10]
    resultado = {}

    for billete in billetes:
        cantidad = monto // billete

        if cantidad > 0:
            resultado[billete] = cantidad
            monto %= billete

    return resultado

print(viaticos(380))
print(viaticos(670))
print(viaticos(920))
