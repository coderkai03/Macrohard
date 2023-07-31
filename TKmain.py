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
    command= lambda: [CSTMR.saveData(
        app_screens,
        store_screens,
        login_assets['Name'].get(), 
        login_assets['Address'].get(),
        login_assets['Demographics']['Var'].get()
    ), updateNameDisplay()]
)
submit_info.grid()

def updateNameDisplay():
    inText = 'Hello, '+str(CSTMR.name)+'!\nDeliver to: '+str(CSTMR.address)
    name_label.config(pady=20, text=inText)

    inText = str(CSTMR.name)+'\'s cart'
    customer_label.config(pady=20, text=inText)


''' Store '''

#MH Store
store = Frame(store_screens['Store'])
store.grid()

#display user name
name_label = Label(store)
name_label.grid()

#Comps, Perips, Games sections
store_menu = Frame(store)
store_menu.grid(row=1, column=0, sticky='w')

#Catalog frames
computer_frame = Frame(store)
computer_frame.grid(row=2, column=0)

peripheral_frame = Frame(store)
peripheral_frame.grid(row=2, column=0)

game_frame = Frame(store)
game_frame.grid(row=2, column=0)

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
    command=lambda: [MH.addToCart(CSTMR, comp_cart, perip_cart, games_cart),
                    updateCarts()]
)
add_cart_button.grid(row=3, column=0)

def updateCarts():
    comp_items = CSTMR.buildCartLbls('Computers', comp_cart_display)
    perip_items = CSTMR.buildCartLbls('Peripherals', perip_cart_display)
    game_items = CSTMR.buildCartLbls('Games', game_cart_display)

#Show Computers, hide Peripherals, Games
catalog_frames['Peripherals'].grid_forget()
catalog_frames['Games'].grid_forget()


''' Account '''
acc_det_label = Label(store_screens['Account'], text='Account Details')
acc_det_label.grid(pady=20)

edit_account = CSTMR.userInfoEntries(store_screens['Account'])

submit_edits = Button(
    store_screens['Account'],
    text='Submit',
    command= lambda: [CSTMR.saveData(
        app_screens,
        store_screens,
        edit_account['Name'].get(), 
        edit_account['Address'].get(),
        edit_account['Demographics']['Var'].get()
    ), updateNameDisplay()]
)
submit_edits.grid()


''' Cart '''

cart_sections = Frame(store_screens['Cart'])
cart_sections.grid()

customer_label = Label(cart_sections)
customer_label.grid(row=0, column=0)

# Computers cart
comp_cart_display = Frame(cart_sections)
comp_cart_display.grid(row=1, column=0, padx=20)

comp_label = Label(comp_cart_display, text='Computers')
comp_label.grid(row=0, column=0, padx=20)

comp_items = None

# Peripherals cart
perip_cart_display = Frame(cart_sections)
perip_cart_display.grid(row=2, column=0, padx=20)

perip_label = Label(perip_cart_display, text='Peripherals')
perip_label.grid(row=0, column=0, padx=20)

perip_items = None

# Games cart
game_cart_display = Frame(cart_sections)
game_cart_display.grid(row=3, column=0, padx=20)

game_label = Label(game_cart_display, text='Games')
game_label.grid(row=0, column=0, padx=20)

game_items = None

#
#
#

''' DO NOT TOUCH/PASS'''
root.mainloop()
