""" Problem Description

Chess bishop moves diagonally in any number of squares. Given two different
 squares of the chessboard, determine whether a bishop can go from the first
 square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and
 the row number, first two - for the first square, and the last two - for the
 second square. The program should output YES if a bishop can go from the first
 square to the second one in a single move or NO otherwise.

 input: type <int>, 4 numbers in range 1-8
 output: type <str>, "YES" or "NO"

"""

def bishopMove(a,b,c,d):
    """
	Takes 4 integers to determine whether chess bishop
	can make a valid move.

	input:  type <int>, 4 numbers from 1-8
	output: type <str>, "YES" or "NO"
    """
    if abs(a - c) == abs(b - d):
	    print("YES")
    else:
	    print("NO")


# Test 
col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

bishopMove(col1, row1, col2, row2)


