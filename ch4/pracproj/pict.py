# 17/12/2019
# takes in an initial grid and rotates it by 90 deg clockwise
'''
input
['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']

output
[..00.00..]
[.0000000.]
[.0000000.]
[..00000..]
[...000...]
[....0....]
'''

#this function reads the grid and just prints it as is
#this was used for familiarisation with the coordinates and logic
def rotate(grid_val):
    y = (len(grid_val)) - 1
    print(y)
    while (y > 0):
        for x in range (len(grid_val[y])):
            print(grid_val[y][x], end = '')
        print('')
        y = y - 1

    return 0

#this function completes the task
def rotate2(grid_val):
    y = 0
    #y row index of the output grid
    #in the range func, it gives out the length of each row of the input grid
    for y in range(len(grid_val[y])):
        #x represents the column index of the output grid
        #the range function here gives the number of lists within the original
        #list
        for x in range(len(grid_val)):
            #we need to read the first element of each list
            #from 8 -> 0
            #row index starts from 8 and decreases to 0 with each loop iteration
            row_index = (len(grid_val)) - 1 - x

            #print what is found in the original grid at certain locations
            #start with 8,0 -> 0,0 || 8,1 - > 0,1 || until 8,6 -> 0,6
            print(grid_val[row_index][y], end = '')
        print('')
    return 0


#main
#input grid
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]


#print(len(grid)-1)
#print(len(grid[0]))
#print result
result = rotate2(grid)