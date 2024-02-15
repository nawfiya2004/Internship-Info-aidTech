import json
class Task:
    def __init__(self, title, description, status="Pending"):
        self.title = title
        self.description = description
        self.status = status
class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False
    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.title} - {task.description} [{task.status}]")
    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)
    def load_tasks(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.tasks = [Task(task['title'], task['description'], task['status']) for task in data]
def main():
    todo_list = ToDoList()
    filename = "tasks.json"  # You can change the filename as needed
    try:
        todo_list.load_tasks(filename)
        print("Previous tasks loaded successfully!")
    except FileNotFoundError:
        print("No previous tasks found.")
    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(Task(title, description))
        elif choice == '2':
            title = input("Enter the title of the task to delete: ")
            if todo_list.delete_task(title):
                print("Task deleted successfully!")
            else:
                print("Task not found!")
        elif choice == '3':
            print("\nYour Tasks:")
            todo_list.view_tasks()
        elif choice == '4':
            todo_list.save_tasks(filename)
            print("Tasks saved successfully!")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
if __name__ == "__main__":
    main()
