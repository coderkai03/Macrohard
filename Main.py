from Customer import Profile
from View import View
from ProductList import Products



#test create profile
cus1 = Profile()

#test create product list
plist = Products()

#create prompt
pt = View()


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

    #display cart
    cus1.display_cart()
    print('\n')