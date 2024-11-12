import json
import os

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        task_id = self.tasks[-1].id + 1 if self.tasks else 1
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        print(f"Task '{title}' added with ID {task_id}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                status = "✓" if task.completed else "✗"
                print(f"[{status}] ID: {task.id} - {task.title}")

    def delete_task(self, task_id):
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task:
            self.tasks.remove(task)
            print(f"Task ID {task_id} deleted.")
        else:
            print(f"Task ID {task_id} not found.")

    def mark_task_complete(self, task_id):
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task:
            task.completed = True
            print(f"Task ID {task_id} marked as complete.")
        else:
            print(f"Task ID {task_id} not found.")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)
        print("Tasks saved to file.")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**data) for data in tasks_data]
                print("Tasks loaded from file.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            task_manager.add_task(title)

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                task_manager.mark_task_complete(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "5":
            task_manager.save_tasks()

        elif choice == "6":
            task_manager.save_tasks()  # Save tasks before exiting
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
