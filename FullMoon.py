from tkinter import *
from tkinter import messagebox
mp = Tk()
mp.geometry("200x170")
mp.title('Fodd Select')
lb = Label(mp, text = 'Please select food item.')
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()

cb1 = Checkbutton(mp, text = 'Noodle : 45฿', variable = v1, onvalue = 1, offvalue = 0)
cb1.var = v1
cb1.pack()

cb2 = Checkbutton(mp, text = 'Fried Rice : 50฿', variable = v2, onvalue = 1, offvalue = 0)
cb2.var = v2
cb2.pack()

cb3 = Checkbutton(mp, text = 'Plain Water : 5฿', variable = v3, onvalue = 1, offvalue = 0)
cb3.var = v3
cb3.pack()

cb4 = Checkbutton(mp, text = 'Orange juice : 15฿', variable = v4, onvalue = 1, offvalue = 0)
cb4.var = v4
cb4.pack()

def calc():
    if cb1.var.get() == 1:
        n = 45
    else:
        n = 0
    if cb2.var.get() == 1:
        fd = 50
    else:
        fd = 0
    if cb3.var.get() == 1:
        w = 5
    else:
        w = 0
    if cb4.var.get() == 1:
        oj = 15
    else:
        oj = 0
    sum = n + fd + w + oj
    messagebox.showinfo('Prices', 'Total : ' + str(sum))

bt = Button(mp, text = 'Order', bg = 'blue', fg = 'white', command = calc)
bt.pack()
mp.mainloop()