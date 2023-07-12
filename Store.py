from ProductList import *
from Customer import *

class Macrohard:
    allprods = Products()
    taxRate = .0725
    shipRate = .05

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
        subdiscount = discount * subtotal
        subship = s.shipRate * subtotal
        
        total = subtotal + subtax + subship #- subdiscount

        print('--- Checkout --------------------------')
        user.display_cart()
        print('\n')
        print(f'Subtotal: ${subtotal:.2f}')
        print(f'Sales tax: ${subtax:.2f}')
        print(f'Shipping: ${subship:.2f}')
        print(f'Discount: -${subdiscount:.2f}')
        print(f'\nTotal: ${total:.2f}')