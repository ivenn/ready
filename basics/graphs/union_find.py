from utils import edges_to_adjacency_map


def find_parent(parents, i):
    if not parents[i]:
        return i
    return find_parent(parents, parents[i])


def union(parents, x, y):
    x_root = find_parent(parents, x)
    y_root = find_parent(parents, y)
    parents[x_root] = y_root


def union_by_rank(parents, ranks, x, y):

    x_root = find_parent(parents, x)
    y_root = find_parent(parents, y)

    if ranks[x_root] < ranks[y_root]:
        parents[x_root] = y_root
    elif ranks[x_root] > ranks[y_root]:
        parents[y_root] = x_root
    else:
        parents[y_root] = x_root
        ranks[x_root] += 1


def is_cycle(graph):

    parents = [None] * len(graph)
    # ranks = [0] * len(graph)

    for i in graph:
        for j in graph[i]:
            x = find_parent(parents, i)
            y = find_parent(parents, j)
            if x == y:
                return True
            union(parents, x, y)

    return False


def test_is_cycle():
    g = edges_to_adjacency_map([(0, 1), (1, 2), (2, 0)], weighted=False)
    print(is_cycle(g))


if __name__ == "__main__":
    test_is_cycle()
