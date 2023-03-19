#Loading required modules for the project
import string
import random

#Trial of the difficult version 30 x 15 - words are between 6 and 9 letters long
word_list = ["soutanne", "laitier", "epaissi", "salicole","additifs","apprendre"]
line = 30
column = 15

#Random letter generator based on column and line
letters = [[random.choice(string.ascii_uppercase) for i in range(0,column)] for j in range(0,line)]

#function to insert words horizontally and vertically between the letters
def insert_words(grid, words):
    for word in words:
        word_len = len(word)
        line, column = random.randint(0, 30), random.randint(0, 15)
        # horizontal placement
        if random.randint(0, 1):
            if column + word_len < 15:
                for i in range(word_len):
                    try:
                        grid[line][column+i] = word[i]
                    except Exception :
                        print(word[i])
        # vertical placement
        else:
            if line + word_len < 30:
                for i in range(word_len):
                    try:
                        grid[line+i][column] = word[i]
                    except Exception :
                        print(word[i])
                       
    return grid

grid_letters = insert_words(letters, word_list)

#Define function to display grid
#Using f-string(f') for concatenation and a 2D array (2d) for number alignment
def display_difficult_grid():
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

#Function to check if the entered word exists in the list
def check_word_exist(word, word_list):
    if word in word_list:
        return True
    else:
        return False

#Function to allow the user to enter the coordinates of the word
def find_word_in_grid():
# Get user input for line and column of the first letter of the word
    line = int(input("Enter the line number of the first letter of the word (0-29): "))
    column = int(input("Enter the column number of the first letter of the word (0-14): "))
    # Get user input for the direction of the word (0 for horizontal, 1 for vertical)
    direction = int(input("Enter the direction of the word (0 for horizontal, 1 for vertical): "))

# Initialize variables to store the word and letters in the direction
    word = ""
    letters = []

# If direction is horizontal, get all letters in the row
    if direction == 0:
        for j in range(column, column + len(word_list)):
            letters.append(grid_letters[line][j])
# If direction is vertical, get all letters in the column
    else:
        for i in range(line, line + len(word_list)):
            letters.append(grid_letters[i][column])

# Concatenate the letters to form the word
    word = "".join(letters)

# Check if the word exists in the word list
    if check_word_exist(word, word_list):
        print("Congratulations, you found the word", word)
    else:
        print("Sorry, the word does not exist in the grid")



