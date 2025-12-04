def get_largest_joltage(joltage: str) -> int:
    maxnum = -1
    for k, d1 in enumerate(joltage):
        for d2 in joltage[k+1:]:
            num = int(d1+d2)
            if num > maxnum: 
                maxnum = num

    return maxnum

            
if __name__ == "__main__":
    with open('input.txt', 'r') as f: 
        joltages = f.readlines()
        joltages = [joltage.strip() for joltage in joltages]
    
    outputs = []
    for joltage in joltages:
        outputs.append(get_largest_joltage(joltage))
        
    print(sum(outputs))