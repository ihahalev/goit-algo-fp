import networkx as nx
import math
import graph
import heapq
G:nx.Graph = graph.G

def dijkstra(graph:nx.Graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = [(0, start)]

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_distance, current_vertex = heapq.heappop(unvisited)

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if current_distance == float('infinity'):
            break

        neighbors = graph[current_vertex]
        for neighbor, param in neighbors.items():
            distance = current_distance + param['weight']

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Наповнюємо купу новими вершинами із сусідніх
                heapq.heappush(unvisited, (distance, neighbor))

    return distances

def main():
    pos = nx.get_node_attributes(G, "pos")
    H = G.copy()

    # Calculating the distances between the nodes as edge's weight.
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            if H.has_edge(i,j):
                H[i][j]['weight'] = math.hypot(pos[i][0] - pos[j][0], pos[i][1] - pos[j][1])

    start = 0
    results = dijkstra(H, start)
    max = 0
    vertex = start
    for res in results.items():
        print(res)
        if res[1] > max:
            max = res[1]
            vertex=res[0]
    vertexs = []
    for res in results.items():
        if res[1] == max:
            vertexs.append(res[0])
    print(f"Найдовший шлях з вершини {start} до {f'вершин {vertexs}' if len(vertexs)>1 else f'вершини {vertex}'}, що складає {max}")

if __name__ == "__main__":
    main()
