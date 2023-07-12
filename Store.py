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

    def calcBill(s, user: Profile(), discount):
        userCosts = user.cart.values()

        subtotal = sum(list(userCosts))
        subtax = s.taxRate * subtotal
        subdiscount = discount * subtotal
        subship = s.shipRate * subtotal
        
        total = subtotal + subtax + subship - subdiscount

        print('--- Checkout --------------------------')
        user.display_cart()