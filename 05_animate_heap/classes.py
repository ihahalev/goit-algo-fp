import uuid
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left:Node|None = None
        self.right:Node|None = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла

class Heap:
    def __init__(self, array: list):
        self.heap = array
        heapq.heapify(self.heap)

    def __str__(self):
        return str(self.heap)

    def is_empty(self):
        return not bool(self.heap)

    def build_children(self, i, root:Node):
        arr = self.heap
        if 2*i+1 < len(arr):
            root.left = Node(arr[2*i+1])
            self.build_children(2*i+1, root.left)
        if 2*i+2 < len(arr):
            root.right = Node(arr[2*i+2])
            self.build_children(2*i+2, root.right)

    def build_tree(self):
        if self.is_empty():
            return
        root = Node(self.heap[0])
        self.build_children(0, root)
        return root
