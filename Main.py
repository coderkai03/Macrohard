from Customer import Profile
from Prompt import Prompt

#test get_customer_info
#use return value to create a new Profile object
c1 = Profile(**Prompt.get_customer_info())

#print customer's info
print(c1)

#test validate_input
print('Enter a number between 1 and 10.')
num = Prompt.validate_input(1, 10)
print(f'You entered {num}')