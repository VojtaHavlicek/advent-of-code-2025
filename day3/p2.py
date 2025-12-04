def get_largest_joltage(joltage: str, digits = 12) -> int:
    max_num = ''
    max_index = -1

    while len(max_num) < digits:
        right_bound = len(joltage) - (digits - len(max_num)) + 1
        left_bound = max_index + 1
        max_index, digit = max(enumerate(joltage[left_bound:right_bound]), key=lambda x: int(x[1]))
        max_index += left_bound
        max_num = max_num + str(digit)

    return int(max_num)

            
if __name__ == "__main__":
    with open('input.txt', 'r') as f: 
        joltages = f.readlines()
        joltages = [joltage.strip() for joltage in joltages]
    
    outputs = []
    for joltage in joltages:
        outputs.append(get_largest_joltage(joltage))
        
    print(sum(outputs))