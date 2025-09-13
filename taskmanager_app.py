class Task:
    def __init__(self, task_id, name):
        self.task_id = task_id
        self.name = name
        self.status = "Pending"

    def execute(self):
        self.status = "Completed"

    def display(self):
        print(f"Task ID: {self.task_id} | Name: {self.name} | Status: {self.status}")


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    # Input Task
    def input_task(self, name):
        task = Task(self.next_id, name)
        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully!")

    # Execute Task
    def execute_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.execute()
                print(f"Task {task_id} executed successfully!")
                return
        print("Task not found!")

    # Remove Task
    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} removed successfully!")
                return
        print("Task not found!")

    # Display Tasks
    def display_tasks(self):
        if not self.tasks:
            print("No tasks available!")
            return
        for task in self.tasks:
            task.display()


# Main Program
def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Input Task")
        print("2. Execute Task")
        print("3. Remove Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            manager.input_task(name)

        elif choice == "2":
            try:
                task_id = int(input("Enter task ID to execute: "))
                manager.execute_task(task_id)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to remove: "))
                manager.remove_task(task_id)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "4":
            manager.display_tasks()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()