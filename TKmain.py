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

catalog_frames['Peripherals'].grid_forget()
catalog_frames['Games'].grid_forget()

''' Prepare Computers Catalog '''
computers = store.allprods.computers
comp_menu = PL.buildCatalog(computer_frame, computers, 0)
comp_frame_button = store.createMenuBtn(store_menu, catalog_frames, 'Computers', 0, 0)

''' Prepare Peripherals Catalog '''
peripherals = store.allprods.peripherals
perip_menu = PL.buildCatalog(peripheral_frame, peripherals, 1)
perip_frame_button = store.createMenuBtn(store_menu, catalog_frames, 'Peripherals', 0, 1)

''' Prepare Games Catalog '''
games = store.allprods.games
game_menu = PL.buildCatalog(game_frame, games, 2)
game_frame_button = store.createMenuBtn(store_menu, catalog_frames, 'Games', 0, 2)



root.mainloop()