#!/usr/bin/python3
str = "Holberton School"
for i in range(3):
    print(str, end = ("\n" if i == 2 else ""))

print(str[:9])