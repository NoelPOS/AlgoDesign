class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    for item in items:
        if capacity > 0 and item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.value * (capacity / item.weight)
            break
    return total_value

items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
print(f"Total value: {fractional_knapsack(items, capacity)}")
