def print_board(theBoard):
    print(theBoard["top-L"],"|",theBoard["top-M"],"|",theBoard["top-R"])
    print("---------")
    print(theBoard["mid-L"],"|",theBoard["mid-M"],"|",theBoard["mid-R"])
    print("---------")
    print(theBoard["low-L"],"|",theBoard["low-M"],"|",theBoard["low-R"])


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

turn="X"
for i in range(9):
    print(turn+"'s turn. Enter the position (top-L,top-M,top-R , mid-L,mid-M,mid-R , low-L,low-M,low-R)")
    pos = input()
    theBoard[pos]=turn
    if turn=="X":
        turn="O"
    else:
        turn="X"
    print_board(theBoard)
