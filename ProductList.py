from tkinter import *
import tkinter.font as tkFont

class ProductList:
    #available products
    computers = [
        ["Dell XPS 15", 1000],
        ["MacBook Pro", 2000],
        ["Lenovo ThinkPad X1 Carbon", 1500],
        ["HP Spectre x360", 1200],
        ["Asus ROG Zephyrus G14", 1300],
        ["Microsoft Surface Pro 7", 800],
        ["Acer Swift 3", 700],
        ["Razer Blade 15", 1500]
    ]

    peripherals = [
        ["Logitech G Pro Mechanical Keyboard", 100],
        ["Razer DeathAdder Elite Gaming Mouse", 50],
        ["Dell Ultrasharp U2718Q Monitor", 300],
        ["Bose QuietComfort 35 II Headphones", 200],
        ["Harman Kardon SoundSticks III Speakers", 100],
        ["Logitech MX Master 3 Mouse", 100],
        ["Apple Magic Keyboard", 100],
        ["Apple Magic Mouse 2", 100],
        ["HP 24mh FHD Monitor", 200],
        ["Logitech C920x Pro HD Webcam", 100]
    ]

    games = [
        ["The Legend of Zelda: Tears of the Kingdom", 60],
        ["Spiderman: Miles Morales", 60],
        ["Cyberpunk 2077", 60],
        ["The Witcher 3: Wild Hunt", 60],
        ["Red Dead Redemption 2", 60],
        ["Minecraft", 30]
    ]

    categories = {
        'Computers': computers,
        'Peripherals': peripherals,
        'Games': games
    }

    compSize = len(computers)
    periSize = len(peripherals)
    gameSize = len(games)

    catSize = compSize+periSize+gameSize

    ''' BACKEND FUNCS'''

    #function to return one dictionary entry
    def get_item(s, choice):
        [category, index] = s.numToCategory(choice)

        if (category == 'computers'):
            return s.computers[index]
        elif (category == 'peripherals'):
            return s.peripherals[index]
        elif (category == 'games'):
            return s.games[index]
        
    def display_products(s):
        prodCount = 1

        print("Computers:")
        for item in s.computers:
            print(f'{str(prodCount)+")":<4} {item[0]:<50}${item[1]:>10.2f}')
            prodCount+=1
        print()

        print("Peripherals:")
        for item in s.peripherals:
            print(f'{str(prodCount)+")":<4} {item[0]:<50}${item[1]:>10.2f}')
            prodCount+=1
        print()

        print("Games:")
        for item in s.games:
            print(f'{str(prodCount)+")":<4} {item[0]:<50}${item[1]:>10.2f}')
            prodCount+=1
        print()

    def numToCategory(s, num):
        num-=1
        cat1 = s.compSize
        cat2 = s.periSize
        cat3 = s.gameSize
        if num < cat1:
            return ['computers', num]
        elif num < cat1+cat2:
            return ['peripherals', num-cat1]
        elif num < cat1+cat2+cat3:
            return ['games', num-cat2-cat1]
        
    ''' UI FUNCS '''

    def showIncrementItem(item, prod_idx, quant, quant_idx):
        idx = prod_idx.index(item)
        #print(f'{idx} found')
        if item.get():
            quant[idx].configure(state='normal')
        else:
            quant[idx].configure(state='disabled')
            quant_idx[idx].set(0)

    #create catalog widgets
    def buildCatalog(s, frame, products, col):
        prod_buttons = []
        prod_vars = []

        quant_entries = []
        quant_vars = []

        r=0
        for i in products:
            prod_vars.append(IntVar())
            prod_buttons.append(Checkbutton(
                frame,
                text=f'{i[0]:<30}${i[1]:>10.2f}',
                font=tkFont.Font(family='Space Mono', size=10),
                variable=prod_vars[r],
                onvalue=1,
                offvalue=0,
                state='normal',
            ))

            quant_vars.append(IntVar())
            quant_entries.append(Entry(
                frame,
                textvariable=quant_vars[r],
                font=tkFont.Font(family='Space Mono', size=10),
                state='disabled',
                width=3
            ))

            quant_entries[r].grid(row=r, column=col+1, sticky='w')
            prod_buttons[r].grid(row=r, column=col, sticky='w')
            prod_buttons[r].configure(command=lambda item=prod_vars[r]: s.showIncrementItem(item, prod_vars, quant_entries, quant_vars))
            r+=1

        return {
            'Prod Buttons': prod_buttons,
            'Prod Vars': prod_vars,
            'Quant Entries': quant_entries,
            'Quant vars': quant_vars
            }
