from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Tic-Tac-Toe")

# si x commence ça donne True
clicked = True
count = 0

# fonction pour désactiver tous les boutons
def disable_buttons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)



def checkGagne():
    global gagne
    gagne = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg = "green")
        b2.config(bg = "green")
        b3.config(bg = "green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur X a gagne")
        disable_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur X a gagne")
        disable_buttons()

    elif b7["text"] ==  "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur X a gagne")
        disable_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7[" text "] == "X" :
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur X a gagne")
        disable_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur X a gagne")
        disable_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur X a gagne")
        disable_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur X a gagne")
        disable_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur X a gagne")
        disable_buttons()

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Félicitaion le joueur 0 a gagné")
        disable_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur O a gagne")
        disable_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur O a gagne")
        disable_buttons()
    elif b1["text"] == "O" and b4["text"] == "O" and b7[" text"] == "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur O a gagne")
        disable_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur O a gagne")
        disable_buttons()
        
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur O a gagne")
        disable_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur O a gagne")
        disable_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        gagne = True
        messagebox.showinfo("Tic Tac Toe", "Brrravooo !! le joueur O a gagne")
        disable_buttons()


    # verifier égalité
    if count == 9 and gagne == False:
        messagebox.showinfo("Tic Tac Toe","Egalité!!")
        disable_buttons()



# function du click des bouttons
def b_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        text1 = Label (root, text= 'X' , fg= 'black', bg= 'white', font=("Courrier", 12))
        text2 = Label (root, text= 'O' , fg='black', bg='#41B77F', font=("Courrier", 12))
        text1.grid(row= 5, column= 0)
        text2.grid(row= 5 , column= 2)
        checkGagne()
    elif b["text"] == " " and clicked == False:
          b["text"] = "O"
          clicked = True
          count += 1
          text1 = Label(root, text='X', fg='black', bg='#41B77F', font=("Courrier", 12))
          text2 = Label(root, text='O', fg='black', bg='white', font=("Courrier", 12))
          text1.grid(row= 5, column= 0)
          text2.grid(row= 5, column= 2)
          checkGagne()
    else:
        messagebox.showerror("TIc Tac Toe","Hey! ce carreaux est deja utilisé \nchoisissez un autre ...")



def rejouer():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0


    # creer les boutons
    b1 = Button(root, text=" ",font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ",font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ",font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ",font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ",font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ",font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ",font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ",font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ",font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # pour une grille pour poser les boutons
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

m_menu = Menu(root)
root.config(menu = m_menu)

option_menu = Menu(m_menu, tearoff=0)
m_menu.add_cascade(label='options',menu=option_menu)
option_menu.add_command(label = 'rejouer', command= rejouer)
option_menu.add_command(label = 'Exit', command= quit)
rejouer()

# pour afficher notre fenetre
root.mainloop()