digit = input('What number do you want to convert? ')
system = int(input('What is its system? '))

def number_conversion(digit, system):
    converted_digit = 0
    reversed_index_of_number = len(digit) - 1

    for number in digit:
        element = int(number) * system ** reversed_index_of_number
        converted_digit += element
        reversed_index_of_number -= 1
    return converted_digit

print(number_conversion(digit, system))
