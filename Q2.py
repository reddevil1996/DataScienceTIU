# Find the largest element in a list of integers supplied.


lst = []
n = eval(input("Enter the number of element in a list: "))
print("Enter the elements of the list: ")
for i in range(n):
    num = eval(input())
    lst.append(num)
print(f"The list is: {lst}")
s = lst.sort()
print(f"The largest element of the list is: {lst[-1]}")
