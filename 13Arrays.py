#Que 1
exp = [2200, 2350, 2600, 2130, 2190]
print("Expences in FEb month is: ", exp[1])
print("Extra spent in February:", exp[1] - exp[0])

print("Total expence in forst quater is:", exp[0]+exp[1]+exp[2])

print("Expended 2000 in any month", 2000 in exp)

exp.append(1980)

exp[3] = exp[3] - 200

print(exp)

#Que 2

heros = ["spider man", "thor", "hulk", "iron man", "captain america"]
print("Length of list is:", len(heros))

heros.append("black panther")

heros.remove("black panther")
heros.insert (3, "black panther")

heros[1 : 3] = ["doctor strange"]
heros.sort()
print(dir(heros))

#Que 3
max_no = int(input("Enter the number till you want odd number"))
odd_no =[]
for i in range (1, max_no+1):
    if i % 2 != 0:
        odd_no.append(i)

print(odd_no)