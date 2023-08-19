existential = []

existential.append("Money")
existential.append("Health")
existential.append("Tech")

print(existential)

for i in range(2):
    existential.append(input("Add some additional features:"))
    
print(existential)

del existential[-1]
del existential[-1]

print(existential)

existential.insert(0, "Fame")

print(existential)
