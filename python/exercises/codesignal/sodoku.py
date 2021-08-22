# see 
# much better solution:
# https://medium.com/digitalfrontiers/gotta-comprehend-em-all-sudoku-verifier-done-easy-in-python-ddf919e587ef 


def is_valid(my_list):
    bit_map={}
    
    for i in range(0,10):
        bit_map[i]=False
    
    for i in my_list:
        if not str(i).isdigit():
            continue      
        index=int(i) 
        if bit_map[index] == True:
            return(False)
        bit_map[index] = True
    return(True)

def print_grid(g):
    for i in g:
        print(i)
        
def flattan_list(my_list):
    ret_list=[]
    for i in my_list:
        for j in i:
           ret_list.append(j)
    return(ret_list)
    
    
def sudoku2(grid):
    
    for row in grid:
        if not is_valid(row):
            return(False)
    
    grid = list(zip(*grid))

    for col in grid:
        if not is_valid(col):
            return(False)

# Should use list comprehensions below?
#             square = [item for items in [row[j:j + 3] for row in grid[i:i + 3]] for item in items]
    # find the subgirds
    for i in range(0,9,3):
        for j in range(0,9,3):
            unflattened_squares=[ row[j:j+3] for row in grid[i:i+3] ]
            flat_square=flattan_list(unflattened_squares)
            if not is_valid(flat_square):
                return(False)
    return(True)
        
            
                       

