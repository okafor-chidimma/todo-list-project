class UserInterface:
    @staticmethod
    def display_menu():
        print("menu")
        print("1. add task")
        print("2. View all tasks")
        print("3. delete task")
        print("4 exit")

    @staticmethod
    def get_task_input():
        task=input("enter the task: ")
        return task
    
    @staticmethod
    def get_task_num_input():
        task_num = int(input("Enter the task number: "))
        return task_num
    
    @staticmethod
    def display_mess(message):
        print(message)


ui = UserInterface()
