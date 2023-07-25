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

incrementers1 = Frame(root)
incrementers1.grid(row=1, column=1)

def showIncrementItem(item):
    idx = prod_idxs.index(item)
    print(f'{idx} found')
    quantities[idx].configure(state='normal') if item.get() else quantities[idx].configure(state='disabled')

#add to ProductList.py
comps = store.allprods.computers
r=0
prod_idxs = []
prods = []


quantities = []
quant_idxs = []
for i in comps:
    prod_idxs.append(IntVar())
    prods.append(Checkbutton(
        items1,
        text=f'{i[0]:<30}${i[1]:>10.2f}',
        font=tkFont.Font(family='Space Mono', size=10),
        variable=prod_idxs[r],
        onvalue=1,
        offvalue=0,
        state='normal',
    ))

    quant_idxs.append(IntVar())
    quantities.append(Entry(
        incrementers1,
        textvariable=quant_idxs[r],
        font=tkFont.Font(family='Space Mono', size=10),
        state='disabled',
    ))

    quantities[r].pack()
    prods[r].configure(command=lambda item=prod_idxs[r]: showIncrementItem(item))
    prods[r].pack(anchor='w')
    r+=1
    

root.mainloop()