def get_invalid_ids(start, end):
    invalid_ids = []
   
    for id in range(start, end + 1):
        strid = str(id)
        n = len(strid)
        if n % 2 == 1:
            continue

        if strid[:n//2] == strid[n//2:]: 
            invalid_ids += [id]

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

    
    print(sum(invalid_ids))



   