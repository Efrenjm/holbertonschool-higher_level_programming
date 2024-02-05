# Define variables a and b
a = 10
b = 5

# Import functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# Call each of the imported functions with arguments a and b
result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

# Print the results
print("Result of adding {} and {} is: {}".format(a, b, result_add))
print("Result of subtracting {} from {} is: {}".format(b, a, result_subtract))
print("Result of multiplying {} and {} is: {}".format(a, b, result_multiply))
print("Result of dividing {} by {} is: {}".format(a, b, result_divide))
