number = int(input("Enter a number to see its multiplication table: "))
for index, num in enumerate(range(number, number*11, number)):
    print(f"{number} * {index +1} = {num}")