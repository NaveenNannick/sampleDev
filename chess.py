N = 8

class coinState:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col

def initialize_state(board):
    states = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != "  ":
                states.append( coinState(board[i][j], i, j) )


    #for i in states:
        #print(i.name, i.row, i.col)
    return states

def check_rook(move, coin, s):
    r = coin.row
    c = coin.col
    
    if c == move[1] and r < move[0]:
        hit = True
        for i in range(r+1, move[0]):
            if board[i][c] != "  ":
                hit = False
                break
        if hit:
            s += "1"
            return s
            
    if c == move[1] and r > move[0]:
        hit = True
        for i in range(move[0], r):
            if board[i][c] != "  ":
                hit = False
                break
        if hit:
            s += "1"
            return s
            
    if r == move[0] and c < move[1]:
        hit = True
        for i in range(c+1, move[1]):
            if board[r][i] != "  ":
                hit = False
                break
        if hit:
            s += "1"
            return s
    if r == move[0] and c > move[1]:
        hit = True
        for i in range(move[1], c):
            if board[r][i] != "  ":
                hit = False
                break
        if hit:
            s += "1"
            return s

    s += "0"
    return s
        
def check_knight(move, coin, s):
    s += "0"
    rows = [2, 1, -1, -2, -2, -1, 1, 2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for row, col in zip(rows, cols):
        if coin.row + row == move[0] and coin.col + col == move[1]:
            s = s[:-1] + "1"
            break
    return s

def check_bishop(move, coin, s):
    r = coin.row
    c = coin.col
    

    for i,j in zip(range(r+1, N), range(c+1, N)):
        if (i == move[0] and j == move[1]):
            s += "1"
            return s
        if (board[i][j] != "  "):
            break

    for i,j in zip(range(r-1, -1, -1), range(c-1, -1, -1)):
        if (i == move[0] and j == move[1]):
            s += "1"
            return s
        if (board[i][j] != "  "):
            break

    for i,j in zip(range(r+1, N), range(c-1, -1, -1)):
        if (i == move[0] and j == move[1]):
            s += "1"
            return s
        if (board[i][j] != "  "):
            break

    for i,j in zip(range(r-1, -1, -1), range(c+1, N)):
        if (i == move[0] and j == move[1]):
            s += "1"
            return s
        if (board[i][j] != "  "):
            break

    s += "0"
    return s

def check_queen(move, coin, s):
    s = check_rook(move, coin, s)
    if s[-1] == "1":
        return s
    s = s[:-1]
    s = check_bishop(move, coin, s)
    return s

def check_king(move, coin, s):
    r = coin.row
    c = coin.col
    
    rows = [1,-1,1,-1,-1,0,0,1]
    cols = [1,-1,-1,1,0,-1,1,0]

    for i,j in zip(rows, cols):
        if r + i == move[0] and c + j == move[1]:
            print("hit")
            s += "1"
            return s
    s += "0"
    return s

def check_pawn(move, coin, s):
    r = coin.row
    c = coin.col
    if r+1 == move[0] and c+1 == move[1]:
        s += "1"
        return s
    if r+1 == move[0] and c-1 == move[1]:
        s += "1"
        return s

    s += "0"
    return s

                 

def is_safe(move, states):
    s = ""
    for coin in states:
        
        if coin.name == "rk":
            print(vars(coin))
            s = check_rook(move, coin, s)
        elif coin.name == "kn":
            print(vars(coin))
            s = check_knight(move, coin, s)
        elif coin.name == "bi":
            print(vars(coin))
            s = check_bishop(move, coin, s)
        elif coin.name == "qn":
            print(vars(coin))
            s = check_queen(move, coin, s)
        elif coin.name == "kg":
            print(vars(coin))
            s = check_king(move, coin, s)
        elif coin.name == "pn":
            print(vars(coin))
            s = check_pakn(move, coin, s)

    print(f"sat string \n{s}")
            
    


board = [["rk", "  ", "  ", "  " , "kg" , "  ", "kn" , "  "],
         ["  ", " pn", "pn", "pn" , "  " , "pn", "pn" , "  "],
         ["bi", "  ", "kn", "bi" , "  " , "qn", "  " , "  "],
         ["pn", "", "  ", "  " , "pn" , "  ", "  " , "  "],
         ["  ", "  ", "  ", "rk" , "  " , "  ", "  " , "pn"],
         ["  ", "  ", "  ", "  " , "  " , "  ", "  " , "  "],
         ["  ", "  ", "  ", "  " , "  " , "  ", "  " , "  "],
         ["  ", "  ", "  ", "  " , "  " , "  ", "  " , "  "]]
states = initialize_state(board)
move = (3, 5)
is_safe(move, states)


#    0     1     2     3       4     5     6      7
#0 ["rk", "  ", "  ", "  " , "kg" , "  ", "kn" , "  "],
#1 ["  ", "  ", "pn", "pn" , "  " , "pn", "pn" , "  "],
#2 ["bi", "  ", "kn", "bi" , "  " , "qn", "  " , "  "],
#3 ["pn", "pn", "  ", "  " , "pn" , " c ", "  " , "  "],
#4 ["  ", "", "  ", "rk" , "  " , "  ", "  " , "pn"],
#5 ["  ", "  ", "  ", "  " , "  " , "  ", "  " , "  "],
#6 ["  ", "  ", "  ", "  " , "  " , "  ", "  " , "  "],
#7 ["  ", "  ", "  ", "  " , "  " , "  ", "  " , "  "]]


