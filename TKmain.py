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
app_screens['AccountLogin'] = Frame(root) #login screen
app_screens['StoreWindow'] = Frame(root) #store screen

''' Account login window'''
app_screens['AccountLogin'].pack(anchor='center', padx=100, pady=30)

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
        login_assets['Name'].get(), 
        login_assets['Address'].get(),
        login_assets['Demographics']['Var'].get()
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
    catalog_assets[cat] = MH.buildCatAssets(store_menu,
                                               catalog_frames[cat],
                                               catalog_frames,
                                               columns,
                                               cat)
    # catalog_assets:
    # 'Computers'
    # 'Peripherals'
    # 'Games'

    # catalog_assets: checkbox/entry vars
    # checkbox (prod name): catalog_assets['Computers']['Menu']['ProdVars'] = 0/1
    # entry (prod quant): catalog_assets['Computers']['Menu']['QuantVars'] = 0<num
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
    app_screens['StoreWindow'],
    text='Add to cart',
    command=lambda: MH.addToCart(CSTMR, comp_cart, perip_cart, games_cart)
)
add_cart_button.grid()

#Show Computers, hide Peripherals, Games
catalog_frames['Peripherals'].grid_forget()
catalog_frames['Games'].grid_forget()

root.mainloop()