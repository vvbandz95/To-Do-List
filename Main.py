# Define user_tasks as a global list so it can be accessed in functions

user_tasks = []

def menu():
    print("\nTo-Do List Application")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Quit the App")

def add_task():
    task = input("Enter a task: ")
    user_tasks.append(task)
    print(f"'{task}' has been added to the list.")

def view_tasks():
    if len(user_tasks) == 0:
        print("The to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(user_tasks, start=1):
            print(f"{index}. {task}")


def delete_task():
    try:
        task_num = int(input("Enter the task number you want to delete: "))
        if task_num < 1 or task_num > len(user_tasks):
            print("Task number is invalid!")
        else:
            removed_task = user_tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully!")
    except ValueError:
        print("This number is invalid, please try again!")
 

def main():
    while True:
        menu()
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Option is not valid, please try again.")
        except ValueError:
            print("Invalid input! Enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
