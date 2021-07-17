
count = 1

while count <= 5:
    print("Counting {}....".format(count))
    count = count + 1

print()


number = int(input("Enter an integer (0 to exit): "))
while number != 0:  # while number is not = 0
    print("You entered {}".format(number))
    number = int(input("Enter an integer (0 to exit): "))
