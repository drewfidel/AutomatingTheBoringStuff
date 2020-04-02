foods = [1,2,3]

snacks = foods
snacks[0] = 0

# print(foods)

# both prints [0,2,3]
# the list is created in memory and both list vars reference that memory location

def eggs(cheese):
    cheese.append(4)

spam = [1,2,3]
eggs(spam)
print(spam)

# prints [1, 2, 3, 4]

# Variables dont contain lists, they contain referemces to lists