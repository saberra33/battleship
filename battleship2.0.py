import random

def display_grid(grid):
    # just printing the rows cleanly
    for row in grid:
        print(' '.join(str(cell) for cell in row))
    print()

def update_grid(grid, row, col, marker):
    # check bounds so it doesnt crash
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        grid[row][col] = marker
    else:
        print("try again")

# start with a clean 5x5 grid
grid = [[0 for _ in range(5)] for _ in range(5)]
print("Welcome to Battleship!")
breaker = True
listofguesses = []

while breaker:
    print("Type play to get in to a match.")
    print("Type quit to exit out of the game.")
    choice = input("What would you like to do?: ").strip().lower()
    
    if choice == "quit":
        print("Have a nice day, goodbye.")
        breaker = False
    elif choice == "play":
        grid = [[0 for _ in range(5)] for _ in range(5)]
        listofguesses = [] # clear past guesses
        
        # fix: random target match grid bounds (1 to 5 for user input)
        randcoordinate_x = random.randint(0, 4)
        randcoordinate_y = random.randint(0, 4)
        
        print("1 battleship has been placed")
        print("initial grid:")
        display_grid(grid)
        
        # separate loop for the actual match turns
        in_game = True
        while in_game:      
            try:
                row_input = input("Guess which row? (1-5): ")
                col_input = input("Guess which column? (1-5): ")
                
                row = int(row_input) - 1
                col = int(col_input) - 1

            except ValueError:
                print("Invalid input, please enter valid numbers.")
                continue
               
            # bounds check first
            if row < 0 or row > 4 or col < 0 or col > 4:
                print("Your guess is out of range. Try again.")
                continue

            # check duplicate guesses
            if (row, col) in listofguesses:
                print("You have already guessed that coordinate. Try again.")
                continue
            
            listofguesses.append((row, col))
            
            # check win condition
            if row == randcoordinate_x and col == randcoordinate_y:
                update_grid(grid, row, col, 'O')
                display_grid(grid)
                
                playagaininput = input("Congratulations! You sunk the battleship! Would you like to play again? (yes/no): ").strip().lower()
                if playagaininput == 'yes':
                    in_game = False # breaks match loop to restart at the main menu
                else:
                    print("Thanks for playing! Goodbye!")
                    in_game = False
                    breaker = False # shuts down the whole game
            else:
                # it's a miss
                update_grid(grid, row, col, 'X')
                print("Sorry, you missed the battleship. Try again.")
                display_grid(grid)
    else:
        print("Invalid input. Please type 'play' or 'quit'.")
