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

    def createMenuBtn(s, store_menu, cat_frames, label, r, c):
        return Button(
                store_menu,
                text=label,
                command=lambda x=label: s.hideCatalogs(x, cat_frames)
            ).grid(row=r, column=c)
    
    def hideCatalogs(s, frame, catalog_frames):
        print(f'Showing {frame, catalog_frames}')
        for cat in catalog_frames:
            if cat != frame:
                catalog_frames[cat].grid_forget()
                print(f'Forgot {cat}!')
                # mid_prog=True
        catalog_frames[frame].grid()
        print(f'Rendered {frame}!')

    def buildCatAssets(s, root_frame, frame, cat_frames, col, label):
        menu = s.allprods.buildCatalog(frame, s.allprods.categories[label], col)
        frame_button = s.createMenuBtn(root_frame, cat_frames, label, 0, col)
        return {
            'Products': s.allprods.categories[label],
            'Menu': menu,
            'MenuButton': frame_button
        }