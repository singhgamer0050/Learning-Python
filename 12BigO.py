# Eg: 1
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers
    
numbers = [2,5,8,9]
print(get_squared_numbers(numbers))

#Eg: 2
numbers = [3,6,2,4,3,6,8,9]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i],"is a duplicate")
            break

#Eg: 3
numbers = [3,6,2,4,3,6,8,9]
duplicate = None
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break

for i in range(len(numbers)):
    if numbers[i] == duplicate:
        print(i)

#Eg: 4
numbers = [4,9,15,21,34,57,68,91]
for i in range(len(numbers)):
    if numbers[i] == 68:
        print(i)