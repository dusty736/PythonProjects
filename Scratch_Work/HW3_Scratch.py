test_grid = [ [ 1, 2, 3], [ 4, 5, 6], [ 7, 8, 9] ]


def get_pixel_at(pixel_grid, i, j):
    '''
    Returns the pixel in pixel_grid at row i and column j (zero-indexed).
    Returns 0 if i or j is out of bounds for the given pixel_grid.
    Returns 0 if i or j is a negative value.
    '''
    pixel_val= 0
    if i <= (len(pixel_grid) - 1) and j <= (len(pixel_grid[0]) - 1):
        if i >= 0 and j >= 0:
            pixel_val = pixel_grid[i][j]
            return pixel_val
        else:
            pixel_val = 0
            return pixel_val
    else:
        pixel_val = 0
    return pixel_val
    
def average_of_surrounding(pixel_grid, i, j):
    '''
    Returns the unweighted average of the values of the pixel at row i
    and column j and the eight pixels surrounding it.
    '''
    pixel_sum = 0
    pixel_sum += get_pixel_at(pixel_grid,i - 1, j -1)
    pixel_sum += get_pixel_at(pixel_grid,i - 1, j)
    pixel_sum +=  get_pixel_at(pixel_grid,i - 1, j + 1)
    pixel_sum += get_pixel_at(pixel_grid,i, j -1)
    pixel_sum += get_pixel_at(pixel_grid,i, j)
    pixel_sum += get_pixel_at(pixel_grid,i, j + 1)
    pixel_sum += get_pixel_at(pixel_grid,i + 1, j -1)
    pixel_sum += get_pixel_at(pixel_grid,i + 1, j)
    pixel_sum += get_pixel_at(pixel_grid,i + 1, j+ 1)

    return pixel_sum / 9

def test_average_of_surrounding():
    ''' Basic, brief sanity checks for average_of_surrounding. '''

    # Similarly to test_get_pixel_at, passing all of these tests
    # does not guarantee that your implementation of
    # average_of_surrounding is correct.

    test_grid = [
        [1, 2, 3, 4, 5, 6],
        [0, 2, 4, 6, 8, 10],
        [3, 4, 5, 6, 7, 8]
    ]

    try:
        assert average_of_surrounding(test_grid, 0, 0) == 0, \
            "Call to average_of_surrounding(test_grid, 0, 0) should have returned 0."
        assert average_of_surrounding(test_grid, 2, 5) == 3, \
            "Call to average_of_surrounding(test_grid, 2, 5) should have returned 3."
    except AssertionError as e:
        print e

print average_of_surrounding(test_grid,0,0)
