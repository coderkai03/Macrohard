from tkinter import *
from Customer import Customer
from View import View
from ProductList import ProductList
from Prompt import Prompt
from Store import Macrohard

''' Module assets '''
MH = Macrohard('Rian')
PL = ProductList()
CSTMR = Customer()

root = Tk()
root.title('Macrohard')
#root.pack()

app_screens = dict()
app_screens['AccountLogin'] = Frame(root) #login screen (only shown once)
app_screens['AccountLogin'].pack(padx=100, pady=30)

app_screens['StoreWindow'] = Frame(root) #store screen
# Packed inside CSTMR.saveData()

store_screens = dict()
store_screens['Store'] = Frame(app_screens['StoreWindow']) #store: catalogs
store_screens['Store'].grid(row=2, column=1)

store_screens['Account'] = Frame(app_screens['StoreWindow']) #store: account
store_screens['Account'].grid(row=2, column=1)

store_screens['Cart'] = Frame(app_screens['StoreWindow']) #store: account
store_screens['Cart'].grid(row=2, column=1)

store_screens['Checkout'] = Frame(app_screens['StoreWindow']) #store: account
store_screens['Checkout'].grid(row=2, column=1)



''' Store sections'''
def hideBtn(targ):    
    for s in switch_store_sections:
        if s != targ:
                store_screens[s].grid_forget()
    
    store_screens[targ].grid(row=2, column=1)


switch_store_sections = {
    'Store': None,
    'Cart': None,
    'Checkout': None,
    'Account': None
}

for sec in switch_store_sections:
    switch_store_sections[sec] = Button(
        app_screens['StoreWindow'],
        text=sec,
        command=lambda x=sec: hideBtn(x)
    )
    
switch_store_sections['Store'].grid(row=1, column=0)
switch_store_sections['Cart'].grid(row=1, column=2)
switch_store_sections['Checkout'].grid(row=3, column=0)
switch_store_sections['Account'].grid(row=3, column=2)



''' Account login window'''

account_login = Frame(app_screens['AccountLogin'])
account_login.grid()

greeting = Label(account_login, text='Welcome to Macrohard!')
greeting.grid(row=0, column=0, pady=20)

#enter user info
login_assets = CSTMR.userInfoEntries(account_login)

#save user info to Customer()
submit_info = Button(
    account_login,
    text='Submit',
    command= lambda: CSTMR.saveData(
        app_screens,
        store_screens,
        login_assets['Name'].get(), 
        login_assets['Address'].get(),
        login_assets['Demographics']['Var'].get()
    )
)
submit_info.grid()


''' Account '''
acc_det_label = Label(store_screens['Account'], text='Account Details')
acc_det_label.grid(pady=20)

edit_account = CSTMR.userInfoEntries(store_screens['Account'])

submit_edits = Button(
    store_screens['Account'],
    text='Submit',
    command= lambda: CSTMR.saveData(
        store_screens,
        login_assets['Name'].get(), 
        login_assets['Address'].get(),
        login_assets['Demographics']['Var'].get()
    )
)
submit_edits.grid()


''' Store '''

#MH Store
store = Frame(store_screens['Store'])
store.grid()

#Comps, Perips, Games sections
store_menu = Frame(store)
store_menu.grid(row=0, column=0, sticky='w')

#Catalog frames
computer_frame = Frame(store)
computer_frame.grid(row=1, column=0)

peripheral_frame = Frame(store)
peripheral_frame.grid(row=1, column=0)

game_frame = Frame(store)
game_frame.grid(row=1, column=0)

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
    catalog_assets[cat] = MH.buildCatAssets(store_menu,
                                               catalog_frames[cat],
                                               catalog_frames,
                                               columns,
                                               cat)
    # catalog_assets:
    # 'Computers'
    # 'Peripherals'
    # 'Games'

    columns+=1

#add to customer cart
comp_cart = {
    'Items': catalog_assets['Computers']['Menu']['ProdVars'],
    'Quantity': catalog_assets['Computers']['Menu']['QuantVars']
}

perip_cart = {
    'Items': catalog_assets['Peripherals']['Menu']['ProdVars'],
    'Quantity': catalog_assets['Peripherals']['Menu']['QuantVars']
}

games_cart = {
    'Items': catalog_assets['Games']['Menu']['ProdVars'],
    'Quantity': catalog_assets['Games']['Menu']['QuantVars']
}

add_cart_button = Button(
    store,
    text='Add to cart',
    command=lambda: MH.addToCart(CSTMR, comp_cart, perip_cart, games_cart)
)
add_cart_button.grid(row=3, column=0)

#Show Computers, hide Peripherals, Games
catalog_frames['Peripherals'].grid_forget()
catalog_frames['Games'].grid_forget()


''' Cart '''

# coming soon...

''' Account '''





''' DO NOT TOUCH/PASS'''
root.mainloop()
