# Find the Sum of squares of first n natural numbers, given n as input. The task is to find 1 2 +2 2
# + …N


def sumsqr(n):
    return (n * (n + 1) / 2) * (2 * n + 1) / 3


num = eval(input("please enter the value of N in finding the sum of the series: "))
print(f"The sum is {sumsqr(num)}")
