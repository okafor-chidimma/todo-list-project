from functions.task_mgr import TaskManager
from functions.ui import ui

def main():
    task_mgr = TaskManager("data_storage/tasks.txt")

    while True:
        ui.display_menu
        choice = input("Enter your choice: ")

        if choice == "1":
            task = ui.get_task_input()
            task_mgr.add_task(task)
            ui.display_mess("Task added")

        elif choice == "2":
            tasks = task_mgr.get_all_tasks()
            ui.display_mess("Tasks:")
            for i, task in enumerate(tasks, start=1):
                ui.display_mess(f"{i}. {task}")

        elif choice == "3":
            task_number = ui.get_task_number_input()
            deleted_task = task_mgr.delete_task(task_number)
            if deleted_task is not None:
                ui.display_mess(f"Deleted task: {deleted_task}")
            else:
                ui.display_mess("Invalid task number!")

        elif choice == "4":
            ui.display_mess("Exiting...")
            break

        else:
            ui.display_mess("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()