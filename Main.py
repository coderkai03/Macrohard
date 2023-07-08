from Customer import Profile
from View import View

#test get_customer_info
#use return value to create a new Profile object
c1 = Profile(**View.get_customer_info())

#print customer's info
print(c1)

#test validate_input
print('Enter a number between 1 and 10.')
num = View.validate_input(1, 10)
print(f'You entered {num}')

#add products to cart
#use return value to add products to cart
c1.add_to_cart(View.get_products())