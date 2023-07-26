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

computer_frame = Frame(root)
computer_frame.pack()

items1 = Frame(computer_frame)
items1.grid(row=1, column=0)

incrementers1 = Frame(computer_frame)
incrementers1.grid(row=1, column=1)

def showIncrementItem(item):
    idx = prod_idxs.index(item)
    print(f'{idx} found')
    if item.get():
        quantities[idx].configure(state='normal')
    else:
        quantities[idx].configure(state='disabled')
        quant_idxs[idx].set(0)

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
        computer_frame,
        text=f'{i[0]:<30}${i[1]:>10.2f}',
        font=tkFont.Font(family='Space Mono', size=10),
        variable=prod_idxs[r],
        onvalue=1,
        offvalue=0,
        state='normal',
    ))

    quant_idxs.append(IntVar())
    quantities.append(Entry(
        computer_frame,
        textvariable=quant_idxs[r],
        font=tkFont.Font(family='Space Mono', size=10),
        state='disabled',
    ))

    quantities[r].grid(row=r, column=1, sticky='w')
    prods[r].configure(command=lambda item=prod_idxs[r]: showIncrementItem(item))
    prods[r].grid(row=r, column=0, sticky='w')
    r+=1

# for i in range(len(comps)):
#     computer_frame.grid_rowconfigure(i, minsize=prods[i].winfo_reqheight())
    

root.mainloop()