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
minimun = min(array)
maxium = max(array)

print("Count:" + str(count))
print("Total:" + str(total))
print("Min:" + str(minimun))
print("Max:" + str(maxium))