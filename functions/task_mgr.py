class TaskManager:
    def __init__(self, filename):
        self.filename = filename

    def open_file(self, mode):
        return open(self.filename, mode) 

    def add_task(self,task):
        f = self.open_file("a")
        f.write(task + "\n")
        f.close()

    
    def get_all_tasks(self):
        f = self.open_file("r")
        filecontents= f.read()
        tasks = filecontents.splitlines()
        f.close()
        return tasks
    
    def delete_task(self, task_number):
        tasks = self.get_all_tasks()
        if 0<=task_number<len(tasks):
            del_task = tasks.pop(task_number)
            f = self.open_file("w")
            for task in tasks:
                f.write(task + "\n")
            f.close()
            return del_task
        else:
            print("Invalid Task Number")

       