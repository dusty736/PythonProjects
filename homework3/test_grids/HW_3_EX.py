
sample = [ [1, 5, 61], [4, 3, 2], [10, 11, 100] ]

def get_pixel_at(pixel_grid, i, j):
    '''
    Returns the pixel in pixel_grid at row i and column j (zero-indexed).
    Returns 0 if i or j is out of bounds for the given pixel_grid.
    Returns 0 if i or j is a negative value.
    '''
    pixel_val= 0
    grid_height = len(pixel_grid)
    grid_width = len(pixel_grid[0])
    if i <= grid_height and j <= grid_width and i >= 0 and j >= 0:
        pixel_val = pixel_grid[i][j]
        return pixel_val 
    else:
        pixel_val = 0
        return pixel_val
    print pixel_val 

print get_pixel_at(sample, 0, 0)