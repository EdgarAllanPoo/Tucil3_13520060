# mengecek nilai g(i), yaitu jumlah slot yang tidak pada tempat seharusnya
def checkFungsiG(puzzle):
    arr = puzzle.board1D()
    value = 0
    
    for i in range(16):
        if(arr[i] != (i+1)):
            value+=1

    return value

# mengecek apabila telah mencapai solusi
def isSolution(puzzle):
    if(checkFungsiG(puzzle) == 0) :
        return True
    else :
        return False

# menyimpan semua state yang dilalui hingga mencapai solusi
def findSolutionRoute(solutionState):
    solution = []

    curState = solutionState.prevState
    prevState = solutionState

    while(curState != None):
       solution.insert(0,prevState) 
       prevState = curState
       curState = curState.prevState
    
    return solution