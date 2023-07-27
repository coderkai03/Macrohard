from tkinter import *
import tkinter.font as tkFont
from Customer import Profile
from View import View
from ProductList import ProductList
from Prompt import Prompt
from Store import Macrohard


store = Macrohard('Rian')
PL = ProductList()

root = Tk()
root.title('Macrohard')


''' Store catalog window'''
store_catalogs = Frame(root)
store_catalogs.grid(row=2, column=0)

store_menu = Frame(root)
store_menu.grid(row=1, column=0)

''' Catalog frames '''
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

catalog_assets = {
    'Computers': None,
    'Peripherals': None,
    'Games': None
}

columns=0
for cat in catalog_assets:
    catalog_assets[cat] = store.buildCatAssets(store_menu,
                                               catalog_frames[cat],
                                               catalog_frames,
                                               columns,
                                               cat)
    #print(f'\n\n{cat} Created: ', catalog_assets[cat])
    columns+=1

catalog_frames['Peripherals'].grid_forget()
catalog_frames['Games'].grid_forget()

root.mainloop()