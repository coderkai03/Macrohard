from Person import Person

class Profile(Person):
    #member variables
    discount_opts = {
        'VETERAN': -.1,
        'SENIOR': -.05,
        'STUDENT': -.08,
        'NONE': 0
    }

    user_discount = []
    cart = []

    #constructor
    def __init__(s, info, disc):
        super().__init__(info)
        disckey = list(s.discount_opts.keys())[disc-1]
        discval = s.discount_opts[disckey]
        s.user_discount.append(disckey)
        s.user_discount.append(discval)

    #methods
    def __str__(s):
        return f'''
        Name: {s.user_data['name']}
        Phone: {s.user_data['phone']}
        Email: {s.user_data['email']}
        ZIP: {s.user_data['ZIP']}
        Address: {s.user_data['address']}
        '''

    def addItem(s, item):
        s.cart.append(item)

    def removeItem(s, index):
        s.cart.pop(index)

    def display_cart(s):
        prodCount = 1

        for item in s.cart:
            print(f'{str(prodCount)+")":<4}{item[0]:<50}${item[1]:>10.2f}')
            prodCount+=1
