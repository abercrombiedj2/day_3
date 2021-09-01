# words = "Hey"

# def greet(name, time_of_day):
#     return words + ", " "good " + time_of_day + " " + name

# name_1 = "Bob"
# time_of_day_1 = "morning"

# print(greet(name_1, time_of_day_1))

# def greet_2():
#     return words

# print(greet_2())

# def count_eggs(list):

#     total_eggs = 0

#     for chicken in list:
#         total_eggs += chicken["eggs"]
#         chicken["eggs"] = 0

#     return f"{total_eggs} eggs collected"

# print(count_eggs(chickens))

# def add_numbers(number_1, number_2):
#     return number_1 + number_2

# def multiply_numbers(number_1, number_2):
#     return number_1 * number_2

# num_1 = 10

# print(multiply_numbers(num_1, add_numbers(2, 5)))

chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]

def find_chicken_by_name(list, name):
    for chicken in list:
        if chicken["name"] == name:
            return chicken
    return "Not found"

print(find_chicken_by_name(chickens, "Margaret"))
print(find_chicken_by_name(chickens, "Audrey"))
