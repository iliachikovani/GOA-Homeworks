names = ["ilia","davit","gio" ,"aleqsandre", "luka", "avsa" ,"vato" ,"ana" ,"nino", "mari"]
names.remove("aleqsandre")
print(names)


# ...............................................................................
hello = []

for i in range(101):
    hello.append(i)
print(hello)


# ...............................................................................

hello = []
number = int(input())


for i in range(0,number + 1):
    hello.append(i)
print(hello)



# ...............................................................................
foods = ["ხაჭაპური", "ხინკალი", "ლობიანი", "მცხეთა", "ჩურჩხელა"]

cars = ["Toyota", "Mercedes", "BMW", "Audi", "Honda"]

combined_list = foods + cars

print("გაერთიანებული სია:", combined_list)
# ...............................................................................

items = ["ვაშლი", "ბანანი", "ატამი", "კიტრი", "ყურძენი", "სტაფილო", "ფორთოხალი", "პომიდორი", "მსხალი", "კარტოფილი"]

filtered_items = []

for item in items:
    if item in ["ვაშლი", "ბანანი", "ატამი", "ყურძენი", "ფორთოხალი", "მსხალი"]:
        filtered_items.append(item)

print(filtered_items)

# ...............................................................................
import random

numbers = random.sample(range(1, 101), 20)
print("სია 20 განსხვავებული რიცხვით:", numbers)


even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("ლუწი რიცხვები:", even_numbers)
print("კენტი რიცხვები:", odd_numbers)