import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []

    #
    # TODO - implement this in part 2
    #
    height = len(grid)
    width = len(grid[0])

    # new beliefs is generated
    for i in range(height):
        new_row = []
        for j in range(width):
            hit = (color == grid[i][j])
            new_row.append(beliefs[i][j] * (hit * p_hit + 1-hit * p_miss))
        new_beliefs.append(new_row)
    
    # normalizer is defined by adding each probability of the new beliefs
    p_sum = 0
    for i in range(height):
        for j in range(width):
            p_sum += new_beliefs[i][j]
    
    # normalization 
    for i in range(height):
        for j in range(width):
            new_beliefs[i][j] = new_beliefs[i][j] / p_sum

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)