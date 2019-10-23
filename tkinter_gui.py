# Yunlu Ma ID: 28072206

import tkinter
import get_point
import P5_logic
import set_dialogs

class Start_game:
    
    # This Class used to build the first root window with a button of "Start Game"
    # and run the game
    
    def __init__(self):
        
        # The __init__() fuction builds the tkinter.Tk() with a button of "Start Game"
    
        self._root_window = tkinter.Tk()
        setting_button = tkinter.Button(
            master = self._root_window, text = 'Start Game', font = ('Helvetica', 14),
            command = self._set)
        setting_button.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def _set(self) -> None:
        
        # When button was clicked call the Class with setting dialogs of the rule of Othello
        # When setting finished, click OK to begin game
        
        set_game = set_dialogs.Dialogs()
        set_game.show()

        if set_game.was_ok_clicked():
            self._root_window.destroy()
            game = Gameboard(set_game._row_number,set_game._col_number,set_game._turn.get(),set_game._winning_way.get())
            game.run()       
            

    def run(self) -> None:
        
        # Run the entire game project
        
        self._root_window.mainloop()

    

class Gameboard:
    
    # This Class contains the core part of the Othello includes the gameboard, notations and game logic
    
    def __init__(self,row_number:str,col_number:str,first_turn:str,winning_way:str):

        # The __init__() fuction builds the canvas for the gameboard on the new tkinter.Tk() and also import Othello's logic
        
        self._point_list = []
        self._useful_list =[]
        self._count = 0
        
        self._root_window = tkinter.Tk()
        
        self._row = int(row_number)
        self._col = int(col_number)
        self._first_set = 'B'
        self._winning_way = winning_way
        
        self._turn = tkinter.StringVar()
        self._turn.set(first_turn)
        
        self._black = tkinter.StringVar()
        self._white = tkinter.StringVar()

        self._change_set_color_clicked = False
        self._start_to_play_clicked = False

        self.Othello = P5_logic.Othello(self._row,self._col,self._turn.get(),self._winning_way)
        


        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 500, height = 500,
            background = 'pink')

        self._canvas.grid(
            row = 0, column = 0, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)


        self._result_frame = tkinter.Frame(master = self._root_window )

        self._result_frame.grid(
            row = 0, column = 1, rowspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.N
            )
        self._set_text = tkinter.StringVar()
        self._set_text.set('Set Black discs first!')

        

        set_black_discs_lable = tkinter.Label(
            master = self._result_frame, textvariable = self._set_text,
            font = ('Helvetica', 14))
        
        set_black_discs_lable.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        self._change_set_color = tkinter.Button(
            master = self._result_frame, text = 'Set White discs',
            font = ('Helvetica', 14), command = self._change_set_color)

        self._change_set_color.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)


        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
            

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def run(self) -> None:
        
        # Run the core part of the game 
        
        self._root_window.mainloop()
        
    def _change_set_color(self) -> None:

        # Change the color to "white" when setting the game board
        
        self._change_set_color_clicked = True
        self._set_text.set('Now Set White discs!')
        self._first_set = "W"
        self._change_button()

    def _change_button(self) -> None:
        
        # Remove the button 'Now Set White discs!' when it was clicked
        # Add the button "Start to Play!!!" at the same position when the player is setting the white discs
        
        if self._change_set_color_clicked:
            self._change_set_color.grid_remove()
            self._start_to_play = tkinter.Button(
                master = self._result_frame, text = 'Start to Play!!!',
                font = ('Helvetica', 14), command = self._begin_to_play)
            self._start_to_play.grid(
                row = 1, column = 0, padx = 10, pady = 10,
                sticky = tkinter.W)

    
        
        
    def _begin_to_play(self) -> None:

        # Show the gameboard which was setted by the player and show it on canvas
        # Show the important information like Welcome, Winning Way, Turn and the number of discs in different colors 
        
        self._start_to_play_clicked = True
       
        self._set_text.set('Welcome to Othello!')
        
        self._start_to_play.grid_remove()
        
        self.Othello.build_board()
        for click_point in self._point_list:
            
            if click_point._color == "B":
                self.Othello._board[click_point._row][click_point._col] = "B"
            else:
                self.Othello._board[click_point._row][click_point._col] = "W"

        self.Othello.count_number()
        self._black.set(str(self.Othello._black))
        self._white.set(str(self.Othello._white))

        winning_way_label = tkinter.Label(
            master = self._result_frame, text = "Winning Way:  " + self._winning_way,
            font = ('Helvetica', 14))
        winning_way_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        Change_frame = tkinter.Frame(master = self._result_frame)

        Change_frame.grid(row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N)

        turn_notation_label = tkinter.Label(
            master = Change_frame, text = "TURN: ",
            font = ('Helvetica', 14))
        turn_notation_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        turn_label = tkinter.Label(
            master = Change_frame, textvariable = self._turn,
            font = ('Helvetica', 14))
        turn_label.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        Black_notation_label = tkinter.Label(
            master = Change_frame, text = "BLACK: ",
            font = ('Helvetica', 14))
        Black_notation_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        Black_number_label = tkinter.Label(
            master = Change_frame, textvariable = self._black,
            font = ('Helvetica', 14))
        Black_number_label.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        White_notation_label = tkinter.Label(
            master = Change_frame, text = "WHITE: ",
            font = ('Helvetica', 14))
        White_notation_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        White_number_label = tkinter.Label(
            master = Change_frame, textvariable = self._white,
            font = ('Helvetica', 14))
        White_number_label.grid(
            row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        if self.Othello.check_for_winner():
            self.Othello.winner_system(self._winning_way)
            winner_label = tkinter.Label(
                master = self._result_frame, text = "WINNER:  " + self.Othello._winner,
                font = ('Helvetica', 14))
            winner_label.grid(
                row = 2, column = 0, padx = 10, pady = 10,
                sticky = tkinter.W)
        else:
            self._turn.set(self.Othello._turn) 

        
        
        
    def _check_valid_point(self,click_point):
        # Check the click point is a valid move based on the game logic
        for lst in self.Othello._total_list:
            if click_point._row == lst[-1][0] and  click_point._col == lst[-1][1]:
                if self._count == 0:
                    self._count += 1
                    self._point_list.append(click_point)
                self._useful_list.append(lst)
                continue
        if self._count != 0:
            self.Othello.change_color(click_point._row, click_point._col,self._useful_list)
            self.change_color()
            self._redraw_all_spots()
            self.Othello.count_number()
            self._black.set(str(self.Othello._black))
            self._white.set(str(self.Othello._white))
            self.Othello.opposite_turn()
            self._turn.set(self.Othello._turn) 
                



                
    def change_color(self) -> None:

        # Make the change of the color of discs on the board if the player drop the correct disc

        for lst in self._useful_list:
            for position in lst[:-1]:
                for click_point in self._point_list:
                    if click_point._row == position[0] and click_point._col == position[1]:
                        click_point._color = self._turn.get()
                        
                    
    def _on_canvas_resized(self, event: tkinter.Event) -> None:

        # Keep all the stuffs on the canvas when resizing

        self._draw_lines()
        self._redraw_all_spots()

    
    def _draw_lines(self) -> None:

        # Draw the line of the gameboard on canvas based on the row number and col number
        
        self._canvas.delete(tkinter.ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        for i in range(1,self._row):
            self._canvas.create_line(0, canvas_height * (i/self._row), canvas_width, canvas_height * (i/self._row), fill = 'black')
        for i in range(1,self._col):
            self._canvas.create_line(canvas_width * (i/self._col), 0, canvas_width * (i/self._col), canvas_height, fill = 'black')

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        
        # Handle the click on the canvas based with different methods based on the situation
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        if self._start_to_play_clicked:
            click_point = get_point.from_pixel(
                event.x, event.y, width, height,self._turn.get())
            self._get_disc_row(click_point)
            self._get_disc_col(click_point)

            self.Othello.total_game()
            self._reset()
            self._check_valid_point(click_point)
            if self.Othello.check_for_winner():
                self.Othello.winner_system(self._winning_way)
                winner_label = tkinter.Label(
                    master = self._result_frame, text = "WINNER:  " + self.Othello._winner,
                    font = ('Helvetica', 14))
                winner_label.grid(
                    row = 2, column = 0, padx = 10, pady = 10,
                    sticky = tkinter.W)
            else:
                self._turn.set(self.Othello._turn) 

            
            
            
        else:
            click_point = get_point.from_pixel(
                    event.x, event.y, width, height,self._first_set)
            self._get_disc_row(click_point)
            self._get_disc_col(click_point)


            if self._count == 0:

                self._point_list.append(click_point)
                self._redraw_all_spots()
                self._count += 1
                
            else:
                l=[]
                alist = [self._point_list[0]]
                for point in self._point_list:
                
                    
                    if (click_point._row == point._row) and (click_point._col == point._col):

                        return
                        
                    else:
                        pass
                        
                self._point_list.append(click_point)
                self._redraw_all_spots()  
                        
                        
                        
                    
                
                    
    def _reset(self):

        # Reset the list and the variable before using them
        
        self._useful_list = []
        self._count = 0
        
    def _redraw_all_spots(self) -> None:

        # Draw the discs on the board with different colors

        self._canvas.delete(tkinter.ALL)
        self._draw_lines()
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        for click_point in self._point_list:
            x_coords = self._check_x_coords(click_point)
            y_coords = self._check_y_coords(click_point)
            color = click_point.color()
            self._canvas.create_oval(
                    x_coords[0] * canvas_width, y_coords[0] * canvas_height,
                    x_coords[1] * canvas_width, y_coords[1] * canvas_height,
                    fill = color, outline = "black")

    def _check_x_coords(self,click_point)-> tuple:

        # Find the x coordinate of the click point by making the translation based on the size of the canvas
        
        center_x = click_point.frac()[0]                    
        for i in range(self._col):
            if i/self._col <= center_x < (i+1)/self._col:
                x_coords = (i/self._col,(i+1)/self._col)

        return x_coords
        
    def _check_y_coords(self,click_point) -> tuple:

        # Find the y coordinate of the click point by making the translation based on the size of the canvas
        
        center_y = click_point.frac()[1]
        for i in range(self._row):
                if i/self._row <= center_y < (i+1)/self._row:
                    y_coords = (i/self._row,(i+1)/self._row)

        return y_coords

  
            
    def _get_disc_col(self,click_point) -> int:

        # Find the col of the click point on the gameboard
        
        center_x = click_point.frac()[0]
        for i in range(self._col):
            if i/self._col <= center_x < (i+1)/self._col:
                col = i

        click_point.add_col(col)

    def _get_disc_row(self,click_point) -> int:

        # Find the row of the click point on the gameboard
        
        center_y = click_point.frac()[1]
        for i in range(self._row):
            if i/self._row <= center_y < (i+1)/self._row:
                row = i

        click_point.add_row(row)
        
        

if __name__ == '__main__':
    app = Start_game()
    app.run()
