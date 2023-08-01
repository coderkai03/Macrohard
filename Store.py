from ProductList import *
from Customer import *
from tkinter import *

class Macrohard:
    allprods = ProductList()
    taxRate = .0725
    shipRate = .05

    store_bill=[]

    def __init__(self, name) -> None:
        self.cname = name

    ''' BACKEND FUNCS '''

    def showCatalog(s):
        print('--- Macrohard -------------------------')
        s.allprods.display_products()
        print('Quit: 0')
        print('Enter an item #: ')

    def checkout(s, user):
        cartsize = range(0, len(user.cart))
        subtotal = 0
        for cost in cartsize:
            subtotal += user.cart[cost][1]

        subtax = s.taxRate * subtotal
        subdiscount = user.user_discount[1] * subtotal
        disctitle = 'Discount ('+user.user_discount[0]+'):'
        subship = s.shipRate * subtotal
        
        total = subtotal + subtax + subship + subdiscount
        
        pad1 = 54
        s.store_bill.append('\n{}${:>10.2f}'.format('Subtotal:'.ljust(pad1), subtotal))
        s.store_bill.append('\n{}${:>10.2f}'.format('Sales tax:'.ljust(pad1), subtax))
        s.store_bill.append('\n{}${:>10.2f}'.format('Shipping:'.ljust(pad1), subship))
        s.store_bill.append('\n{}${:>10.2f}'.format(disctitle.ljust(pad1), subdiscount))
        s.store_bill.append('\n{}${:>10.2f}'.format('Total:'.ljust(pad1), total))

        return s.store_bill
    
    ''' UI FUNCS '''

    def createMenuBtn(s, store_menu, cat_frames, label, c):
        return Button(
                store_menu,
                text=label,
                command=lambda x=label: s.hideCatalogs(x, cat_frames)
            ).grid(row=0, column=c)
    
    def hideCatalogs(s, frame, catalog_frames):
        print(f'Showing {frame, catalog_frames}')
        for cat in catalog_frames:
            if cat != frame:
                catalog_frames[cat].grid_forget()
                print(f'Forgot {cat}!')
                # mid_prog=True
        catalog_frames[frame].grid(row=2, column=0)
        print(f'Rendered {frame}!')

    def buildCatAssets(s, root_frame, frame, cat_frames, col, label):
        menu = s.allprods.buildCatalog(frame, s.allprods.categories[label], col)
        frame_button = s.createMenuBtn(root_frame, cat_frames, label, col)
        return {
            'Menu': menu,
            'MenuButton': frame_button
        }
    
    def createCartEntry(s, cat, var, cat_vars):
        prod_idx = cat_vars['Items'].index(var) # gets the item name index
        quant = cat_vars['Quantity'][prod_idx].get() # gets the quantity
        return [
            s.allprods.categories[cat][prod_idx][0],
            quant
        ]
    
    def addToCart(s, customer, comp_vars, perip_vars, games_vars):
        comp_items={}
        print('\n\nComputer cart:')
        item_idx=0
        for var in comp_vars['Items']:
            if var.get(): # box checked?
                if comp_vars['Quantity'][comp_vars['Items'].index(var)].get(): # quant>0?
                    itemName, quantity = s.createCartEntry('Computers', var, comp_vars)
                    comp_items[itemName] = quantity # adds dict item to cart
                    customer.subtotal += quantity * s.allprods.categories['Computers'][item_idx][1]
                    print(f'{itemName}: {quantity}')
            item_idx+=1

        perip_items={}
        print('\n\nPeripheral cart:')
        item_idx=0
        for var in perip_vars['Items']:
            if var.get(): # box checked?
                if perip_vars['Quantity'][perip_vars['Items'].index(var)].get(): # quant>0?
                    itemName, quantity = s.createCartEntry('Peripherals', var, perip_vars)
                    perip_items[itemName] = quantity # adds dict item to cart
                    customer.subtotal += quantity * s.allprods.categories['Peripherals'][item_idx][1]
                    print(f'{itemName}: {quantity}')

        games_items={}
        print('\n\nGames cart:')
        item_idx=0
        for var in games_vars['Items']:
            if var.get(): # box checked?
                if games_vars['Quantity'][games_vars['Items'].index(var)].get(): # quant>0?
                    itemName, quantity = s.createCartEntry('Games', var, games_vars)
                    games_items[itemName] = quantity # adds dict item to cart
                    customer.subtotal += quantity * s.allprods.categories['Games'][item_idx][1]
                    print(f'{itemName}: {quantity}')

        # finally, assign all carts to CSTMR cart
        customer.cart['Computers'] = comp_items
        customer.cart['Peripherals'] = perip_items
        customer.cart['Games'] = games_items

        # test cart display
        #customer.display_cart()