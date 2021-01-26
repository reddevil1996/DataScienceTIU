# Take the size and list of elements of a list as input. Create a tuple with the elements and
# their cubes. Print the tuple.


lst = []
n = eval(input("Enter the number of element in a list: "))
print("Enter the elements of the list: ")
for i in range(n):
    num = eval(input())
    lst.append(num)
print(f"The list is: {lst}")
print(f"Tuple is : {tuple(lst)}")
print(f"For Cubic element tuple is: {tuple(i ** 3 for i in lst)}")
