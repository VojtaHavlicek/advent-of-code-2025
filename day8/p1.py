from math import sqrt
from itertools import combinations
from operator import mul
from functools import reduce


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().strip().splitlines()
        data = [[int(s) for s in line.split(',')] for line in data]

    def _distance(x, y): 
        return sqrt(sum([(x[i]-y[i])**2 for i in range(len(x))]))
    
    sorted_edges = []
    for (ia, a), (ib, b) in combinations(enumerate(data), 2):
        sorted_edges.append((_distance(a,b), ia, ib))
    
    ordered_pairs = sorted(sorted_edges, key=lambda x: x[0])  # (distance, index1, index2)
    to_connect = 1000  # number of edges to connect all nodes
    k = 0 

    clusters = [{i} for i in range(len(data))]  # each point starts in its own cluster
    for _ in range(to_connect):
        _, ia, ib = ordered_pairs.pop(0)

        for ci, c in enumerate(clusters):
            if ia in c:
                cluster_a_index = ci
            if ib in c:
                cluster_b_index = ci

        if cluster_a_index != cluster_b_index:
            clusters[cluster_a_index] = clusters[cluster_a_index].union(clusters[cluster_b_index])
            clusters.pop(cluster_b_index)

    lengths = sorted([len(c) for c in clusters], reverse=True)
    print(reduce(mul, lengths[:3], 1))  # product of the sizes of the three largest clusters
    
   
        
