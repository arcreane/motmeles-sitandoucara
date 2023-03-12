#Loading required modules for the project
import string
import random
#from fpdf import FPDF

#Trial of the average version 15 x 7 - words are between 4 and 6 letters long
word_list = ["colère", "dallai", "marbre", "normes","solive","trésor"]
line = 15
column = 7

#Random letter generator based on column and line
letters = [[random.choice(string.ascii_uppercase) for i in range(0,column)] for j in range(0,line)]

#Define function to display grid
#Using f-string(f') for concatenation and a 2D array (2d) for number alignment
def display_grid():
    # Display column numbers 
    print('  ', end='  ')
    for i in range(0,column):
        print(f'{i:2d}', end=' ')
    print('')
    # Display top line
    print('  _|' + ' _'*(column+4) + '|_')
    # Display grid line with line numbers
    for i in range(0,line):
        print(f'{i:2d} |', end=' ')
        for j in range(0,column):
            print(letters[i][j], end='  ')
        print('|')
display_grid()
