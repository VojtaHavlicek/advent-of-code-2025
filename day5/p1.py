if __name__ == "__main__":
    with open("input.txt", "r") as f: 
        data = f.read().strip().split("\n\n")
        ranges = data[0].split('\n')
        ids = data[1].split('\n')

    # 1. Is there a nice way to process the intervals? 
    fresh = 0 
    for id in ids: 
        for range in ranges: 
            left, right = range.split('-')

            if int(left) <= int(id) <= int(right):
                fresh += 1
                break

    print(f"Number of fresh ids: {fresh}")



    