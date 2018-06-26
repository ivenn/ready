from heapq import *
from utils import edges_to_adjacency_map


def dijkstra_shortest_path(graph, start, dest):

    def parents_to_path(parents, start, dest):
        path = [dest]
        v = dest
        while v != start:
            path.append(parents[v])
            v = parents[v]

        return list(reversed(path))

    parents = {}
    visited = set()
    costs = {k: float('inf') for k in graph}
    costs[start] = 0

    queue = [(0, start)]

    while queue:
        cur = heappop(queue)[1]

        if cur not in visited:
            visited.add(cur)

            if cur == dest:
                return costs[cur], parents_to_path(parents, start, dest)

            for v in graph[cur]:
                new_cost = graph[cur][v] + costs[cur]
                if new_cost < costs[v]:
                    costs[v] = new_cost
                    parents[v] = cur
                heappush(queue, (costs[v], v))

    return None


g = {
    'start': {'a': 4, 'b': 2},
    'a': {'dest': 3},
    'b': {'a': 1, 'dest': 6},
    'dest': {},
}


edges1 = [('a', 'b', 4), ('a', 'c', 5),
          ('b', 'd', 4), ('b', 'e', 4),
          ('c', 'e', 2), ('c', 'f', 2),
          ('d', 'g', 3), ('e', 'g', 1), ('f', 'g', 3)]


print(dijkstra_shortest_path(g, 'start', 'dest'))


print(dijkstra_shortest_path(edges_to_adjacency_map(edges1), 'a', 'g'))
