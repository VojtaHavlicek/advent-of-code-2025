if __name__ == "__main__":
    def _block_split(s, max_col_lengths): 
        result = [] 

        for col_len in max_col_lengths:
            result.append(s[:col_len])
            s = s[col_len+1:]

        return result

    with open("input.txt") as f:
        lines =  f.read().splitlines()
        operators = lines[-1].split()
        operands = [line.split() for line in lines[:-1]]
        max_col_lengths = [max([len(operands[row][col]) for row in range(len(operands))]) for col in range(len(operators))]
        block_split_operands = [_block_split(line, max_col_lengths) for line in lines[:-1]]
        print(block_split_operands)

    number_of_problems = len(operators)
    results = [] 

    def _parse_col(str_list):
        print(f"strlist {str_list}")
        max_len = max([len(s) for s in str_list])
        padded = str_list#[s.ljust(max_len, ' ') for s in str_list]
        parsed_numbers = ['' for _ in range(max_len)] 
        for s in padded:
            for k, d in enumerate(s):
                parsed_numbers[k] = parsed_numbers[k] + d

        return [int(n) for n in parsed_numbers]

    for col in range(number_of_problems):
        operator = operators[col]
        result = 1 if operator == '*' else 0

        parsed_column = _parse_col([block_split_operands[row][col] for row in range(len(operands))])

        print(parsed_column)

        for num in parsed_column: 
            if operator == "*":
                result *= num
            elif operator == '+':
                result += num

        results.append(result)

    print(sum(results))
