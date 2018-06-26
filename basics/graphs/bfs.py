from Queue import Queue
from utils import test_graphs


WHITE = 'WHITE'
GRAY = 'GRAY'
BLACK = 'BLACK'


def bfs_cormen(graph, start):
    start.dist = 0
    start.color = GRAY
    start.parent = None

    for v in [v for v in graph if v is not start]:
        v.color = WHITE
        v.dist = None
        v.parent = None

    q = Queue()
    q.put(start)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if v.color == WHITE:
                v.color = GRAY
                v.dist = u.dist + 1
                v.parent = u
                q.put(v)
        u.color = BLACK
        print(u)


def bfs(graph, start):

    queue = Queue()
    queue.put(start)

    levels = {start: 0}
    visited = {start, }

    while not queue.empty():
        v = queue.get()
        neighbours = graph[v]

        to_do = [n for n in neighbours if n not in visited]

        for neighbour in to_do:
            queue.put(neighbour)
            visited.add(neighbour)
            levels[neighbour] = levels[v] + 1

    return levels


def main():
    for g in test_graphs:
        start = sorted(g.keys(), key=lambda vertex: vertex.val)[0]
        bfs_cormen(g, start)
        print("-" * 50)


if __name__ == "__main__":
    main()

