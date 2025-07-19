import json
import os

DB_FILE = "tasks.json"
 
def load_tasks():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f :
            return json.load(f)
    return []
def save_tasks(tasks):
    with open(DB_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
def display_menu():
    print("\n=== To-Do List App ===")
    print("1. Add Task")        
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
def add_task(tasks):
    desc = input("Enter the task description: ").strip()
    if desc:
        tasks.append({"desc": desc, "done": False})
        save_tasks(tasks)
        print("Task added!")
    else:
        print("Task empty not possible.")
def view_tasks(tasks):    
    if not tasks:
        print(" no task ")  
        return 
    for i, task in enumerate(tasks, 1):
        status = "[✓]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['desc']}")
def mark_task_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted: {removed['desc']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print(" Bye!!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
