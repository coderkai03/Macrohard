from tkinter import *
import tkinter.font as tkFont
from Customer import Customer
from View import View
from ProductList import ProductList
from Prompt import Prompt
from Store import Macrohard

''' Module assets '''
store = Macrohard('Rian')
PL = ProductList()
CSTMR = Customer()

root = Tk()
root.title('Macrohard')
root.geometry('600x400')

app_screens = dict()
app_screens['AccountLogin'] = Frame(root) #login screen
app_screens['StoreWindow'] = Frame(root) #store screen

''' Account login window'''
app_screens['AccountLogin'].pack(anchor='center')

account_login = Frame(app_screens['AccountLogin'])
account_login.grid()

greeting = Label(account_login, text='Welcome to Macrohard!')
greeting.grid(row=0, column=0)

#enter user info
login_assets = CSTMR.userInfoEntries(account_login)

#save user info to Customer()
submit_info = Button(
    account_login,
    text='Submit',
    command= lambda: CSTMR.saveData(
        app_screens,
        login_assets['Name'].get(), 
        login_assets['Address'].get(),
    )
)
submit_info.grid()

''' Store catalog window'''

#Store frames
#app_screens['StoreWindow'] = Frame(root)
#app_screens['StoreWindow'].grid()

store_catalogs = Frame(app_screens['StoreWindow'])
store_catalogs.grid(row=2, column=0)

store_menu = Frame(app_screens['StoreWindow'])
store_menu.grid(row=1, column=0, sticky='w')

#Catalog frames
computer_frame = Frame(store_catalogs)
computer_frame.grid(row=0, column=0)

peripheral_frame = Frame(store_catalogs)
peripheral_frame.grid(row=0, column=1)

game_frame = Frame(store_catalogs)
game_frame.grid(row=0, column=2)

#Create catalog assets
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

#Show Computers, hide Peripherals, Games
catalog_frames['Peripherals'].grid_forget()
catalog_frames['Games'].grid_forget()

root.mainloop()