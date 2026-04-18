def click(num):
    global count, arr
    row = (num-1)//3
    col = (num-1)%3

    player = "X" if count % 2 == 0 else "O"
    color = "blue" if player == "X" else "red"

    buttons[num-1].config(text=player, bg=color, fg="white" , state="disabled")
    arr[row][col] = player
    count += 1

    check_winner()
def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")
def check_winner():
    global arr, count

    lines = [
        arr[0], arr[1], arr[2],  
        [arr[0][0], arr[1][0], arr[2][0]],
        [arr[0][1], arr[1][1], arr[2][1]],
        [arr[0][2], arr[1][2], arr[2][2]],
        [arr[0][0], arr[1][1], arr[2][2]],
        [arr[0][2], arr[1][1], arr[2][0]]
    ]

    for line in lines:
        if line == ["X","X","X"]:
            messagebox.showinfo("X Wins", "X Wins")
            disable_all_buttons()
            return
        elif line == ["O","O","O"]:
            messagebox.showinfo("O Wins", "O Wins")
            disable_all_buttons()
            return

    if count == 9:
        messagebox.showinfo("Tie", "It's a Tie!")
def newgameset():
    global count, arr
    count = 0
    arr = [[None,None,None],[None,None,None],[None,None,None]]

    for btn in buttons:
        btn.config(text="", bg="white", fg="black", state="normal")
from tkinter import Button,Label,messagebox,Frame,Tk
root=Tk()
root.title("Tic Tac Toe Game")
count=0
arr=[[None,None,None],[None,None,None],[None,None,None]]
root.geometry("300x300")
root.resizable(width=False,height=False)
root.iconbitmap(r"C:\Users\ELCOT\Documents\python GUI programs\x_o.ico")
root.config(background="green")
label1=Label(root,text="TIC TAC TOE GAME",bg="yellow",font=("Arial", 12, "bold"))
label1.grid(row=0,column=0,padx=5,pady=10,columnspan=2)
frame=Frame(root)
frame.grid(row=1,column=1,padx=75)
button1=Button(frame,text="",activebackground="grey",command=lambda : click(1),width=4,height=2)
button1.grid(row=1,column=0,padx=5,pady=5)
button2=Button(frame,text="",activebackground="grey",command=lambda : click(2),width=4,height=2)
button2.grid(row=1,column=1,padx=5,pady=5)
button3=Button(frame,text="",activebackground="grey",command=lambda : click(3),width=4,height=2)
button3.grid(row=1,column=2,padx=5,pady=5)
button4=Button(frame,text="",activebackground="grey",command=lambda : click(4),width=4,height=2)
button4.grid(row=2,column=0,padx=5,pady=5)
button5=Button(frame,text="",activebackground="grey",command=lambda : click(5),width=4,height=2)
button5.grid(row=2,column=1,padx=5,pady=5)
button6=Button(frame,text="",activebackground="grey",command=lambda : click(6),width=4,height=2)
button6.grid(row=2,column=2,padx=5,pady=5)
button7=Button(frame,text="",activebackground="grey",command=lambda : click(7),width=4,height=2)
button7.grid(row=3,column=0,padx=5,pady=5)
button8=Button(frame,text="",activebackground="grey",command=lambda : click(8),width=4,height=2)
button8.grid(row=3,column=1,padx=5,pady=5)
button9=Button(frame,text="",activebackground="grey",command=lambda : click(9),width=4,height=2)
button9.grid(row=3,column=2,padx=5,pady=5)
resetgame=Button(root,text="Reset",bg="lightblue",fg="black",activebackground="red",font=("bold"),command=lambda :newgameset())
resetgame.grid(row=2,column=0,columnspan=2,pady=20)
buttons = [button1, button2, button3,
           button4, button5, button6,
           button7, button8, button9]
root.mainloop()