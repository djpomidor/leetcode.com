def int_to_list_method_1(number):
    return [int(digit) for digit in str(number)]

# Example usage
number = 12345
result = int_to_list_method_1(number)
print(result)