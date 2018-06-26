from heapq import *
from utils import edges_to_adjacency_map


def prim_mst(graph):
    costs = {}
    parents = {}

    for v in graph:
        costs[v] = float('inf')
        parents[v] = None

    start = list(graph.keys())[0]
    costs[start] = 0

    visited = set()

    queue = [(0, start), ]

    while queue:
        cur = heappop(queue)[1]
        if cur not in visited:
            visited.add(cur)

            for v in graph[cur]:
                new_cost = graph[cur][v]
                if new_cost < costs[v] and v not in visited:
                    costs[v] = new_cost
                    parents[v] = cur

                heappush(queue, (costs[v], v))
            print(cur, parents)

    return parents


a, b, c, d, e, f = 'a', 'b', 'c', 'd', 'e', 'f'

edge_list = ((a, b, 5), (a, c, 6), (a, d, 4),
             (b, c, 1), (b, d, 2),
             (c, d, 2), (c, e, 5), (c, f, 3),
             (d, f, 4),
             (f, e, 4),
             )

g = edges_to_adjacency_map(edge_list, directed=False)


print(prim_mst(g))
