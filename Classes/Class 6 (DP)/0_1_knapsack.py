class Product:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.value_per_weight = value / weight
    
    def __str__(self):
        return f"{self.name}"

def knapsack01(capacity, current_product, products):
    if capacity == 0 or current_product >= len(products):
        return 0
    elif products[current_product].weight > capacity:
        return knapsack01(capacity, current_product + 1, products)
    else:
        take = products[current_product].value + knapsack01(capacity - products[current_product].weight, current_product + 1, products)
        ignore = knapsack01(capacity, current_product + 1, products)
        return max(take, ignore)


products = [
    Product("P1", 1, 1),
    Product("P2", 3, 4),
    Product("P3", 4, 5),
    Product("P4", 5, 7)
    ]
capacity = 7
print(knapsack01(capacity, 0, products))