from Person import Person
from tkinter import *
import tkinter.font as tkFont

class Customer(Person):
    #member variables
    name = None
    address = None
    user_discount = None

    discount_opts = {
        'VETERAN': -.1,
        'SENIOR': -.05,
        'STUDENT': -.08,
        'NONE': 0
    }

    cart = {} #items - quant
    cart_bill={} #subtotals -> grandtotal

    #constructor
    # def __init__(s, info, disc):
    #     super().__init__(info)
    #     disckey = list(s.discount_opts.keys())[disc-1]
    #     discval = s.discount_opts[disckey]
    #     s.user_discount.append(disckey)
    #     s.user_discount.append(discval)

    ''' BACKEND FUNCS '''
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
            print(f'{str(prodCount)+")":<4}{item:<50}${s.cart[item]:>10.2f}')
            prodCount+=1

    def export_cart(s):
        prodCount = 1

        for item in s.cart:
            s.cart_bill.append(f'\n{str(prodCount)+")":<4}{item[0]:<50}${item[1]:>10.2f}')
            prodCount+=1

        return s.cart_bill
    
    ''' UI FUNCS '''

    def userInfoEntries(s, root):
        entry_vars = [StringVar() for _ in range(3)]
        entry_vars[2] = StringVar(value=0) #set radio buttons to 0

        name_label = Label(root, text='Name: ')
        name_label.grid(row=1, column=0, sticky='w')

        name_entry = Entry(root, textvariable=entry_vars[0])
        name_entry.grid(row=1, column=1)

        address_label = Label(root, text='Address: ')
        address_label.grid(row=2, column=0, sticky='w')

        address_entry = Entry(root, textvariable=entry_vars[1])
        address_entry.grid(row=2, column=1)

        demog_label = Label(root, text='Apply discount:')
        demog_label.grid(row=3, column=0, sticky='w')
        demog_radio = dict()
        demog_radio['Student'] = Radiobutton(root, text='Student', variable=entry_vars[2], value='Student')
        demog_radio['Veteran'] = Radiobutton(root, text='Veteran', variable=entry_vars[2], value='Veteran')
        demog_radio['Senior'] = Radiobutton(root, text='Senior', variable=entry_vars[2], value='Senior')
        
        r=3
        for radio in demog_radio.values():
            radio.grid(row=r, column=1)
            r+=1

        return {
            'Name': name_entry,
            'Address': address_entry,
            'Demographics': {
                'Radio': demog_radio,
                'Var': entry_vars[2]
                }
        }
    
    def saveData(s, roots, screens, save_name, save_address, save_discount):
        if roots['AccountLogin'].winfo_ismapped():
            roots['AccountLogin'].pack_forget()
        
        if not roots['StoreWindow'].winfo_ismapped():
            roots['StoreWindow'].pack(anchor='center', padx=200, pady=50)
        
        for scr in screens:
            if scr != 'Store':
                screens[scr].grid_forget()

        screens['Store'].grid(row=2, column=1)

        s.name = save_name
        s.address = save_address
        s.user_discount = s.discount_opts[save_discount.upper()]

        print('Name: ', s.name)
        print('Address: ', s.address)
        print('Discount: ', s.user_discount)

    def buildCartLbls(s, cat, frame):
        show_cat = []
        
        r=0

        for item in s.cart[cat]:
            show_cat.append(Label(
                frame,
                font=tkFont.Font(family='Space Mono', size=10),
                text=f'{item:<30}{s.cart[cat][item]:>10.0f}'
            ))

            show_cat[r].grid(row=r+1, column=0, sticky='w')
            r+=1