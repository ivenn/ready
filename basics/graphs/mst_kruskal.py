def adjacency_list_from_edge_list(edges):
    graph = {}

    for cost, from_v, to_v in edges:
        if from_v not in graph:
            graph[from_v] = {}
        if to_v not in graph:
            graph[to_v] = {}
        graph[from_v][to_v] = cost

    return graph


def find_set(parents, i):
    if parents[i] == i:
        return i
    else:
        return find_set(parents, parents[i])


def union(parents, ranks, x, y):
    xroot = find_set(parents, x)
    yroot = find_set(parents, y)

    if ranks[xroot] < ranks[yroot]:
        parents[xroot] = yroot
    elif ranks[xroot] > ranks[yroot]:
        parents[yroot] = xroot
    else:
        parents[yroot] = xroot
        ranks[xroot] += 1


def naive_union(parents, ranks, x, y):
    xroot = find_set(parents, x)
    yroot = find_set(parents, y)

    parents[xroot] = yroot


def kruskal_mst(edges):
    res_mst = []

    graph = adjacency_list_from_edge_list(edges)
    print(graph)
    sorted_edges = sorted(edges, key=lambda x: x[0])
    parents = {}
    ranks = {}

    # make sets
    for v in graph:
        parents[v] = v
        ranks[v] = 0

    for edge in sorted_edges:
        weight, u, v = edge

        x = find_set(parents, u)
        y = find_set(parents, v)

        if x != y:
            res_mst.append(edge)
            union(parents, ranks, x, y)

    print(parents)

    return res_mst


# weight, u, v
edge_list = [(1, 7, 6),
             (2, 8, 2),
             (2, 6, 5),
             (4, 0, 1),
             (4, 2, 5),
             (6, 8, 6),
             (7, 2, 3),
             (7, 7, 8),
             (8, 0, 7),
             (8, 1, 2),
             (9, 3, 4),
             (10, 5, 4),
             (11, 1, 7),
             (14, 3, 5),
             ]


print(kruskal_mst(edge_list))

