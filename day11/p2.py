from collections import defaultdict, deque

def topo_sort(data):
    """ Topological sort using Kahn's algorithm."""
    indegrees = defaultdict(int)

    for node, outs in data.items():
        indegrees[node] += 0
        for out in outs:
            indegrees[out] += 1

    noprereq = deque([node for node, degree in indegrees.items() if degree == 0])

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

    memo = defaultdict(int)
    memo[start] = 1

    nodes = topo_sort(data)
    for node in nodes:
        if memo[node] == 0:
            continue

        for out in data.get(node, []):
            memo[out] += memo[node]
       
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