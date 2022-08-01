"""
    Problem Description:

Chess king moves one square in any direction. Given two different squares
 of the chessboard, determine whether a king can go from the first square
 to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column
 and the row number, first two - for the first square,
 and the last two - for the second square. The program should output YES
 if a king can go from the first square to the second one in a single move
 or NO otherwise.

 input:  type <int>, 4 numbers from 1-8
 output: type <str>, "YES" or "NO"

"""


def kingMove(a, b, c, d):
    """
	Takes 4 integers to determine whether chess king
	can make a valid move.

	input:  type <int>, 4 numbers from 1-8
	output: type <str>, "YES" or "NO"
    """

    if (((a == c + 1) or (a == c - 1) or (a == c)) and ((b == d + 1) or (b == d - 1) or (b == d))):
	    print("YES")
    else:
	    print("NO")


# Test 
col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

kingMove(col1, row1, col2, row2)


