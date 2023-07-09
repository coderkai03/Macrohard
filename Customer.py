class Profile:
    #member variables
    user_data = {
        'name': None,
        'phone': None,
        'email': None,
        'ZIP': None,
        'address': None
    }

    user_discounts = {
        'veteran': False,
        'senior': False,
        'student': False
    }

    #constructor
    def __init__(s, name, phone, email, ZIP, address):
        s.user_data['name'] = name
        s.user_data['phone'] = phone
        s.user_data['email'] = email
        s.user_data['ZIP'] = ZIP
        s.user_data['address'] = address

    #methods
    def __str__(s):
        return f'''
        Name: {s.user_data['name']}
        Phone: {s.user_data['phone']}
        Email: {s.user_data['email']}
        ZIP: {s.user_data['ZIP']}
        Address: {s.user_data['address']}
        '''
    
    def add_to_cart(s, product):
        s.cart.append(product)


class Cart:
    #member variables
    computers = []
    peripherals = []
    games = []

    def addItem(s, item):
        s.computers.append(item)

    def removeItem(s, index):
        s.computers.pop(index)

    def display_cart(s):
        if s.computers:
            print("Computers:")
            for item in s.computers:
                print(f'{item[0]:<15}{item[1]:>5}')
            print()

        if s.peripherals:
            print("Peripherals:")
            for item in s.peripherals:
                print(f'{item[0]:<15}{item[1]:>5}')
            print()

        if s.games:
            print("Games:")
            for item in s.games:
                print(f'{item[0]:<15}{item[1]:>5}')
            print()