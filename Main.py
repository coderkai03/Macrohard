from Customer import Profile
from View import View
from ProductList import Products

def numToCategory(num):
    num-=1
    cat1 = plist.compSize
    cat2 = plist.periSize
    cat3 = plist.gameSize
    if num <= cat1:
        return ['computers', num]
    elif num <= cat1+cat2:
        return ['peripherals', num-cat1]
    elif num <= cat1+cat2+cat3:
        return ['games', num-cat2-cat1]

#test create profile
cus1 = Profile()

#test create product list
plist = Products()


#show avail products
plist.display_products()

#ask user to add items to cart
uInput = int(input("Enter an item #: "))

#add to cart
itemInput = numToCategory(uInput)
uItem = plist.get_item(itemInput[0], itemInput[1])
cus1.addItem(uItem)

#display cart
cus1.display_cart()