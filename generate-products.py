import random
import csv

class Item:
    def __init__(self, category, name, price, rating):
        self.category = category
        self.name = name
        self.price = price
        self.rating = rating

# List of categories and their items
categories = {
    "Computers": ["Dell XPS 15", "MacBook Pro", "Lenovo ThinkPad X1 Carbon", "HP Spectre x360", "Asus ROG Zephyrus G14"],
    "Peripherals": ["Logitech G Pro Mechanical Keyboard", "Razer DeathAdder Elite Gaming Mouse", "Dell Ultrasharp U2718Q Monitor", "Bose QuietComfort 35 II Headphones", "Harman Kardon SoundSticks III Speakers"],
    "Games": ["The Witcher 3: Wild Hunt", "Red Dead Redemption 2", "God of War", "The Legend of Zelda: Breath of the Wild", "Cyberpunk 2077"]
}

# Creating a list of items
items = []

# Distribute random number of items across categories
total_items = random.randint(15, 25)
num_categories = len(categories)
items_per_category = [0] * num_categories

while total_items > 0:
    category_index = random.randint(0, num_categories - 1)
    items_per_category[category_index] += 1
    total_items -= 1

# Generating random items
for category, items_list in categories.items():
    num_items = items_per_category.pop(0)
    num_items = min(num_items, len(items_list))
    selected_items = random.sample(items_list, num_items)
    for name in selected_items:
        price = round(random.uniform(10, 100), 2)
        rating = random.randint(1, 5)
        item = Item(category, name, price, rating)
        items.append(item)

# Writing the data to a CSV file
filename = "random_items.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Name", "Price", "Rating"])
    for item in items:
        writer.writerow([item.category, item.name, item.price, item.rating])

print(f"Random items data written to {filename}.")
