class InventoryManager:
    def __init__(self):
        # Start with an empty inventory
        self.inventory = []

    def add_item(self, item_name, quantity, price):
        # Create a new item as a dictionary for better readability
        new_item = {
            'name': item_name,
            'quantity': quantity,
            'price': price
        }

        # Check if the item already exists in the inventory
        for item in self.inventory:
            if item['name'] == item_name:
                # If it exists, update the quantity
                item['quantity'] += quantity
                print(f"Updated {item_name} quantity to {item['quantity']}.")
                return

        # If the item does not exist, add it to the inventory
        self.inventory.append(new_item)
        print(f"Added new item: {item_name} (Quantity: {quantity}, Price: {price})")

    def remove_item(self, item_name, quantity):
        # Look for the item in the inventory
        for item in self.inventory:
            if item['name'] == item_name:
                if item['quantity'] < quantity:
                    print(f"Cannot remove {quantity} of {item_name}. Only {item['quantity']} available.")
                    return
                elif item['quantity'] == quantity:
                    # Remove the item if the quantity is zero
                    self.inventory.remove(item)
                    print(f"Removed all {item_name} from inventory.")
                    return
                else:
                    # Decrease the quantity
                    item['quantity'] -= quantity
                    print(f"Reduced {item_name} quantity to {item['quantity']}.")
                    return

        print(f"Item {item_name} not found in inventory.")

    def calculate_total_value(self):
        # Calculate the total value of the inventory
        total_value = sum(item['quantity'] * item['price'] for item in self.inventory)
        return total_value

    def display_inventory(self):
        # Sort inventory by item name and display it
        self.inventory.sort(key=lambda x: x['name'])  # Sort by item name
        print("\nCurrent Inventory:")
        print("--------------------")
        for item in self.inventory:
            print(f"Item: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']:.2f}")
        print("--------------------")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Adding items to the inventory
    manager.add_item("Apple", 50, 0.5)
    manager.add_item("Banana", 30, 0.3)
    manager.add_item("Orange", 40, 0.7)

    # Display the inventory
    manager.display_inventory()

    # Calculating total value
    print(f"\nTotal inventory value: ${manager.calculate_total_value():.2f}")

    # Removing items
    manager.remove_item("Apple", 20)
    manager.remove_item("Banana", 15)

    # Display the updated inventory
    manager.display_inventory()

    # Total value after removal
    print(f"\nTotal inventory value after removal: ${manager.calculate_total_value():.2f}")