#!/usr/bin/env python3

"""
This following program uses variables and expression to perform a 
compound-interest calculation
"""


if __name__ == "__main__":
    principal = 1000    # Initial amount
    rate = 0.05         # Interest rate
    num_years = 5       # Number of years
    year = 1
    while year <= num_years:
        principal = principal * (1 + rate)
        print(year, principal)
        year += 1
