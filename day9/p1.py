if __name__ == "__main__":
    with open("input.txt", "r") as f: 
        data = f.readlines()
        data = [[int(a) for a in line.strip().split(',')] for line in data]

    from itertools import combinations

    max_area = 0
    for a,b in combinations(data, 2):
        area = abs((a[0] - b[0] + 1) * (a[1] - b[1] +1))
        if area > max_area:
            max_area = area

    print(max_area)
