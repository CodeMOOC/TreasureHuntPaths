from itertools import tee


class PathCostFinder:

    def __init__(self):
        pass

    @staticmethod
    def __pairwise(iterable):
        "s -> (s0,s1), (s1,s2), (s2, s3), ..."
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    def pathCost(self, graph, path):
        """
        Returns the total cost of the provided path.
        Between each couple of vertexes the shortest past cost is taken.
        :param graph: an igraph graph
        :param path:  a sequence of indexes of the graph
        :return: the path total cost
        """
        total_cost = 0
        for v, w in self.__pairwise(path):
            cost_list = graph.shortest_paths_dijkstra(v, w, weights="weight")
            cost = sum(i[0] for i in cost_list)
            #print(cost)
            #print("{0} -> {1} cost {2}".format(v, w, cost))
            total_cost = total_cost + cost

        return total_cost
