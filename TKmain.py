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

# items1 = Frame(computer_frame)
# items1.grid(row=1, column=0)

# incrementers1 = Frame(computer_frame)
# incrementers1.grid(row=1, column=1)

#refactor showIncrementItem to showIncrementItem(item, prod, prod_idx, quant, quant_idx)
def showIncrementItem(item, prod_idx, quant, quant_idx):
    idx = prod_idx.index(item)
    #print(f'{idx} found')
    if item.get():
        quant[idx].configure(state='normal')
    else:
        quant[idx].configure(state='disabled')
        quant_idx[idx].set(0)

#create catalog widgets
def buildCatalog(frame, products):
    prod_buttons = []
    prod_vars = []

    quant_entries = []
    quant_vars = []

    r=0
    for i in products:
        prod_vars.append(IntVar())
        prod_buttons.append(Checkbutton(
            frame,
            text=f'{i[0]:<30}${i[1]:>10.2f}',
            font=tkFont.Font(family='Space Mono', size=10),
            variable=prod_vars[r],
            onvalue=1,
            offvalue=0,
            state='normal',
        ))

        quant_vars.append(IntVar())
        quant_entries.append(Entry(
            frame,
            textvariable=quant_vars[r],
            font=tkFont.Font(family='Space Mono', size=10),
            state='disabled',
            width=3
        ))

        quant_entries[r].grid(row=r, column=1, sticky='w')
        prod_buttons[r].grid(row=r, column=0, sticky='w')
        prod_buttons[r].configure(command=lambda item=prod_vars[r]: showIncrementItem(item, prod_vars, quant_entries, quant_vars))
        r+=1

    return {
        'Prod Buttons': prod_buttons,
        'Prod Vars': prod_vars,
        'Quant Entries': quant_entries,
        'Quant vars': quant_vars
        }


''' Prepare Computers Catalog '''
computer_frame = Frame(root)
computer_frame.pack()
computers = store.allprods.computers
comp_assets = buildCatalog(computer_frame, computers)

# for i in range(len(comps)):
#     computer_frame.grid_rowconfigure(i, minsize=comp_prods[i].winfo_reqheight())

root.mainloop()