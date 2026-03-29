
# =========================================
# QUEUE USING TWO STACKS (CON MENSAJES)
# =========================================

print("=== COLA (QUEUE) CON DOS PILAS ===")
print("Ingrese el número de consultas:")
print("Tipos de consulta:")
print("1 x -> Insertar x")
print("2   -> Eliminar")
print("3   -> Mostrar el primero")

in_stack = []
out_stack = []

q = int(input())

for _ in range(q):
    query = input("Ingrese la consulta: ").split()

    if query[0] == '1':
        in_stack.append(int(query[1]))

    elif query[0] == '2':
        if not out_stack:
            while in_stack:
                out_stack.append(in_stack.pop())
        if out_stack:
            out_stack.pop()

    elif query[0] == '3':
        if not out_stack:
            while in_stack:
                out_stack.append(in_stack.pop())
        if out_stack:
            print("Frente de la cola:", out_stack[-1])
        else:
            print("La cola está vacía")
# =========================================
# PREORDER TRAVERSAL (CON MENSAJES)
# =========================================

print("=== RECORRIDO PREORDER ===")
print("Orden: RAÍZ -> IZQUIERDA -> DERECHA\n")

def preOrder(root):
    if root is None:
        return
    
    print(root[0], end=" ")
    preOrder(root[1])
    preOrder(root[2])


# Árbol de ejemplo
print("Árbol de ejemplo:")
print("      1")
print("     / \\")
print("    2   3")
print("   / \\")
print("  4   5\n")

root = (1,
        (2,
         (4, None, None),
         (5, None, None)
        ),
        (3, None, None)
       )

print("Resultado del recorrido preorder:")
preOrder(root)
# =========================================
# KNIGHT IN A GRID (CON MENSAJES)
# =========================================

from collections import deque

print("=== CABALLO EN EL TABLERO ===")
print("El caballo se mueve en forma (M, N)")
print("Ingrese el número de casos:")

T = int(input())

for t in range(1, T+1):
    print(f"\n--- Caso {t} ---")
    
    print("Ingrese R C M N:")
    R, C, M, N = map(int, input().split())

    print("Ingrese número de casillas con agua:")
    W = int(input())

    water = set()
    print("Ingrese las posiciones con agua (x y):")
    for _ in range(W):
        x, y = map(int, input().split())
        water.add((x, y))

    visited = set()
    queue = deque()
    queue.append((0, 0))
    visited.add((0, 0))

    moves = set([
        (M, N), (M, -N), (-M, N), (-M, -N),
        (N, M), (N, -M), (-N, M), (-N, -M)
    ])

    even = 0
    odd = 0

    while queue:
        x, y = queue.popleft()
        count = 0

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in water:
                count += 1
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        if count % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"Resultado -> Case {t}: {even} {odd}")
