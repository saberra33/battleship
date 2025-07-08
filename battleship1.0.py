import random

def display_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()
def update_grid (grid, row, col):
      if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
         grid[row][col] = "X" 
      else:
         print("try again")

grid = [[0 for _ in range(5)] for _ in range(5)]
print("Welcome to Battleship!")
breaker = True
listofguesses = []
while breaker :
   print("Type play to get in to a match.")
   print("Type quit to exit out of the game.")
   choice = input("What would you like to do?: ")
   if choice == "quit":
      print("Have a nice day, goodbye.")
      breaker = False
   elif choice == "play":
      grid = [[0 for _ in range(5)] for _ in range(5)]
      randcoordinate_y = random.randint(0,4)
      randcoordinate_x = random.randint(0,4)
      loops= 0
      
      loops += 1
      coordinates_list= [randcoordinate_x, randcoordinate_y]
      if loops == 1:
         print ("1 battleship has been placed")
         print("initial grid:")
         print(grid)
      while breaker:      
            try:
               row = int(input(f"Guess which row?: "))
               col = int(input(f"Guess which column?: "))
               row -=1
               col -=1
               update_grid(grid, row, col)
               print(grid)

            except ValueError or KeyboardInterrupt:
               print("Invalid input, please enter the valid numbers for row and column provided.")
               
         #update the grid
            
            update_grid(grid, row, col)
            print(grid)
            
            try:
                  if row == randcoordinate_x and col == randcoordinate_y:
                     grid[randcoordinate_x][randcoordinate_y]= 'O'
                     update_grid
                     print (update_grid)
                     playagaininput= input("Congratulations! You sunk the battleship! Would you like to play again? (yes/no): ")
                     if playagaininput.lower() == 'yes':
                        grid = [[0 for _ in range(5)] for _ in range(5)]
                        listofguesses.clear()
                        randcoordinate_x = random.randint(0,4)
                        randcoordinate_y = random.randint(0,4)
                        loops = 0
                     elif playagaininput.lower() == 'no':
                        print("Thanks for playing! Goodbye!")
                        breaker = False
                     else:
                        print("Invalid input. Please type 'yes' or 'no'.")
                     
                  elif row < 0 or row > 4 or col < 0 or col > 4:
                        print("Your guess is out of range. Try again.")
                  else:
                        if [row, col] in listofguesses:
                           print("You have already guessed that coordinate. Try again.")
                        else:
                           grid[row][col]= 'X'
                           listofguesses.append([(row,col)])
                           print("Sorry, you missed the battleship. Try again.")
                           print(update_grid)
                        
                           
            except ValueError:
               print("you cant put that please enter the valid numbers for row and column provided")
      else:
         print("Invalid input. Please type 'play' or 'quit'.")