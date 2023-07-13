class View:
    #print a list of products
    def print_products(products):
        for i in range(len(products)):
            print(f'{i + 1}. {products[i]}')

    def print_bill(s, cart, bill):
        print('--- Checkout --------------------------')
        for l1 in cart:
            print(l1, end='')

        print('\n')

        for l2 in bill:
            print(l2, end='')

    def export_bill(s, cart, bill):
        filename = 'Macrohard-Bill.txt'
        f = open(filename, 'w')
        f.write('--- Checkout --------------------------\n')
        for l1 in cart:
            f.write(l1)

        f.write('\n\n')

        for l2 in bill:
            f.write(l2)