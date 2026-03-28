# 🚀 Análisis y Diseño de Algoritmos: Documentación Técnica

Este repositorio contiene el contenido de estrategias algorítmicas, análisis de complejidad y documentación de ingeniería de software desarrollados durante el curso. Aquí se exploran desde métodos básicos incrementales hasta optimizaciones avanzadas mediante Programación Dinámica y estructuras jerárquicas como los árboles.

---

## 📂 Estructura del Repositorio

En las carpetas de este proyecto encontrarás la siguiente documentación detallada por cada tema:

* **Mapas de Flujo:** Lógica visual de los algoritmos implementados.
* **Diagramas de Usos y Usuarios:** Interacción del sistema con los actores finales.
* **Requerimientos:** Especificaciones funcionales y no funcionales.
* **Historias de Usuario:** Perspectiva del usuario final sobre las funcionalidades.
* **Análisis Cost/Time:** Evaluación de recursos vs. tiempo de ejecución.
* **Codigo funciaonla 

---

## 🧠 Temas del Ensayo y Contenido Académico

### 1. Estrategia Incremental

Análisis de algoritmos que construyen la solución un paso a la vez.

* **Enfoque:** Resolución secuencial (ej. *Insertion Sort*).
* **Contenido:** Documentación sobre cómo el crecimiento de los datos afecta la ejecución lineal.

### 2. Análisis Asintótico

Estudio de la eficiencia de los algoritmos en el límite, cuando el tamaño de la entrada $n$ tiende al infinito.

* **Notaciones:** $O(n)$ (Cota superior), $\Omega(n)$ (Cota inferior) y $\Theta(n)$ (Cota ajustada).

### 3. Recursión

Implementación de funciones que se llaman a sí mismas para resolver problemas mediante una estructura de "caso base" y "caso recursivo".

### 4. Dividir y Conquistar (Divide and Conquer)

Técnica basada en desglosar un problema complejo en subproblemas independientes más simples.

1. **Dividir:** Partir el problema.
2. **Conquistar:** Resolver subproblemas.
3. **Combinar:** Mezclar resultados.

### 5. Teorema Maestro

Método matemático para proporcionar una solución asintótica a las relaciones de recurrencia:
$$T(n) = aT(n/b) + f(n)$$

### 6. Programación Dinámica (DP)

Optimización de algoritmos recursivos mediante el almacenamiento de resultados intermedios (Memoización o Tabulación) para evitar cálculos redundantes.

---

## 📚 Contenido por Semanas

### 📌 Semana 7: Pilas y Colas

Estructuras de datos fundamentales para el manejo de información en orden específico.

* **Pilas (Stacks):**

  * Estructura LIFO (Last In, First Out)
  * Operaciones: push, pop, peek
  * Aplicaciones: evaluación de expresiones, recursión

* **Colas (Queues):**

  * Estructura FIFO (First In, First Out)
  * Operaciones: enqueue, dequeue
  * Aplicaciones: manejo de procesos, simulaciones

---

### 📌 Semana 8: Árboles y Búsqueda Binaria

* **Árboles (BST - Binary Search Tree):**

  * Estructura jerárquica de datos
  * Inserción, búsqueda y recorridos (preorden, inorden, postorden)
  * Organización eficiente de datos

* **Búsqueda Binaria:**

  * Algoritmo eficiente para listas ordenadas
  * Complejidad: $O(\log n)$

---

### 📌 Semana 9: Árboles y Simulación de Arenas

#### 🌳 Árboles

Se profundizó en el uso de árboles binarios como estructura fundamental para organizar datos jerárquicos.

* **Conceptos clave:**

  * Nodo, raíz, hojas, altura y profundidad
  * Árbol binario y árbol binario de búsqueda (BST)

* **Recorridos:**

  * **Preorden:** Raíz → Izquierda → Derecha
  * **Inorden:** Izquierda → Raíz → Derecha
  * **Postorden:** Izquierda → Derecha → Raíz

* **Búsquedas:**

  * **DFS (Depth First Search):** Exploración en profundidad
  * **BFS (Breadth First Search):** Exploración por niveles

* **Complejidad:**

  * Mejor caso: $O(\log n)$
  * Peor caso: $O(n)$

---

#### 🏜️ Simulación de Arenas

Se implementó una simulación basada en estructuras de datos para modelar procesos dinámicos.

* **Características:**

  * Uso de colas para gestionar eventos
  * Procesamiento secuencial de acciones
  * Control de estados y cambios en el sistema

* **Objetivo:**
  Representar escenarios donde múltiples elementos interactúan en un orden específico, aplicando lógica algorítmica.

---

## 🛠️ Ingeniería de Software (Por cada módulo)

### 📋 Requerimientos e Historias de Usuario

| ID   | Historia de Usuario                                      | Requerimiento Relacionado                                   |
| :--- | :------------------------------------------------------- | :---------------------------------------------------------- |
| HU01 | Como analista, quiero calcular promedios eficientemente. | El sistema debe usar DP para optimizar la suma de rangos.   |
| HU02 | Como usuario, quiero ver quién aprobó la materia.        | El sistema debe filtrar notas ≥ 3.0 tras el cálculo.        |
| HU03 | Como usuario, quiero gestionar datos con pilas y colas.  | El sistema debe implementar estructuras LIFO y FIFO.        |
| HU04 | Como usuario, quiero buscar datos rápidamente.           | El sistema debe implementar búsqueda binaria y árboles BST. |
| HU05 | Como usuario, quiero recorrer estructuras tipo árbol.    | El sistema debe implementar DFS y BFS.                      |

---

## 📊 Diagramas de Flujo y Usuarios

Cada carpeta técnica incluye un **Mapa de Flujo** que describe el ciclo de vida del dato y un **Mapa de Usuario** que detalla la experiencia desde la entrada (input) hasta el resultado (output).

---

## ⏳ Análisis de Costo / Tiempo (Cost vs Time)

Evaluación de la complejidad temporal frente al costo computacional:

* **Recursión Simple:** Costo de memoria alto (Stack).
* **Programación Dinámica:** Mayor uso de memoria, menor tiempo de ejecución.
* **Pilas y Colas:** Operaciones en $O(1)$.
* **Árboles BST:**

  * Mejor caso: $O(\log n)$
  * Peor caso: $O(n)$
* **Búsqueda Binaria:** $O(\log n)$

---

## 🎥 Video Explicativo

👉 **[Agregar aquí el link del video]**

---

## 🚀 Instrucciones de Uso

1. Navega a la carpeta del tema de interés.
2. Revisa el archivo `.py` o `.ipynb` para ver la implementación.
3. Consulta el PDF para entender los diagramas.

---

## 👤 Autor

**Santiago Echeverría**

## 📅 Fecha

2026

