#!/usr/bin/python3
a = 10
b = 5

# Import functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Call each of the imported functions with arguments a and b
result_add = add(a, b)
result_subtract = sub(a, b)
result_multiply = mul(a, b)
result_divide = div(a, b)

# Print the results
print("{} + {} = {}".format(a, b, result_add))
print("{} - {} = {}".format(a, b, result_subtract))
print("{} * {} = {}".format(a, b, result_multiply))
print("{} / {} = {}".format(a, b, result_divide))
