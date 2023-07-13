class Prompt:
    #validate input to be an integer between min and max
    def validate_input(s, min, max):
        while True:
            try:
                print('0 - Quit')
                num = int(input('Input: '))
                if num >= min and num <= max:
                    return num
                else:
                    #throw an error to go to the except block
                    raise ValueError
            except ValueError:
                print('Invalid input. Please try again.\n')

    #ask user for customer info and return a dictionary
    def get_customer_info(s):
        print('Enter the customer\'s information.')
        name = input('Name: ')
        email = input('Email: ')
        address = input('Address: ')
        print()

        return {
            'name': name,
            'email': email,
            'address': address
        }
    
    def get_discount(s):
        print('I am a:')
        print('1 - Veteran')
        print('2 - Senior')
        print('3 - Student')
        print('4 - None')
        print()
        return s.validate_input(1, 4)