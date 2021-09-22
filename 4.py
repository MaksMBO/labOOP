def knapsack(roominess, bag, number):
    if number == 0 or roominess == 0:
        return False
    if (bag[number - 1] > roominess):
        return knapsack(roominess, bag, number - 1)
    else:
        return max(bag[number - 1] + knapsack(roominess - bag[number - 1], bag, number - 1),
        knapsack(roominess, bag, number - 1))


bag = []
try:
    roominess = int(input("Roominess: "))
    number = int(input("Number: "))

    for i in range(0, number):
        ingot = int(input("Ingot: "))
        bag.append(ingot)

    if knapsack(roominess, bag, number):
        print(knapsack(roominess, bag, number))
    else:
        print("Something went wrong")
except ValueError:
    print("You did not enter incorrect data!")

