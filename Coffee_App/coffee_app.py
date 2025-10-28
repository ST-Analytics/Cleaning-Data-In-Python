

class CoffeeApp:

## Initialize the CoffeeApp with a list of coffee options
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size
         

class Order:
## Initialize the Order with an empty list of items
    def __init__(self):
        self.items = []

## Add coffee item to the order
    def add_item(self, coffee):
        self.items.append(coffee)

        print(f"Added {coffee.size}{coffee.name} to your order for ${coffee.price:.2f}")

## Calculate the total price of the order

    def total_price(self):
        return sum(item.price for item in self.items)
    
    def display_order(self):
        if not self.items:
            print("Your order is empty.")
            return
        
        print("Your order contains:")
        for item in self.items:
            print(f"- {item.size}{item.name}: ${item.price:.2f}")

## handle checkout process

    def checkout(self):
        total = self.total_price()
        print(f"Your total is: ${total:.2f}")
        print("Thank you for your order!")


## Define coffee options

coffee_menu = [
    CoffeeApp("Espresso", 2.50, "Small "),
    CoffeeApp("Latte", 3.50, "Medium "),
    CoffeeApp("Cappuccino", 4.00, "Large "),
    CoffeeApp("Mocha", 4.50, "Medium "),
    CoffeeApp("Americano", 2.75, "Small ")
]

## Simulate user interaction
def main():
    order = Order()
    
    print("Welcome to the Coffee Shop!")
    print("Here is our menu:")
    for idx, coffee in enumerate(coffee_menu, start=1):
        print(f"{idx}. {coffee.size}{coffee.name} - ${coffee.price:.2f}")
    
    while True:
        choice = input("Enter the number of the coffee you want to add to your order (or 'q' to checkout): ")
        if choice.lower() == 'q':
            break
        try:
            coffee_index = int(choice) - 1
            if 0 <= coffee_index < len(coffee_menu):
                order.add_item(coffee_menu[coffee_index])
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    order.display_order()
    order.checkout()

if __name__ == "__main__":
    main()
    pass
