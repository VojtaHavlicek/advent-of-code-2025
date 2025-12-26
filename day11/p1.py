if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().strip().splitlines()
        dict_data = {}
        for line in data:
            line = line.split(':')
            dict_data[line[0]] = line[1].strip().split()
        data = dict_data

    paths = [['you']]
    final_paths = []

    while paths:
        current_path = paths.pop(0)
        last_node = current_path[-1]
        
        for out_node in data[last_node]:
            if out_node == 'out':
                final_paths.append(current_path + [out_node])
            else:
                paths.append(current_path + [out_node])

    print(len(final_paths))


        
           
                
         