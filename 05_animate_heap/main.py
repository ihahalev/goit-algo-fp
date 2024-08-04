from typing import Callable
from classes import Heap, Node
from tree_search import bfs_iterative, dfs_iterative
import networkx as nx
import matplotlib.pyplot as plt

def add_edges(graph:nx.DiGraph, node:Node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root:Node, search_func:Callable[[Node], list]|None=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if search_func:
        visited_nodes = search_func(tree_root)
        color_step = 255 // (len(visited_nodes) + 1)
        # step = (len(visited_nodes) + 1)//3
        colors = list()
        for node in tree.nodes(data=True):
            i = visited_nodes.index(node[1]["label"])
            color = f"#{color_step*i:02x}{color_step*i:02x}55"
            colors.append(color)
    else:
        colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

if __name__ == "__main__":
    # Heap creation from array of numbers
    array = [7, 12, 3, 5, 2, 15, 8, 11, 4, 20, 1, 6, 9, 14, 21, 22]
    heap = Heap(array)
    print("Original heap: ", heap)
    root = heap.build_tree()
    if root:
        draw_tree(root)

        result = dfs_iterative(root)
        print("Deep first search: ", result)

        result = bfs_iterative(root)
        print("Breadth first search: ", result)

        # Deep First Search Visualisation
        draw_tree(root, dfs_iterative)

        # Breadth First Search Visualisation
        draw_tree(root, bfs_iterative)
