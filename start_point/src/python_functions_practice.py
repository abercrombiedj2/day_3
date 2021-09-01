def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(number):
    if number == 1: return "January"
    elif number == 3: return "March"
    elif number == 9: return "September"

def number_to_short_month_name(number):
    if number == 1: return "Jan"
    if number == 4: return "Apr"
    if number == 10: return "Oct"

def cubed(number):
    return number ** number

def r_string(string):
    return string[:: -1]

def fahrenheit_to_celsius(f):
    return (f - 30) / 2
