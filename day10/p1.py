import re
from itertools import combinations

if __name__ == "__main__":
    cases = []
    with open('input.txt', 'r') as f:
        data = f.readlines()

        for k in range(len(data)):
            diagram = re.findall('\[.*\]', data[k])[0].strip('[]')
            buttons = re.findall('\(\d[,\d]*\)', data[k])
            reqs = re.findall('\{.*\}', data[k])[0].strip('{}').split(',')
            cases.append((diagram, buttons, reqs))

    def _decode(c):
        if c == '#':
            return 1
        return 0

    total_lenght = 0 
    for diagram, buttons, reqs in cases:
        config = [_decode(k) for k in list(diagram)]
        n = len(config)

        button_vectors = [] 

        for b in buttons:
            button_vector = [0 for _ in range(n)]
            indices = [int(x) for x in b.strip('()').split(',')]
            for idx in indices:
                button_vector[idx] = 1
            
            button_vectors.append(button_vector)

        # iterate over bitstrings with increasing hamming weight

        found_solution = False 
        for weight in range(len(button_vectors) + 1):
            for combo in combinations(range(len(button_vectors)), weight):
                test_vector = [0 for _ in range(n)]
                for btn_idx in combo:
                    for i in range(n):
                        test_vector[i] ^= button_vectors[btn_idx][i]
                
                if test_vector == config:
                    found_solution = True
                    break 
            if found_solution:
                break

        total_lenght += len(combo)
    
    print("Total lenght:", total_lenght)
                