from tkinter import *
from Store import Macrohard

store = Macrohard('Rian')

root = Tk()
#root.geometry('800x600')

# welcome = Label(frame1, text='Welcome to Macrohard!')
# welcome.pack()

frame1 = Frame(root)
frame1.grid(row=1, column=0)

frame2 = Frame(root)
frame2.grid(row=1, column=1)

comps = store.allprods.computers
for i in comps:
    prod = Checkbutton(
        frame1,
        text=i[0],
        onvalue=1,
        offvalue=0,
    ).pack(anchor='w')
    price = Label(
        frame2,
        text=i[1],
    ).pack(anchor='e')

# for i in comps:
#     #print(i)
    

root.mainloop()