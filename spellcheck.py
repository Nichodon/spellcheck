from Tkinter import *
#suff for da win
lines = []
fill = open('words.suff', 'r')
asdfasdf = ''
for l in fill:
    lines.append(l.strip())
    if len(l.strip()) > len(asdfasdf):
        asdfasdf = l.strip()
print asdfasdf
tk = Tk()
e = Entry(tk)
e.pack()
x = StringVar(value='Right')
l = Label(tk, textvariable=x)
l.pack()
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
def evv(event):
    if e.get() in lines:
        x.set('Right')
    else:
        x.set('Wrong')
tk.bind('<Return>', evv)
center(tk)
mainloop()