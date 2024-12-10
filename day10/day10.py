import time
import os

def read_input(file_path):
    with open(file_path, 'r') as input_file:
        return [[int(digit) for digit in line] for line in input_file.read().splitlines()]
    
def find_head(grid):
    head=[]
    for x_idx, x in enumerate(grid):
        for y_idx, y in enumerate(x):
            if y==0:
                head.append([x_idx,y_idx])
    return head

def hike_and_rate(heads, grid):
    score = 0
    rating = 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)] 

    for head in heads: 
        def dfs(x, y, visited):
            if (x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or 
                (x, y) in visited):
                return set(), set()
            
            if visited and grid[x][y] - grid[visited[-1][0]][visited[-1][1]] != 1:
                return set(), set()

            new_visited = visited + [(x, y)]

            if grid[x][y] == 9:
                return {(x, y)}, {tuple(new_visited)}

            all_destinations = set()
            all_trails = set()
            for dx, dy in directions:
                dest, trails = dfs(x + dx, y + dy, new_visited)
                all_destinations.update(dest)
                all_trails.update(trails)

            return all_destinations, all_trails

        head_dest, head_trails = dfs(head[0], head[1], [])
        score += len(head_dest)
        rating += len(head_trails)

    return score, rating

def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    start_time = time.time()
    grid = read_input("data.txt")

    heads = find_head(grid)
    
    score, rating = hike_and_rate(heads, grid)

    print("Score:", score)
    print("Rating:", rating)

    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    main()