class View:
    #validate input to be an integer between min and max
    def validate_input(min, max):
        while True:
            try:
                num = int(input('Input: '))
                if num >= min and num <= max:
                    return num
                else:
                    #throw an error to go to the except block
                    raise ValueError
            except ValueError:
                print('Invalid input. Please try again.')

    #ask user for customer info and return a dictionary
    def get_customer_info():
        print('Enter the customer\'s information.')
        name = input('Name: ')
        phone = input('Phone: ')
        email = input('Email: ')
        ZIP = input('ZIP: ')
        address = input('Address: ')
        return {
            'name': name,
            'phone': phone,
            'email': email,
            'ZIP': ZIP,
            'address': address
        }
    
    #print a list of products
    def print_products(products):
        for i in range(len(products)):
            print(f'{i + 1}. {products[i]}')