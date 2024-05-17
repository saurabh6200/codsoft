# This is a command line based appllication .
# here we can add ,update,dispaly and track our to-do list.


# /// Define the task class 
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.description}"
# //// To-do list classes
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def update_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description
        else:
            print("Task not found.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Task not found.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Task not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")
#//// command line interface
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. Complete Task")
        print("5. Display Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Enter task number to update: ")) - 1
            new_description = input("Enter new task description: ")
            todo_list.update_task(index, new_description)
        elif choice == "3":
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "4":
            index = int(input("Enter task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == "5":
            todo_list.display_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
