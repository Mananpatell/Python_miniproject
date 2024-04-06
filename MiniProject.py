# Function to display menu
def display_menu():
    print("Welcome to the To-Do List App!")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save Tasks to File")
    print("6. Load Tasks from File")
    print("7. Exit")

# Function to add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} - {status}")

# Function to mark task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    index = get_task_index(len(tasks))
    if index is not None:
        tasks[index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid index.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    index = get_task_index(len(tasks))
    if index is not None:
        deleted_task = tasks.pop(index)
        print(f"Task '{deleted_task['task']}' deleted successfully!")
    else:
        print("Invalid index.")

# Function to save tasks to a file
def save_tasks_to_file(tasks):
    filename = input("Enter file name to save tasks: ")
    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task["task"] + "," + str(task["completed"]) + "\n")
        print("Tasks saved to file successfully!")
    except IOError:
        print("Error: Unable to save tasks to file.")

# Function to load tasks from a file
def load_tasks_from_file(tasks):
    filename = input("Enter file name to load tasks: ")
    try:
        with open(filename, "r") as file:
            tasks.clear()
            for line in file:
                task, completed = line.strip().split(",")
                tasks.append({"task": task, "completed": bool(int(completed))})
        print("Tasks loaded from file successfully!")
    except IOError:
        print("Error: Unable to load tasks from file.")

# Function to get valid task index from user
def get_task_index(max_index):
    while True:
        try:
            index = int(input("Enter the index of the task: ")) - 1
            if 0 <= index < max_index:
                return index
            else:
                print("Invalid index. Please enter a number between 1 and", max_index)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main function
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks_to_file(tasks)
        elif choice == "6":
            load_tasks_from_file(tasks)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
