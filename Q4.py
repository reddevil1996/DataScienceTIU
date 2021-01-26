# Check if a Substring is Present in a Given String. Search should be case insensitive.


import re

str1 = input("Enter a string: ")
print(f"The string is: {str1}")
str2 = input("Enter the substring you want to find: ")
print(f"The substring is: {str2}")
str1 = str1.lower()
str2 = str2.lower()
if re.search(str2, str1):
    print(f"The Substring {str2} is present in string {str1}")
else:
    print(f"The Substring {str2} is not present in string {str1}")
