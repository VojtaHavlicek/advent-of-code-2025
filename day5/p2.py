if __name__ == "__main__":
    with open("input.txt", "r") as f: 
        data = f.read().strip().split("\n\n")
        ranges = data[0].split('\n')
        ids = data[1].split('\n')

    
    intervals = []
    for r in ranges: 
        left, right = r.split('-')
        intervals.append((int(left), int(right)))

    intervals.sort(key=lambda x: x[0])

    # Merging
    k = 0 
    while k < len(intervals) - 1:
        left, right = intervals[k]

        j = k + 1
        while j < len(intervals) and right >= intervals[j][0] :
            right = max(right, intervals[j][1])
            j += 1
        
        intervals[k] = (left, right)
        intervals = intervals[:k+1] + intervals[j:] # Remove merged intervals

        if j == k + 1:
            k += 1

    ids = 0
    for interval in intervals:
        ids += interval[1] - interval[0] + 1

    print(f"Number of ids: {ids}")



    