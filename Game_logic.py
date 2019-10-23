# YUNLU MA ID: 28072206

class Othello:
    
    #This class is used to build the gamestate of Othello Game
    
    def __init__(self,board_row:int,board_col:int,first_turn:str,winning_way:str):
        
        #Build some parameters in class and add the related data in them
        
        self._row = board_row
        self._col = board_col
        self._black = 0
        self._white = 0
        self._turn = first_turn
        self._board = []
        self._total_list = []
        self.winner = ''

    def build_board(self):

        # Build the basic gameboard
        
        for row in range(self._row):
            self._board.append([])
            for col in range(self._col):
                self._board[row].append(".")
                
                

    def opposite_turn(self):
        
        #Change the player's turn of the game
        
        if self._turn == "B":
            self._turn = "W"
        else:
            self._turn = "B"
            
    def count_number(self):
        
        #Count the number of discs on the board in different colors (White and Black)

        self._black = 0
        self._white = 0
        for row in range(self._row):
            for col in range(self._col):
                if self._board[row][col] == "B":
                    self._black +=1
                elif self._board[row][col] == "W":
                    self._white +=1
                    

    def print_board(self):

        #Print the game board in shell
        for i in self._board:
            for col in range(self._col):
                if col != self._col -1:
                    
                    print(i[col],end=" ")
                else:
                    print(i[col])


    def change_color(self,input_row:int, input_col:int,useful_list:list):

        #Make the change of the color of discs on the board if the player drop the correct disc

        self._board[input_row][input_col] = self._turn
        for lst in useful_list:
            for position in lst[:-1]:
                self._board[position[0]][position[1]] = self._turn
        

    def check_for_winner(self) -> bool:
        
        #Check is there a chance for both turns to continue playing through self._total_list
        #If not, return True
        
        self.total_game()
        if self._total_list == []:
            self.opposite_turn()
            self.total_game()
            if self._total_list == []:
                return True
        
                
    def winner_system(self,winning_way:str):
        
        #Find the winner of the game based on the winning way the player entered
    
        self.count_number()
        if winning_way == ">":
            if self._black > self._white:
                self._winner = "BLACK"
            elif self._black < self._white:
                self._winner = "WHITE"
            elif self._black == self._white:
                self._winner = "NONE"
        elif winning_way == "<":
            if self._black < self._white:
                self._winner = "BLACK"
            elif self._black > self._white:
                self._winner = "WHITE"
            elif self._black == self._white:
                self._winner = "NONE"
            
        
    def total_game(self):
        
        #Combined the two functions together in order to build the fundemental part of the game -- self._total_list

        position_list = self._find_position_in_board()
        self._find_position_to_drop(position_list)
                
            


    def _find_position_in_board(self):
        
        #Find the positions of the discs on the board in the same color as the player's turn
        #and add them to the list named "position_list"
        #and return the list
        
        position_list = []
        for row in range(self._row):
            for col in range(self._col):
                if self._turn == "B":
                    if self._board[row][col] == 'B':
                        position_list.append([row,col])
                else:
                    if self._board[row][col] == 'W':
                        position_list.append([row,col])
        return position_list


    def _check_drop_position(self,row: int, col: int, rowdelta: int, coldelta:int, str1:str, str2:str) -> list:
        
        #Check are there any dics in the opposite color around the own discs by using rowdelta and coldelta
        #and add them to the list named valid_position.
   	#If there are valid_position to drop the disc,
       	#return a list named self._total_list with the list "valid_position" in it

        if self._row > self._col:
            num = self._row
        else:
            num = self._col
        try:
            if self._is_valid_row_number(row + rowdelta) \
               and self._is_valid_col_number(col + coldelta) \
               and self._board[row + rowdelta][col + coldelta] == str1:
                valid_position = [[row + rowdelta, col + coldelta]]
                for i in range(2,num):
                    if self._is_valid_row_number(row + rowdelta * i) \
                       and self._is_valid_col_number(col + coldelta * i):
                        if self._board[row + rowdelta * i][col + coldelta * i] == str2:
                            break
                        if self._board[row + rowdelta * i][col + coldelta * i] == str1:
                            valid_position.append([row + rowdelta * i,col + coldelta * i])
                        else:
                            valid_position.append([row + rowdelta * i,col + coldelta * i])
                            self._total_list.append(valid_position)
                            break

            
        except:
            pass
        

    def _find_position_to_drop(self,position_list:list) -> list:
        
        #Use the position in position_list and called the funciton _check_drop_position() with different rowdelta and coldelta
        #in order to check the vaild position in eight direcitons around discs
        #and complete the self._total_list

        self._total_list =[]
        for position in position_list:
            row = int(position[0])
            col = int(position[1])
            if self._turn == 'B':
                self._check_drop_position(row,col, 0, 1,"W","B")
                self._check_drop_position(row,col, 1, 1,"W","B")
                self._check_drop_position(row,col, 1, 0,"W","B")
                self._check_drop_position(row,col, 1, -1,"W","B")
                self._check_drop_position(row,col, 0, -1,"W","B")
                self._check_drop_position(row,col, -1, -1,"W","B")
                self._check_drop_position(row,col, -1, 0,"W","B")
                self._check_drop_position(row,col, -1, 1,"W","B")
            else:
                self._check_drop_position(row,col, 0, 1,"B","W")
                self._check_drop_position(row,col, 1, 1,"B","W")
                self._check_drop_position(row,col, 1, 0,"B","W")
                self._check_drop_position(row,col, 1, -1,"B","W")
                self._check_drop_position(row,col, 0, -1,"B","W")
                self._check_drop_position(row,col, -1, -1,"B","W")
                self._check_drop_position(row,col, -1, 0,"B","W")
                self._check_drop_position(row,col, -1, 1,"B","W")
            
            
    def _is_valid_col_number(self,col_number:int) -> bool:
        
        #Return True if the given column number is valid;
        #return False otherwise
        
        return 0 <= col_number < self._col
            

    def _is_valid_row_number(self,row_number: int) -> bool:
        
        #Return True if the given row number is valid;
        #return False otherwise
    

        return 0 <= row_number < self._row

        

   

                     

        
        
        
