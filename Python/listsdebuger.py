simple_list = [3, 5, 4, 3, 2, 8, 6, 4, 4, 6, 4, 4, 6, 5, 6, 7, 6, 5, 4, 3]
secret_list = []

for i in simple_list[:]:
    if i not in secret_list:
        secret_list.append(i)
        
simple_list = secret_list
print(simple_list)
