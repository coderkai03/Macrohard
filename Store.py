from ProductList import *
from Customer import *


class Macrohard:
    allprods = Products()
    taxRate = .0725
    shipRate = .05

    store_bill=[]

    def __init__(self, name) -> None:
        self.cname = name

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