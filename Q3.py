# Create an array of long integers supplied. Pop the last element and print. Reverse the array
# and print.


arr = []
n = eval(input("Enter the size of the array: "))
print("Enter the elements of the array(Long Type Element)")
for i in range(n):
    num = eval(input())
    arr.append(num)
print(f"The array is: {arr}")
arr.pop(-1)
print(f"After popping the last element of the array, now the array is: {arr}")
arr.reverse()
print(f"After reversing the array is: {arr}")
