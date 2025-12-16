from functools import cmp_to_key

class Product:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.value_per_weight = value / weight
    
    def __str__(self):
        return f"{self.name}"

def our_comparator(a, b):
    if a.value_per_weight > b.value_per_weight:
        return -1
    elif a.value_per_weight < b.value_per_weight:
        return 1
    else:
        return 0

products = [
    Product("P1", 2, 10),
    Product("P2", 5, 15),
    Product("P3", 9, 30),
    Product("P4", 6, 20),
    Product("P5", 4, 18)
    ]

products.sort(key=cmp_to_key(our_comparator))


taken_products = []
capacity = 10
total_value = 0

for product in products:
    if product.weight <= capacity:
        taken_products.append([product, "FULL"])
        total_value = total_value + product.value
        capacity = capacity - product.weight
    else:
        taken_products.append([product, "Fraction"])
        total_value = total_value + (capacity * product.value_per_weight)
        capacity = 0
        break


print(f"Total Value: {total_value:0.2f}")
for product in taken_products:
    print(product[0], product[1])
        
        
        

        