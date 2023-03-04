#!usr/bin/env python3

"""
The following program opens a file and reads its contents line by line
as text strings
"""

if __name__ == "__main__":

    with open("data.txt") as file:
        for line in file:
            print(line, end="")
