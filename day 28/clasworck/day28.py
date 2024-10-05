numbers = list(range(1, 11))

even_numbers = [numbers[i] for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(even_numbers)

# ..................................................

items = [
    "Toyota", "Honda", "BMW", "Mercedes", "Audi", 
    "Harley-Davidson", "Ducati", "Yamaha", "Kawasaki", "Suzuki",
    "Pizza", "Burger", "Sushi", "Pasta", "Salad",
    "Ford", "Chevrolet", "Tesla", "Nissan", "Mazda"
]

for item in items:
    print(item)
# ..................................................

numbers = list(range(1, 21))

for number in numbers:
    if number % 2 == 0:
        print(number)

