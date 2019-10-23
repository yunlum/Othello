# Yunlu Ma ID: 28072206

import tkinter

class Dialogs:
    
    # This Class builds the dialogs in tkinter for the player to set the game
    
    def __init__(self):
        
        # The __init__() function builds a dialog window to ask for
        # row number, col number, first turn and the winning way with entry, checkbutton and button
        
        
        self._ok_clicked = False
        self._row_number = 0
        self._col_number = 0
        self._turn = tkinter.StringVar()
        self._turn.set("W")
        self._winning_way = tkinter.StringVar()
        self._winning_way.set("<")


        self._dialog_window = tkinter.Toplevel()
        
        
        
        set_label = tkinter.Label(
            master = self._dialog_window, text = 'Set your Othello!',
            font = ('Helvetica', 18))

        set_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N + tkinter.E)
        
        row_col_infor_label = tkinter.Label(
            master = self._dialog_window, text = "Row & Col must be between 4 to 16",
            font = ('Helvetica', 14))

        row_col_infor_label.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        row_number_label = tkinter.Label(
            master = self._dialog_window, text = 'Row number:',
            font = ('Helvetica', 14))

        row_number_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_number_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = ('Helvetica', 14))

        self._row_number_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        col_number_label = tkinter.Label(
            master = self._dialog_window, text = 'Col number:',
            font = ('Helvetica', 14))

        col_number_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._col_number_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = ('Helvetica', 14))

        self._col_number_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        first_turn_frame = tkinter.Frame(master = self._dialog_window)

        first_turn_frame.grid(
            row = 4, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N
            )
        

        black_label = tkinter.Label(
            master = first_turn_frame, text = 'For Black move first, check the box!',
            font = ('Helvetica', 14))
        black_label.grid(row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        white_label = tkinter.Label(
            master = first_turn_frame, text = 'For White move first, NOT check the box!',
            font = ('Helvetica', 14))
        white_label.grid(row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        
        first_turn_lable = tkinter.Checkbutton(
            master = first_turn_frame, text = 'Black First or Not', variable = self._turn,
            font = ('Helvetica', 14), onvalue = "B", offvalue = 'W')
        

        first_turn_lable.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)



        winning_way_frame = tkinter.Frame(master = self._dialog_window)

        winning_way_frame.grid(
            row = 5, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N
            )

        more_label = tkinter.Label(
            master = winning_way_frame, text = 'For More Discs Win, check the box!',
            font = ('Helvetica', 14))
        more_label.grid(row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        fewer_label = tkinter.Label(
            master = winning_way_frame, text = 'For Fewer Discs Win, NOT check the box!',
            font = ('Helvetica', 14))
        fewer_label.grid(row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        winning_way = tkinter.Checkbutton(
            master = winning_way_frame, text = 'More Discs Win or Not', variable = self._winning_way,
            font = ('Helvetica', 14), onvalue = ">", offvalue = "<")

        winning_way.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = ('Helvetica', 14),
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = ('Helvetica', 14),
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)
  

        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        

    

    def was_ok_clicked(self) -> bool:
        
        # Check whether the OK button was clicked or not
        
        return self._ok_clicked




    def _on_ok_button(self) -> None:

        # Get all the variables and destory the dialog window when OK button was clicked
        
        self._ok_clicked = True
        self._row_number = self._row_number_entry.get()
        self._col_number = self._col_number_entry.get()
        self._turn.get()
        self._winning_way.get()
        self._dialog_window.destroy()

    def show(self):

        # Show the dialog window in tkinter
        
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()
    
        
        
        
    def _on_cancel_button(self) -> None:

        # Destory the dialog window when CANCEL button was clicked
        
        self._dialog_window.destroy()

        
        

    
        
