from tkinter import *
import tkinter.font as tkFont
from Customer import Customer
from View import View
from ProductList import ProductList
from Store import Macrohard
from PIL import Image, ImageTk

''' Module assets '''
MH = Macrohard('Rian')
PL = ProductList()
CSTMR = Customer()

root = Tk()
root.title('Macrohard')
#root.pack()

# Logo
img_path = 'msft-cool-logo.jpg'
img = Image.open(img_path)
img = img.resize((80, 80))
logo = ImageTk.PhotoImage(img)

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

store_sec_frame = Frame(app_screens['StoreWindow'])
store_sec_frame.grid(row=0, column=1, sticky='e')

for sec in switch_store_sections:
    switch_store_sections[sec] = Button(
        store_sec_frame,
        text=sec,
        command=lambda x=sec: hideBtn(x)
    )

img_label = Label(store_sec_frame, image=logo)
img_label.grid(row=0, column=0, padx=50, pady=50)
    
switch_store_sections['Store'].grid(row=0, column=1)
switch_store_sections['Cart'].grid(row=0, column=2)
switch_store_sections['Checkout'].grid(row=0, column=3)
switch_store_sections['Account'].grid(row=0, column=4)



''' Account login window'''

account_login = Frame(app_screens['AccountLogin'])
account_login.grid(row=1, column=0)

greetframe = Frame(app_screens['AccountLogin'])
greetframe.grid(row=0, column=0)

greeting = Label(greetframe, text='Welcome to Macrohard!')
greeting.grid(row=0, column=0, pady=20)

img_label = Label(greetframe, image=logo)
img_label.grid(row=0, column=1, padx=50, pady=50)

#enter user info
login_assets = CSTMR.userInfoEntries(account_login)

submit_frame = Frame(app_screens['AccountLogin'])
submit_frame.grid(row=2, column=0, pady=30)

#save user info to Customer()
submit_info = Button(
    submit_frame,
    text='Submit',
    command= lambda: [CSTMR.saveData(
        app_screens,
        store_screens,
        login_assets['Name'].get(), 
        login_assets['Address'].get(),
        login_assets['Demographics']['Var'].get()
    ), updateNameDisplay(), checkout_label.config(text=f'{CSTMR.name}\'s checkout')]
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

user_stats = Frame(store)
user_stats.grid(row=0, column=0)

#display user name
name_label = Label(user_stats)
name_label.grid(row=0, column=0, padx=30)

#cart quant
cart_quant_label = Label(user_stats, text=f'Cart: 0 items')
cart_quant_label.grid(row=0, column=1, padx=30)

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

    tot_quant=0
    for quant in comp_cart['Quantity']:
        tot_quant += quant.get()
    
    for quant in perip_cart['Quantity']:
        tot_quant += quant.get()
         
    for quant in games_cart['Quantity']:
        tot_quant += quant.get()
    
    cart_quant_label.config(text=f'Cart: {tot_quant} items')

    updateCheckout()
    updateSubtotals()

#Show Computers, hide Peripherals, Games
catalog_frames['Peripherals'].grid_forget()
catalog_frames['Games'].grid_forget()


''' Account '''

acc_label_frame = Frame(store_screens['Account'])
acc_label_frame.grid(row=0, column=0)

acc_det_label = Label(acc_label_frame, text='Account Details')
acc_det_label.grid(pady=20)

acc_edit_frame = Frame(store_screens['Account'])
acc_edit_frame.grid(row=1, column=0)

edit_account = CSTMR.userInfoEntries(acc_edit_frame)

acc_submit_frame = Frame(store_screens['Account'])
acc_submit_frame.grid(row=2, column=0, pady=30)

submit_edits = Button(
    acc_submit_frame,
    text='Submit',
    command= lambda: [CSTMR.saveData(
        app_screens,
        store_screens,
        edit_account['Name'].get(), 
        edit_account['Address'].get(),
        edit_account['Demographics']['Var'].get()
    ), updateNameDisplay(), checkout_label.config(text=f'{CSTMR.name}\'s checkout')]
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
comp_label.grid(row=0, column=0, pady=20)

comp_items = None

# Peripherals cart
perip_cart_display = Frame(cart_sections)
perip_cart_display.grid(row=2, column=0, padx=20)

perip_label = Label(perip_cart_display, text='Peripherals')
perip_label.grid(row=0, column=0, pady=20)

perip_items = None

# Games cart
game_cart_display = Frame(cart_sections)
game_cart_display.grid(row=3, column=0, padx=20)

game_label = Label(game_cart_display, text='Games')
game_label.grid(row=0, column=0, pady=20)

game_items = None


''' Checkout '''

# display cart again w/ Place Order btn
checkout_frame = Frame(store_screens['Checkout'])
checkout_frame.grid(row=0, column=0)

checkout_label = Label(checkout_frame)
checkout_label.grid(row=1, column=0)

checkout_lbls_frame = Frame(checkout_frame)
checkout_lbls_frame.grid()

def createTableLbls():
    global checkout_label
    global tableLabels

    cols=0
    for lbl in tableLabels:
        if cols == 0:
            lbl_text = f'{lbl:<50}'
        elif cols == 1:
            lbl_text = f'{lbl:>40}'
        else:
            lbl_text = f'{lbl:>20}'

        tableLabels[lbl] = Label(checkout_lbls_frame, text=lbl_text)
        tableLabels[lbl].grid(row=0, column=cols)

        # if cols == 0:
        #     tableLabels[lbl].config(anchor='w')
        # elif cols == 2:
        #     tableLabels[lbl].config(anchor='e')

        cols+=1

tableLabels = {
    'Item name': None,
    'Quantity': None,
    'Price': None
}
createTableLbls()

# for the checkout items
checkout_categories = Frame(checkout_frame)
checkout_categories.grid(row=3, column=0)

# Computer checkout
comp_checkout_frame = Frame(checkout_categories)
comp_checkout_frame.grid(row=1, column=0)

comp_check = None

# Peripheral checkout
perip_checkout_frame = Frame(checkout_categories)
perip_checkout_frame.grid(row=2, column=0)

perip_check = None

# Game checkout
game_checkout_frame = Frame(checkout_categories)
game_checkout_frame.grid(row=3, column=0)

game_check = None

def updateCheckout():
    global comp_check
    global perip_check
    global game_check

    comp_check = CSTMR.buildCheckout('Computers', comp_checkout_frame)
    perip_check = CSTMR.buildCheckout('Peripherals', perip_checkout_frame)
    game_check = CSTMR.buildCheckout('Games', game_checkout_frame)

# Final subtotals + bill
def updateSubtotals():
    print('UI SUBTOTAL', CSTMR.subtotal)
    tax = CSTMR.subtotal*.0725
    ship = CSTMR.subtotal*.1
    disc = CSTMR.subtotal*CSTMR.user_discount
    grand = CSTMR.subtotal + tax + ship + disc

    lbl = 'Taxes'
    tax_lbl.config(text=f'{lbl:<30}{equal:>10}{tax:>10.2f}')

    lbl = 'Shipping'
    ship_lbl.config(text=f'{lbl:<30}{equal:>10}{ship:>10.2f}')

    lbl = 'Discount'
    disc_lbl.config(text=f'{lbl:<30}{equal:>10}{disc:>10.2f}')

    lbl = 'Grand total'
    grnd_lbl.config(text=f'{lbl:<30}{equal:>10}{grand:>10.2f}')

lbl = 'Subtotal'
equal = '$'

subtot_lbl = Label(
    checkout_categories, 
    font=tkFont.Font(family='Space Mono', size=10))
subtot_lbl.grid(row=4, column=0, pady=(30, 0))

tax_lbl = Label(
    checkout_categories,
    font=tkFont.Font(family='Space Mono', size=10))
tax_lbl.grid(row=5, column=0)

ship_lbl = Label(
    checkout_categories,
    font=tkFont.Font(family='Space Mono', size=10))
ship_lbl.grid(row=6, column=0)

disc_lbl = Label(
    checkout_categories,
    font=tkFont.Font(family='Space Mono', size=10))
disc_lbl.grid(row=7, column=0)

grnd_lbl = Label(
    checkout_categories,
    font=tkFont.Font(family='Space Mono', size=10))
grnd_lbl.grid(row=8, column=0)



#
#
#

''' DO NOT TOUCH/PASS'''
root.mainloop()
