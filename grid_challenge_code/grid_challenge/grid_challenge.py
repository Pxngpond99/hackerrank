def gridChallenge(grid):
    # Write your code here
    new_grid = [sorted(t) for t in grid]
    for x in range(len(new_grid[0])):
        columns = [y[x] for y in new_grid]
        if columns != sorted(columns):
            return 'NO'
    return 'YES'