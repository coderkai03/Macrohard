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