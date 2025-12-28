from collections import defaultdict, deque

def topo_sort(data):
    """ Topological sort using Kahn's algorithm."""
    indegrees = defaultdict(int)

    # Count in-degrees:
    for node, outs in data.items():
        indegrees[node] += 0
        for out in outs:
            indegrees[out] += 1

    # No prerequisites:
    noprereq = deque([node for node, degree in indegrees.items() if degree == 0])

    # Nice!!! 
    order = deque()
    while noprereq:
        node = noprereq.popleft()
        order.append(node)

        for out in data.get(node, []):
            indegrees[out] -= 1
            if indegrees[out] == 0:
                noprereq.append(out)

    if len(order) != len(indegrees):
        raise ValueError("Graph has at least one cycle")
    
    return order

def count_paths(start='svr', 
                end='out', 
                data=None):
    """
    Counts paths from start to end. 
    """

    innodes = defaultdict(list)
    # Count in-degrees:
    for node, outs in data.items():
        for out in outs:
            innodes[out].append(node) # <--- append innodes

    memo = {}
    nodes = topo_sort(data)
    for node in nodes:
        if node == start:
            memo[node] = 1
        else:
            memo[node] = sum(memo.get(in_node, 0) for in_node in innodes[node])

    return memo.get(end, 0)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().strip().splitlines()
        dict_data = {}
        for line in data:
            line = line.split(':')
            dict_data[line[0]] = line[1].strip().split()
        data = dict_data

    print(count_paths('svr', 'fft', data)*count_paths('fft', 'dac',data)*count_paths('dac', 'out',data))