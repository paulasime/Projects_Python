class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")


todo_list = TodoList()

while True:
    print("\n1. Add task")
    print("2. Delete task")
    print("3. Display tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.add_task(task)
    elif choice == '2':
        task = input("Enter task to delete: ")
        todo_list.delete_task(task)
    elif choice == '3':
        todo_list.display_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the to do list application!")
