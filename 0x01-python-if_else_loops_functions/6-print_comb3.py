#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            print("{}, ".format(str(i) + str(j)), end="")
print("\n")
