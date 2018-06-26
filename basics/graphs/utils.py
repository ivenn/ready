def edges_to_adjacency_map(edges, directed=True, weighted=True):
    graph = {}
    if weighted:
        for from_v, to_v, cost in edges:
            if from_v not in graph:
                graph[from_v] = {}
            if to_v not in graph:
                graph[to_v] = {}
            graph[from_v][to_v] = cost
            if not directed:
                graph[to_v][from_v] = cost
    else:
        for from_v, to_v in edges:
            if from_v not in graph:
                graph[from_v] = []
            if to_v not in graph:
                graph[to_v] = []
            graph[from_v].append(to_v)

    return graph


class Vertex:

    def __init__(self, val):
        self.val = val
        self.color = None
        self.parent = None
        self.dist = None
        self.dis_t = None
        self.fin_t = None

    def __repr__(self):
        if self.dis_t:
            return "V(%s, dis_t=%s, fin_t=%s)" % (self.val, self.dis_t, self.fin_t)
        if self.dist:
            return "V(%s, dist=%s)" % (self.val, self.dist)
        else:
            return "V(%s)" % self.val


v1, v2, v3, v4, v5, v6, v7 = Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5), Vertex(6), Vertex(7)


g0 = {v1: [v2, v5],
      v2: [v1, v5, v3, v4],
      v3: [v2, v4],
      v4: [v2, v5, v3],
      v5: [v4, v1, v2]
      }

g_line = {v1: [v2, ],
          v2: [v1, v3],
          v3: [v2, v4],
          v4: [v3, v5],
          v5: [v4, ]
          }

g_circle = {v1: [v2, v5],
            v2: [v1, v3],
            v3: [v2, v4],
            v4: [v3, v5],
            v5: [v4, v1]
            }

g_man = {v1: [v3],
         v2: [v3],
         v3: [v1, v2, v4],
         v4: [v3],
         v5: [v3, v6, v7],
         v6: [v5],
         v7: [v5]
         }

g_broken = {v1: [v2, v3],
            v2: [v1, v3],
            v3: [v1, v3],
            v4: [v5, v6],
            v5: [v4, v6],
            v6: [v4, v6],
            }

test_graphs = [g0, g_line, g_circle, g_man, g_broken]


if __name__ == "__main__":
    print(test_graphs)
