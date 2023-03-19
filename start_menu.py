from easy_level import display_easy_grid, find_word_in_easy_grid
from average_level import display_average_grid, find_word_in_average_grid
from difficult_level import display_difficult_grid, find_word_in_difficult_grid
# Define function to display welcome menu
def display_menu():
    print(55*"*", "\tWelcome to Sitan's Random Letter Grid!", 55*"*","\n",sep="\n")
    #print("Welcome to Sitan's Random Letter Grid!\n")
    print('Please choose an option:')
    print('e. To start the easy level')
    print('a. To start the average level')
    print('d. To start the difficult level')
    print('q. To leave')



# Display welcome menu and get user choice
while True:
    display_menu()
    choice = input('Enter your choice: ')
    if choice == 'e':
        display_easy_grid()
        find_word_in_easy_grid()
        break
    elif choice == 'a':
        display_average_grid()
        find_word_in_average_grid()
        break
    elif choice == 'd':
        display_difficult_grid()
        find_word_in_difficult_grid()
        break
    elif choice == 'q':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.\n')
