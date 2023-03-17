#Loading required modules for the project
import string
import random

#Trial of the average version 15 x 7 - words are between 4 and 6 letters long
word_list = ["pomme", "dallai", "marbre", "normes","solive","trésor"]
line = 15
column = 7

#Random letter generator based on column and line
letters = [[random.choice(string.ascii_uppercase) for i in range(0,column)] for j in range(0,line)]

#function to insert words horizontally and vertically between the letters
def insert_words(grid, words):
    for word in words:
        word_len = len(word)
        line, column = random.randint(0, 15), random.randint(0, 7)
        # horizontal placement
        if random.randint(0, 1):
            if column + word_len <= 7:
                for i in range(word_len):
                    grid[line][column+i] = word[i]
        # vertical placement
        else:
            if line + word_len <= 15:
                for i in range(word_len):
                    grid[line+i][column] = word[i]
    return grid

grid_letters = insert_words(letters, word_list)

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
            print(grid_letters[i][j], end='  ')
        if i < len(word_list):
            print('|',word_list[i])
        else :
            print('|')

# Define function to display welcome menu
def display_menu():
    print(55*"*", "\tWelcome to Sitan's Random Letter Grid!", 55*"*","\n",sep="\n")
    #print("Welcome to Sitan's Random Letter Grid!\n")
    print('Please choose an option:')
    print('1. To start the game')
    print('2. To leave')


# Display welcome menu and get user choice
while True:
    display_menu()
    choice = input('Enter your choice: ')
    if choice == '1':
        display_grid()
        break
    elif choice == '2':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.\n')

