import csv
import random

food_items = [ # change data values as per your need
    "Apple", "Banana", "Orange", "Grapes", "Strawberry",
    "Blueberry", "Watermelon", "Pineapple", "Mango", "Peach",
    "Pear", "Cherry", "Plum", "Kiwi", "Lemon",
    "Lime", "Raspberry", "Cantaloupe", "Blackberry", "Apricot",
    "Coconut", "Fig", "Pomegranate", "Guava", "Papaya",
    "Cranberry", "Lychee", "Passion Fruit", "Dragon Fruit", "Avocado"
]

def generate_food_basket(rows, columns):
    basket = [
        [random.choice(food_items) for _ in range(random.randint(columns/2, columns))] # range(columns)
        for _ in range(rows)
    ]

    return basket

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

def main():
    try:
        num_rows = int(input("Number of rows: "))
        num_columns = int(input("Number of columns: "))
        
        basket_data = generate_food_basket(num_rows, num_columns)
        
        filename = input("Enter the filename(CSV): ")

        write_to_csv(basket_data, filename)
        print(f"CSV file '{filename}' generated.")
    
    except ValueError:
        print("Please enter valid numeric values")

if __name__ == "__main__":
    main()
