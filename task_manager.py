# Name: Tosin Bello
# Course: COMP120
# Assignment 3 - Managing a Software Project with GitHub
# Description: A simple to-do list. The user can add a task, view all
#              tasks, or quit from a menu.


def add_task(tasks):
    """Ask the user for a task and add it to the list."""
    task_name = input("Enter a task: ").strip()
    if task_name == "":
        print("A task cannot be empty.")
    else:
        tasks.append(task_name)
        print("Task added:", task_name)


def view_tasks(tasks):
    """Print every task with a number, or a message if there are none."""
    if len(tasks) == 0:
        print("You have no tasks yet.")
    else:
        print("--- Your Tasks ---")
        task_number = 1
        for task in tasks:
            print(str(task_number) + ".", task)
            task_number += 1
        print("Total tasks:", len(tasks))


def show_menu():
    """Print the menu options."""
    print()
    print("--- Task Manager ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Quit")


# --- Main program ---
tasks = []
choice = ""

while choice != "3":
    show_menu()
    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
