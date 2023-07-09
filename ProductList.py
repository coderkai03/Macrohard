class Product:
    computers = {
        "Dell XPS 15": 1000,
        "MacBook Pro": 2000,
        "Lenovo ThinkPad X1 Carbon": 1500,
        "HP Spectre x360": 1200,
        "Asus ROG Zephyrus G14": 1300,
        "Microsoft Surface Pro 7": 800,
        "Acer Swift 3": 700,
        "Razer Blade 15": 1500
    }

    peripherals = {
        "Logitech G Pro Mechanical Keyboard": 100,
        "Razer DeathAdder Elite Gaming Mouse": 50,
        "Dell Ultrasharp U2718Q Monitor": 300,
        "Bose QuietComfort 35 II Headphones": 200,
        "Harman Kardon SoundSticks III Speakers": 100,
        "Logitech MX Master 3 Mouse": 100,
        "Apple Magic Keyboard": 100,
        "Apple Magic Mouse 2": 100,
        "HP 24mh FHD Monitor": 200,
        "Logitech C920x Pro HD Webcam": 100
    }

    games = {
        "The Legend of Zelda: Tears of the Kingdom": 60,
        "Spiderman: Miles Morales": 60,
        "Cyberpunk 2077": 60,
        "The Witcher 3: Wild Hunt": 60,
        "Red Dead Redemption 2": 60,
        "Minecraft": 30
    }

    #revise dictionary to be a list with dictionaries

    #function to return one dictionary entry
    def get_computer(s, index):
        return [list(s.computers)[index], list(s.computers.values())[index]]