
# 🚀 Análisis y Diseño de Algoritmos: Documentación Técnica

Este repositorio contiene el compendio de estrategias algorítmicas, análisis de complejidad y documentación de ingeniería de software desarrollados durante el curso. Aquí se exploran desde métodos básicos incrementales hasta optimizaciones avanzadas mediante Programación Dinámica.

---

## 📂 Estructura del Repositorio

En las carpetas de este proyecto encontrarás la siguiente documentación detallada por cada tema:

* **Mapas de Flujo:** Lógica visual de los algoritmos implementados.
* **Diagramas de Usos y Usuarios:** Interacción del sistema con los actores finales.
* **Requerimientos:** Especificaciones funcionales y no funcionales.
* **Historias de Usuario:** Perspectiva del usuario final sobre las funcionalidades.
* **Análisis Cost/Time:** Evaluación de recursos vs. tiempo de ejecución.

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
1.  **Dividir:** Partir el problema.
2.  **Conquistar:** Resolver subproblemas.
3.  **Combinar:** Mezclar resultados.

### 5. Teorema Maestro
Método matemático para proporcionar una solución asintótica a las relaciones de recurrencia:
$$T(n) = aT(n/b) + f(n)$$
*Utilizado para determinar la eficiencia de algoritmos de Dividir y Conquistar de forma directa.*

### 6. Programación Dinámica (DP)
Optimización de algoritmos recursivos mediante el almacenamiento de resultados intermedios (Memoización o Tabulación) para evitar cálculos redundantes.

---

## 🛠️ Ingeniería de Software (Por cada módulo)

### 📋 Requerimientos e Historias de Usuario
| ID | Historia de Usuario | Requerimiento Relacionado |
|:---|:---|:---|
| HU01 | Como analista, quiero calcular promedios eficientemente. | El sistema debe usar DP para optimizar la suma de rangos. |
| HU02 | Como usuario, quiero ver quién aprobó la materia. | El sistema debe filtrar notas $\geq 3.0$ tras el cálculo. |

### 📊 Diagramas de Flujo y Usuarios
Cada carpeta técnica incluye un **Mapa de Flujo** que describe el ciclo de vida del dato y un **Mapa de Usuario** que detalla la experiencia desde la entrada (input) hasta el resultado (output).



### ⏳ Análisis de Costo / Tiempo (Cost vs Time)
Evaluación de la complejidad temporal frente al costo computacional:
* **Recursión Simple:** Costo de memoria alto (Stack).
* **DP:** Mayor costo inicial de memoria (Tablas), pero tiempo de ejecución significativamente menor en problemas complejos.

---

## 🚀 Instrucciones de Uso
1. Navega a la carpeta del tema de interés (ej. `/programacion-dinamica`).
2. Revisa el archivo `.py` o `.cpp` para ver la implementación.
3. Consulta el PDF de diagramas para entender la lógica de flujo y usuario.

---
**Desarrollado por:** [Tu Nombre]  
**Fecha:** 2026
