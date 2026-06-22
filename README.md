# Evaluación T1 - Análisis de Algoritmos y Estrategias de Programación

Este repositorio contiene la resolución técnica e implementación en Python de los 6 ejercicios prácticos correspondientes a la **Evaluación T1** del curso.

---

## Estructura de la Solución

### Parte 1: Tipos Estructurados, Registros y Cadenas
* **Actividad 1:** Diseño de una base de datos logística de 15 pedidos utilizando una estructura de **lista de diccionarios**.
    * *Función incluida:* `buscar_cliente(texto)` (Búsqueda parcial insensible a mayúsculas/minúsculas).

### Parte 2: Algoritmos de Búsqueda
* **Actividad 2:** Implementación y comparación de tiempos/pasos para localizar un pedido mediante su identificador único.
    * `busqueda_lineal(pedidos, codigo)` — Complejidad: $O(n)$
    * `busqueda_lineal_acotada(pedidos, codigo, inicio, fin)` — Complejidad: $O(k)$
    * `busqueda_binaria_iterativa(pedidos, codigo)` — Complejidad: $O(\log n)$
    * `busqueda_binaria_recursiva(pedidos, codigo, inicio, fin)` — Complejidad: $O(\log n)$

### Parte 3: Algoritmos de Ordenamiento
* **Actividad 3:** Organización y ordenamiento financiero de los pedidos en función del costo de envío.
    * `ordenamiento_burbuja(lista)` — Complejidad: $O(n^2)$
    * `ordenamiento_seleccion(lista)` — Complejidad: $O(n^2)$
    * `ordenamiento_insercion(lista)` — Complejidad: $O(n^2)$ (El más eficiente para listas cortas).

### Parte 4: Algoritmos Voraces (Greedy)
* **Actividad 4:** Optimización del desglose de viáticos para conductores utilizando la menor cantidad posible de billetes de alta denominación (S/. 200, S/. 100, S/. 50, S/. 20, S/. 10).
    * `viaticos(monto)` — Resolución vorazizada aplicable a sistemas monetarios canónicos.

### Parte 5: Ruta de Entrega y Árbol de Recubrimiento Mínimo (MST)
* **Actividad 5:** Optimización e interconexión económica de los 6 centros de distribución nacionales.
    * `prim(grafo, inicio)` — Implementación del **Algoritmo de Prim** mediante montículos binarios (`heapq`) para minimizar costos logísticos totales.

### Parte 6: Exploración por Backtracking
* **Actividad 6:** Resolución del problema de distribución espacial y horaria en la zona industrial.
    * `resolver(tablero, col)` — Implementación basada en el **Problema de las 8 Reinas** para hallar configuraciones válidas sin generar colisiones ni cruces de rutas.
