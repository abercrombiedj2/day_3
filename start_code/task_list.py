tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1. Print a list of uncompleted tasks.
def uncompleted(list):
    for task in list:
        if task["completed"] == False:
            print(task)

uncompleted(tasks)

# 2. Print a list of completed tasks.
def completed(list):
    for task in list:
        if task["completed"] == True:
            print(task)

completed(tasks)

# 3. Print a list of task descriptions.
def description(list):
    for task in list:
        print(task["description"])

description(tasks)

# 4. Print a list of tasks where time_taken is at least a given time.
def takes_at_least(time, list):
    for task in list:
        if task["time_taken"] >= int(time):
            print(f"{task['description']} takes at least {time} minuites.")

takes_at_least(15, tasks)

# 5. Print any task with a given description.
def task_description(description, list):
    for task in list:
        if task["description"] == description:
            print(task)
            return
    print("Task not in the list.")

task_description("Walk Dog", tasks)

# 6. Given a description update that task to mark it as complete.
def update(description, list):
    for task in list:
        if description == task["description"]:
            task["completed"] = True

update("Wash Dishes", tasks)

# 7. Add a task to the list.
def add_task(task, list):
    list.append(task)

add_task({
    "description": "Do laundry",
    "completed": False,
    "time_taken": 90
}, tasks)

# 8. Use a while loop to display the menu and allow the user to enter an option.
def print_menu():
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

# 9. Call the appropriate function depending on the users choice.
print_menu()
running = True
while running:
    option = input("Please enter an option from the menu above: ")
    if option == "1":
         print(tasks)
    elif option == "2":
        uncompleted(tasks)
    elif option == "3":
        completed(tasks)
    elif option == "4":
        update(input("Which task? "), tasks)
    elif option == "5":
        takes_at_least(input("How long? "), tasks)
    elif option == "6":
        task_description(input("Enter description: "), tasks)
    elif option == "7":
        add_task(input("Enter task: "), tasks)
    elif option == "M" or "m":
        print_menu()
    elif option == "Q" or "q":
        break