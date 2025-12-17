if __name__ == "__main__":
    with open("input.txt") as f:
        lines =  f.read().strip().splitlines()
        operators = lines[-1].split()
        operands = [[int(s) for s in line.split()] for line in lines[:-1]]

    number_of_problems = len(operators)
    results = [] 

    for col in range(number_of_problems):
        operator = operators[col]
        result = 1 if operator == '*' else 0

        for row in operands: 
            num = row[col]
            if operator == "*":
                result *= num
            elif operator == '+':
                result += num

        results.append(result)

    print(sum(results))




