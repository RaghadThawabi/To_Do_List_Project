import json
import uuid
from itertools import count

#NEW , Rename the class
class TaskStructure:
    _id_counter = count(1)
    def __init__(self,title,description,priority,status="TO-DO",id=None):
        self.id = id or next(TaskStructure._id_counter)
        self.title=title
        self.description=description
        self.priority=priority
        self.status=status


    def as_dictionary(self):
        return {
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "priority":self.priority,
            "status":self.status,
        }


def menu():
    print("1- Add Task ")
    print("2- View Tasks status ")
    print("3- Sort Tasks ")
    print("4- Mark_As_Done ")
    print("5- Change priority ")
    print("6- Delete Task ")
    print("7- Exit the program")
    print("8- Save the list  ")



#NEW , rename the class as singular
class TaskManager:
    def __init__(self):
        self.tasks=self.load_data()


    def load_data(self):
            try:
                with open("tasks.json", "r") as file:
                    tasks_from_file = json.load(file)
                    max_id = max([t["id"] for t in tasks_from_file], default=0)
                    TaskStructure._id_counter = count(max_id + 1)
                    return [TaskStructure(**t) for t in tasks_from_file]
            except FileNotFoundError:
                return []
            except json.JSONDecodeError:
               print("File is empty ")
               return []


    def add_task(self):
        while True:
            title = input("Enter the title of the task: ")
            if title:
                break
            print("Please enter a valid title.")
        while True:
            description = input("Enter the description of the task: ")
            if description:
                break
            print("Please enter a valid description.")
        while True:
            try:
                priority = int(input("Enter priority , [highest : 0 - lowest : 5] "))
                if 0 <= priority <= 5:
                    break
            except ValueError:
                print("Please enter a valid priority [0 - 5]")
 #NEW
        task = TaskStructure(title,description,priority)
        self.tasks.append(task)
        print("Task added : "+task.title ,f"ID: {task.id}")
        print(" please save the task to not loss it ")


    def view_tasks(self):
        if len(self.tasks)==0:
            print("No tasks added yet !")

        for i in self.tasks:
            print(
                f"ID: {i.id}\n  Title: {i.title}\n  Priority: {i.priority}\n  Status: {i.status}\n"
            )
        print("End of Tasks")

    #for the searching by ID
    def find_task_by_id(self,task_id):
        for i in self.tasks:
            if i.id == task_id:
                return i
        print("Task not found ")
        return None

    # I face a problem with duplication values when save to the file ,with a previous version of code , use this approach to ensure no duplication
    def save(self):
        try:
            with open("tasks.json", "w") as file:
                json.dump([t.as_dictionary() for t in self.tasks], file, indent=4)
            print("Tasks saved successfully")
        except FileNotFoundError:
            print("Error during saving:")


    def sort_tasks (self):
        self.tasks.sort(key=lambda data:data.priority)
        for i in self.tasks:
            print(i.title +" with priority :" + f"{i.priority}")
        print("Tasks sorted successfully")


    def mark_as_done(self):
        task_id=int(input("Enter the task id: "))
        task=self.find_task_by_id(task_id)
        task.status= "Done"
        print(task.title+" : marked as Done")
        self.save()




    def change_priority(self):
        task_id=int(input("Enter the task id: "))
        task = self.find_task_by_id(task_id)
        if task:
            while True:
                try:
                    new_priority = int(input("Enter new priority [0-5]: "))
                    if 0 <= new_priority <= 5:
                        task.priority = new_priority
                        print(" Priority updated.")
                        break
                    else:
                        print("Please enter a valid priority [0 - 5]")
                except ValueError:
                    print("Please enter a number.")
        self.save()



    def delete_task(self):
        task_id = int(input("Enter the task ID: "))
        task=self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(task.title + " deleted successfully")
        self.save()



def main():
    TaskOP = TaskManager()
    while True:
        menu()
        feature= input("Enter your choice please : ")
        match feature:
            case "1":
                print("Add Task")
                TaskOP.add_task()
            case "2":
                print("View Tasks")
                TaskOP.view_tasks()
            case "3":
                print("Sort Tasks")
                TaskOP.sort_tasks()
            case "4":
                print("Mark_As_Done")
                TaskOP.mark_as_done()
            case "5":
                print("Change priority")
                TaskOP.change_priority()
            case "6":
                print("Delete Task")
                TaskOP.delete_task()
            case "7":
                print("Exit")
                exit()
            case "8":
                print("Save the list")
                TaskOP.save()
if __name__ == "__main__":
    main()



