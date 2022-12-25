from tkinter import*
from messagebox import showinfo, showwarning
from random import choice as select
from time import sleep


def endGame(win):
    if mode.get() == 2:
        if win == 'X':
            l.config(text='You Won', fg='#00f')
        else:
            l.config(text='You Lose ', fg='#f00')
    else:
        if win == 'X':
            l.config(text='X Win', fg='#00f')
        else:
            l.config(text='O Win', fg='#f00')
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)


def check():
    if board[0] == board[1] and board[1] == board[2]:
        return endGame(board[0])
    elif board[3] == board[4] and board[4] == board[5]:
        return endGame(board[3])
    elif board[6] == board[7] and board[7] == board[8]:
        return endGame(board[6])
    elif board[0] == board[3] and board[3] == board[6]:
        return endGame(board[0])
    elif board[1] == board[4] and board[4] == board[7]:
        return endGame(board[1])
    elif board[2] == board[5] and board[5] == board[8]:
        return endGame(board[2])
    elif board[0] == board[4] and board[4] == board[8]:
        return endGame(board[0])
    elif board[2] == board[4] and board[4] == board[6]:
        return endGame(board[2])


def play(btn):
    global x_o, autoRole, restPosition
    x_o = 'O' if x_o == 'X' else 'X'
    if (x_o == 'O'):
        color = '#f00'
    else:
        color = '#00f'
    restPosition.remove(btn)
    if btn == 1:
        btn1.config(state=DISABLED, text=x_o, disabledforeground=color)
        board[0] = x_o
    elif btn == 2:
        btn2.config(state=DISABLED, text=x_o, disabledforeground=color)
        board[1] = x_o
    elif btn == 3:
        btn3.config(state=DISABLED, text=x_o, disabledforeground=color)
        board[2] = x_o
    elif btn == 4:
        btn4.config(state=DISABLED, text=x_o, disabledforeground=color)
        board[3] = x_o
    elif btn == 5:
        btn5.config(state=DISABLED, text=x_o, disabledforeground=color)
        board[4] = x_o
    elif btn == 6:
        btn6.config(state=DISABLED, text=x_o, disabledforeground=color)
        board[5] = x_o
    elif btn == 7:
        btn7.config(state=DISABLED, text=x_o, disabledforeground=color)
        board[6] = x_o
    elif btn == 8:
        btn8.config(state=DISABLED, text=x_o, disabledforeground=color)
        board[7] = x_o
    elif btn == 9:
        btn9.config(state=DISABLED, text=x_o, disabledforeground=color)
        board[8] = x_o
    check()
    if mode.get() == 2:
        if autoRole:
            autoRole = 0
            app.update()
            sleep(.3)
            playAuto()
        else:
            if len(restPosition) > 1:
                autoRole = 1
        check()


def playAuto():
    if (board[0] == board[1]) and (3 in restPosition):
        choice = 3
    elif (board[1] == board[2]) and (1 in restPosition):
        choice = 1
    elif (board[0] == board[2]) and (2 in restPosition):
        choice = 2

    elif (board[3] == board[4]) and (6 in restPosition):
        choice = 6
    elif (board[4] == board[5]) and (4 in restPosition):
        choice = 4
    elif (board[3] == board[5]) and (5 in restPosition):
        choice = 5

    elif (board[6] == board[7]) and (9 in restPosition):
        choice = 9
    elif (board[7] == board[8]) and (7 in restPosition):
        choice = 7
    elif (board[6] == board[8]) and (8 in restPosition):
        choice = 8

    elif (board[0] == board[3]) and (7 in restPosition):
        choice = 7
    elif (board[3] == board[6]) and (1 in restPosition):
        choice = 1
    elif (board[0] == board[6]) and (4 in restPosition):
        choice = 4

    elif (board[1] == board[4]) and (8 in restPosition):
        choice = 8
    elif (board[4] == board[7]) and (2 in restPosition):
        choice = 2
    elif (board[1] == board[7]) and (5 in restPosition):
        choice = 5

    elif (board[2] == board[5]) and (9 in restPosition):
        choice = 9
    elif (board[5] == board[8]) and (3 in restPosition):
        choice = 3
    elif (board[2] == board[8]) and (6 in restPosition):
        choice = 6

    elif (board[0] == board[4]) and (9 in restPosition):
        choice = 9
    elif (board[4] == board[8]) and (1 in restPosition):
        choice = 1
    elif (board[0] == board[8]) and (5 in restPosition):
        choice = 5

    elif (board[2] == board[4]) and (7 in restPosition):
        choice = 7
    elif (board[4] == board[6]) and (3 in restPosition):
        choice = 3
    elif (board[2] == board[6]) and (5 in restPosition):
        choice = 5

    else:
        choice = select(restPosition)

    play(choice)


def start():
    if mode.get():
        m1p.config(state=DISABLED)
        m2p.config(state=DISABLED)
        start.config(state=DISABLED)
        btn1.config(state=NORMAL)
        btn2.config(state=NORMAL)
        btn3.config(state=NORMAL)
        btn4.config(state=NORMAL)
        btn5.config(state=NORMAL)
        btn6.config(state=NORMAL)
        btn7.config(state=NORMAL)
        btn8.config(state=NORMAL)
        btn9.config(state=NORMAL)
        reset.config(state=NORMAL)
        if mode.get() == 2:
            play(select(restPosition))
    else:
        app.update()
        return showwarning('DRS-X_O', 'Please select mode "2 player" or "1 player"')


def reset():
    global board, restPosition, x_o, autoRole
    board = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    ]
    restPosition = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    ]
    autoRole = 0
    x_o = 'X'
    l.config(text='X-O', fg='#000')
    m1p.config(state=NORMAL)
    m2p.config(state=NORMAL)
    start.config(state=NORMAL)
    btn1.config(state=DISABLED, text=' ')
    btn2.config(state=DISABLED, text=' ')
    btn3.config(state=DISABLED, text=' ')
    btn4.config(state=DISABLED, text=' ')
    btn5.config(state=DISABLED, text=' ')
    btn6.config(state=DISABLED, text=' ')
    btn7.config(state=DISABLED, text=' ')
    btn8.config(state=DISABLED, text=' ')
    btn9.config(state=DISABLED, text=' ')
    reset.config(state=DISABLED)


x_o = 'X'
autoRole = 0
board = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
restPosition = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

app = Tk()
app.title('X-O')
app.geometry('398x630+650+180')

l = Label(text='X-O', font=('verdana', 30),
          borderwidth=4, relief="ridge", width=15)
l.grid(row=0, columnspan=3, pady=10)

mode = IntVar()
m1p = Radiobutton(text='2 Player', font=('curier',),
                  value=1, variable=mode, cursor='hand2', activebackground='#d8cfff')
m1p.grid(row=1, column=0)
m2p = Radiobutton(text='1 Player', font=('curier',),
                  value=2, variable=mode, cursor='hand2', activebackground='#d8cfff')
m2p.grid(row=1, column=1)
start = Button(text='Start', font=('curier'), width=12, fg='#006400', bg='#d4e6d4', cursor='hand2',
               relief=GROOVE, command=start)
start.grid(row=1, column=2, pady=10)


btn1 = Button(text=' ', width=3, height=1, relief=GROOVE, state=DISABLED, font=(
    "curier", 50, 'bold'),cursor='circle', command=lambda: play(1))
btn1.grid(row=2, column=0)
btn2 = Button(text=' ', width=3, height=1, relief=GROOVE, state=DISABLED, font=(
    "curier", 50, 'bold'),cursor='circle', command=lambda: play(2))
btn2.grid(row=2, column=1)
btn3 = Button(text=' ', width=3, height=1, relief=GROOVE, state=DISABLED, font=(
    "curier", 50, 'bold'),cursor='circle', command=lambda: play(3))
btn3.grid(row=2, column=2)
btn4 = Button(text=' ', width=3, height=1, relief=GROOVE, state=DISABLED, font=(
    "curier", 50, 'bold'),cursor='circle', command=lambda: play(4))
btn4.grid(row=3, column=0)
btn5 = Button(text=' ', width=3, height=1, relief=GROOVE, state=DISABLED, font=(
    "curier", 50, 'bold'),cursor='circle', command=lambda: play(5))
btn5.grid(row=3, column=1)
btn6 = Button(text=' ', width=3, height=1, relief=GROOVE, state=DISABLED, font=(
    "curier", 50, 'bold'),cursor='circle', command=lambda: play(6))
btn6.grid(row=3, column=2)
btn7 = Button(text=' ', width=3, height=1, relief=GROOVE, state=DISABLED, font=(
    "curier", 50, 'bold'),cursor='circle', command=lambda: play(7))
btn7.grid(row=4, column=0)
btn8 = Button(text=' ', width=3, height=1, relief=GROOVE, state=DISABLED, font=(
    "curier", 50, 'bold'),cursor='circle', command=lambda: play(8))
btn8.grid(row=4, column=1)
btn9 = Button(text=' ', width=3, height=1, relief=GROOVE, state=DISABLED, font=(
    "curier", 50, 'bold'),cursor='circle', command=lambda: play(9))
btn9.grid(row=4, column=2)

reset = Button(text='Reset', width=20, font=('arier', 20, 'bold'),
               state=DISABLED, command=reset, cursor='exchange', fg='#ff9500', relief=GROOVE)
reset.grid(row=5, columnspan=3, pady=20)

app.mainloop()
