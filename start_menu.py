from projet import display_grid, find_word_in_grid
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
        find_word_in_grid()
        break
    elif choice == '2':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.\n')
