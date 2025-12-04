def can_access_roll(x,y,map):
    neighbors = []
    
    # 1. get valid neigbors
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue

            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or ny >= len(map) or nx >= len(map[0]):
                continue
            
            neighbors.append((x+dx, y+dy))

    #print(f"Neighbors of {(x,y)}: {neighbors}")

    # 2. get the sum
    neighbor_sum = sum([(map[y][x] == '@') for x,y in neighbors])

    if neighbor_sum < 4:
        return True
    return False 
    
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        map = f.read().strip().split("\n")
        map = [list(row) for row in map]

    map_copy = [row.copy() for row in map]
        
    result = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '@':
                if can_access_roll(x,y,map):
                    result += 1
                    map_copy[y][x] = 'O'
    
    print(f"Can access {result} rolls")
