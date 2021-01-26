# Create a dictionary of 5 elements with key as integers. Print it and then print the key and
# values in sorted order.


n = eval(input("Enter the size of the dictionary: "))
dic = {}
for i in range(n):
    key = eval(input("Enter the key: "))
    value = eval(input(f"Enter the {key} th integer: "))
    dic[key] = value

print(f"The dictionary is: {dic}")
print(f"Print the key in sorted way: {sorted(dic.keys())}")
print(sorted(dic.items()))
print(f"Print the values in sorted way: {sorted(dic.values())}")
