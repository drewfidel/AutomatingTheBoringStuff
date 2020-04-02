def div(divideBy):
    try:
        return 42 / divideBy

    except ZeroDivisionError:
        print("You entered a zero number")

# print(div(42)

print("How many pairs of shoes do you have")
num = input()

try:
    if int(num) > 0:
        print("You have a good amount of shoes!")
    else:
        print("You need more shoes than that buddy")

except ValueError:
    print("Please enter a number ")

