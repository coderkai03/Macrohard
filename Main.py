from Customer import Profile
from View import View
from ProductList import Products
from Prompt import Prompt
from Store import Macrohard


print('--- Welcome to Macrohard! -----------------------------------')

#create prompt
pt = Prompt()
uInfo = pt.get_customer_info()
uDisc = pt.get_discount()

#test create profile
cus1 = Profile(uInfo, uDisc)

#test create product list
plist = Products()

#store mechanics
MH = Macrohard(cus1.user_data['name'])

#create view
view = View()


#show avail products
plist.display_products()

while (True):
    #ask user to add items to cart
    print("Enter an item #: ")
    uInput = pt.validate_input(0, plist.catSize)
    if not uInput:
        break

    #add to cart
    uItem = plist.get_item(uInput)
    cus1.addItem(uItem)

    print('\n')

#display cart
MHBill = MH.checkout(cus1)
cusBill = cus1.export_cart()

view.print_bill(cusBill, MHBill)
view.export_bill(cusBill, MHBill)

print('\n\nExported bill to Macrohard-Bill.txt')
print('\n--- Thanks for shopping with Macrohard! ---------------------------------------\n')