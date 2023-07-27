from tkinter import *
from Store import Macrohard
import tkinter.font as tkFont


store = Macrohard('Rian')

root = Tk()
root.title('Macrohard')

# root.pack()

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
def buildCatalog(frame, products, col):
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

        quant_entries[r].grid(row=r, column=col+1, sticky='w')
        prod_buttons[r].grid(row=r, column=col, sticky='w')
        prod_buttons[r].configure(command=lambda item=prod_vars[r]: showIncrementItem(item, prod_vars, quant_entries, quant_vars))
        r+=1

    return {
        'Prod Buttons': prod_buttons,
        'Prod Vars': prod_vars,
        'Quant Entries': quant_entries,
        'Quant vars': quant_vars
        }

def hideCatalogs(frame, r, c):
    print(f'Hiding {frame} catalog')
    for cat in catalog_frames:
        print(f'Viewing {catalog_frames[cat]}...')
        if cat != frame:
            catalog_frames[cat].grid_forget()
    catalog_frames[frame].grid()

def createMenuBtn(label, r, c):
    return Button(
            store_menu,
            text=label,
            command=lambda x=label: hideCatalogs(x, r, c)
        ).grid(row=r, column=c)

# def showCatalog(frame, var):
#     children = frame.children
#     for child in children:
#         if child

''' Store catalog window'''
store_catalogs = Frame(root)
store_catalogs.grid(row=2, column=0)

store_menu = Frame(root)
store_menu.grid(row=1, column=0)

computer_frame = Frame(store_catalogs)
computer_frame.grid(row=0, column=0)

peripheral_frame = Frame(store_catalogs)
peripheral_frame.grid(row=0, column=1)

game_frame = Frame(store_catalogs)
game_frame.grid(row=0, column=2)

catalog_frames = {
    'Computers': computer_frame,
    'Peripherals': peripheral_frame,
    'Games': game_frame
}

''' Prepare Computers Catalog '''
computers = store.allprods.computers
comp_assets = buildCatalog(computer_frame, computers, 0)
comp_frame_button = createMenuBtn('Computers', 0, 0)

''' Prepare Peripherals Catalog '''
peripherals = store.allprods.peripherals
perip_assets = buildCatalog(peripheral_frame, peripherals, 1)
perip_frame_button = createMenuBtn('Peripherals', 0, 1)

''' Prepare Games Catalog '''
games = store.allprods.games
game_assets = buildCatalog(game_frame, games, 2)
game_frame_button = createMenuBtn('Games', 0, 2)



root.mainloop()