
if __name__ == '__main__':

    state = 50
    zeros = 0

    with open('input.txt') as f:
        problem_input = f.read().strip()
    
    for instruction in problem_input.split():
        angle = int(instruction[1:])

        if instruction[0] == 'R':
            state += angle
        else:
            state -= angle

        state %= 100
        print(state)
        
        if state == 0:
            zeros += 1

    print('-------------')
    print(zeros)

    