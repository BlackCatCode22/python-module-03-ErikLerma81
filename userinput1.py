array = []

while True:

    numbersInput = input("Enter a number or 'done' if finished: ")

    if numbersInput == 'done':
        break

    try:
        number = float(numbersInput)
        array.append(number)

    except ValueError:
        print("Invalid input: Please enter valid number")

count = len(array)
total = sum(array)
average = total / count

print("Count:" + str(count))
print("Total:" + str(total))
print("Average:" + str(average))