
# 🧪 Pre Parcial Práctico 02

**Estructuras de Datos y Algoritmos**

---

## 📌 Información General

Este repositorio contiene la solución al **Pre Parcial Práctico 02**, donde se desarrollan tres problemas fundamentales relacionados con estructuras de datos y algoritmos:

* Uso de pilas para simular una cola
* Recorridos de árboles binarios
* Recorridos en grafos (BFS) aplicados a una cuadrícula

---

## 📂 Estructura del Proyecto

```
Preparcial-semana-10/
│
├── queue_two_stacks.py
├── preorder_traversal.py
├── knight_grid.py
└── README.md
```

---

## 🟢 Ejercicio 1: Queue usando Two Stacks

### 📖 Descripción

Se implementa una cola (FIFO) utilizando dos pilas (LIFO).

Se soportan las siguientes operaciones:

* `1 x` → Insertar elemento en la cola
* `2` → Eliminar el elemento del frente
* `3` → Mostrar el elemento del frente

### ⚙️ Lógica

Se utilizan dos listas:

* `in_stack`: para insertar elementos
* `out_stack`: para eliminar y consultar el frente

Cuando `out_stack` está vacío, se transfieren los elementos desde `in_stack`.

### ⏱ Complejidad

* Tiempo amortizado: **O(1)** por operación
* Peor caso: **O(n)**

---

## 🟢 Ejercicio 2: Preorder Traversal

### 📖 Descripción

Se implementa el recorrido **Preorder** de un árbol binario.

### 🔁 Orden del recorrido

```
RAÍZ → IZQUIERDA → DERECHA
```

### ⚙️ Lógica

Se utiliza recursión para:

1. Procesar el nodo actual
2. Recorrer el subárbol izquierdo
3. Recorrer el subárbol derecho

### ⏱ Complejidad

* Tiempo: **O(n)**
  (donde n es el número de nodos)

---

## 🔴 Ejercicio 3: Knight in a Grid

### 📖 Descripción

Se simula el movimiento de un caballo en una cuadrícula de tamaño `R x C`, con movimientos personalizados `(M, N)`.

El objetivo es:

* Recorrer todas las casillas alcanzables desde `(0,0)`
* Clasificar cada casilla como:

  * **Par** → número de movimientos posibles es par
  * **Impar** → número de movimientos posibles es impar

### ⚙️ Lógica

Se utiliza un recorrido **BFS (Breadth-First Search)**:

* Se usa una cola para explorar el grid
* Se evitan casillas con agua
* Se controla qué nodos ya fueron visitados

### ⏱ Complejidad

* Tiempo: **O(R × C)**
* Espacio: **O(R × C)**

---

## ▶️ Cómo ejecutar

Cada archivo se puede ejecutar de forma independiente:

```bash
python queue_two_stacks.py
python preorder_traversal.py
python knight_grid.py
```

---

## 🧠 Conceptos Aplicados

* Pilas (Stacks)
* Colas (Queues)
* Recursión
* Árboles binarios
* BFS (Breadth-First Search)
* Manejo de estructuras de datos en Python

---

## 👨‍💻 Autor

**Santiago Echeverría**
Estudiante de Ingeniería de Sistemas

---

## ✅ Conclusión

Este laboratorio permite aplicar conceptos clave de estructuras de datos y algoritmos, fortaleciendo habilidades en:

* Diseño de soluciones eficientes
* Uso adecuado de estructuras
* Resolución de problemas tipo competencia

---
