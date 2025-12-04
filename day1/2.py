if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        problem_input = f.readlines()

    state = 50
    zeros = 0

    for instruction in problem_input: 
        dir = 1 if instruction[0] == 'R' else -1
        angle = int(instruction[1:])

        dzeros = angle // 100 # number of whole revs
        angle = angle % 100  # remainder 

        final_state = state + dir*angle

        if (state > 0 and final_state < 0) or final_state >= 100 or final_state == 0:
            dzeros += 1

        print(f"{state}-({dir*angle})->{final_state%100}:{dzeros}")
        state = final_state % 100
        zeros += dzeros
    print('-------------')
    print(zeros)