from collections import deque
from classes import Node

def dfs_iterative(vertex:Node, visited=None):
    visited = list()
    values = list()
    stack = [vertex]
    while stack:
        # get vertex from the stack
        vertex = stack.pop()

        if vertex not in visited:
            # add vertex to the visited
            visited.append(vertex)
            values.append(vertex.val)
            # add vertexes to the stack
            if vertex.right:
                stack.append(vertex.right)
            if vertex.left:
                stack.append(vertex.left)
    return values

def bfs_iterative(start:Node):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = list()
    values = list()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Додаємо вершину до множини відвіданих вершин
            visited.append(vertex)
            values.append(vertex.val)
            # Додаємо лівий і правий
            if vertex.left:
                queue.append(vertex.left)
            if vertex.right:
                queue.append(vertex.right)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return values
