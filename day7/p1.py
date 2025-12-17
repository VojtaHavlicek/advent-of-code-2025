if __name__ == "__main__":
    with open("input.txt", "r") as f:
        problem_input = f.readlines() 
        problem_input = [list(line.strip()) for line in problem_input]

    initial = problem_input[0]

    beams = [] 
    for symbol in initial: 
        if symbol == '.': 
            beams.append(0)
        elif symbol == 'S': 
            beams.append(1) 

    manifold = problem_input[1:]
    num_splits = 0 

    for row in manifold: 
        post_beams = beams

        for index, cell in enumerate(row):
            if cell == '^': 
                if beams[index] == 1:
                    num_splits += 1 
                    if index > 0:
                        post_beams[index - 1] = 1
                    if index < len(post_beams) -1: 
                        post_beams[index + 1] = 1
                    post_beams[index] = 0

        beams = post_beams

    print(num_splits)

