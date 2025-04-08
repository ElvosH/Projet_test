from tkinter import*

def set_tile(row, column):
    global current_player

    board[row][column]["background"] = current_player
    
    if current_player == player0:
        current_player = player1
    else:
        current_player = player0

    texte["text"] = current_player+"'s turn"
    texte["background"] = current_player

def case_valide():
    pass

def victoire(row,column):
    pass

def nouvelle_partie():
    for row in range(6):
        for column in range(7):
          board[row][column] = Button(frame, text="", font=("Consolas", 20, "bold"), background="blue", foreground="yellow", width=10, height=3,
                                     command=lambda row = row, column = column: set_tile(row,column))
          board[row][column].grid(row=row+1, column=column)
   

#game setup
player0 = "red"
player1 = "yellow"
current_player = player0

board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]
     



#créer la fenêtre
fenetre = Tk()

fenetre.resizable(False, False)
fenetre.title("Connect 4 test")

#ajouter des "widget" dans la fenetre
frame = Frame(fenetre)
texte = Label(frame, text=current_player+"'s turn",font=("Consolas", 20), background=current_player,
              foreground="black")
frame.pack()
#faire la grille + fonction button
texte.grid(row=0, column=0, columnspan=7, sticky="we")

for row in range(6):
    for column in range(7):
        board[row][column] = Button(frame, text="", font=("Consolas", 20, "bold"), background="blue", foreground="yellow", width=10, height=3,
                                    command=lambda row = row, column = column: set_tile(row,column))
        board[row][column].grid(row=row+1, column=column)

button = Button(frame, text="recommencer", font=("Consolas", 20,), background="grey", foreground="white", command= nouvelle_partie)

button.grid(row=8, column=0, columnspan=7,sticky="we")


fenetre.mainloop()