def get_divisors(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

def get_invalid_ids(start, end):
    invalid_ids = []
   
    for id in range(start, end + 1):
        strid = str(id)
        n = len(strid)
        divisors = get_divisors(n)

        print(f'Processing ID: {id} with divisors {divisors}')

        for d in divisors:
            if d == n:
                continue

            for k in range(0, n, d):
                if strid[k:k+d] != strid[:d]:
                    break
            else:
                print(f'Adding {id}')
                invalid_ids += [id]
                break

    return invalid_ids


if __name__ == '__main__':
    with open('input.txt', 'r') as f: 
       ranges = f.read().strip().split(',')

    invalid_ids = []
    for r in ranges: 
        ids = r.split('-')
        start = int(ids[0])
        end = int(ids[1])
        invalid_ids += get_invalid_ids(start=start, end=end)

    
    print(f"sum: {sum(invalid_ids)}")
