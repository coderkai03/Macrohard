from tkinter import *
from Store import Macrohard
import tkinter.font as tkFont

store = Macrohard('Rian')

root = Tk()
root.title('Macrohard')

print(1 if 'Space Mono' in tkFont.families() else 0)

root.geometry('800x600')

# welcome = Label(items1, text='Welcome to Macrohard!')
# welcome.pack()

items1 = Frame(root)
items1.grid(row=1, column=0)

# prices1 = Frame(root)
# prices1.grid(row=1, column=1)

comps = store.allprods.computers
r=0
for i in comps:
    prod = Checkbutton(
        items1,
        text=f'{i[0]:<50}${i[1]:>10.2f}',
        font=tkFont.Font(family='Space Mono', size=10),
        onvalue=1,
        offvalue=0,
    ).pack(anchor='w')#.grid(row=r, column=0)
    r+=1
    

root.mainloop()