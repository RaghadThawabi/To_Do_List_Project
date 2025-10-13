import json

tasks = []


def menu():
    print("1- Add Task ")
    print("2- View Tasks status ")
    print("3- Sort Tasks ")
    print("4- Mark_As_Done ")
    print("5- Change priority ")
    print("6- Delete Task ")
    print("7- Exit the program")
    print("8- Save the list  ")


def add_task():
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
    task = {"title": title, "description": description, "priority": priority, "status": "To-Do"}
    tasks.append(task)
    print("Task added : "+task["title"])
    print(" please save the task to not loss it ")


def view_tasks(tasks):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except Exception:
        print("No tasks found.")

    if len(tasks)==0:
        print("No tasks added yet !")

    for i in range(len(tasks)):
        task = tasks[i]
        print(f"{i + 1} . " + task['title'] + " - " + "the status is : " + task['status'])

    print("End of Tasks")



def save():
    try:
        try:
            with open("tasks.json", "r") as file:
                previous_list = json.load(file)
        except Exception :
            previous_list = []

        updated_list = previous_list + tasks

        with open("tasks.json", "w") as file:
            json.dump(updated_list, file, indent=4)
        print("Tasks saved successfully")
    except Exception:
        print("Error during saving:")



#  use this function for the sort , change status , delete , mark as done functions
def load_data():
    try:
        with open("tasks.json", "r") as file:
            tasks_from_file = json.load(file)
            return tasks_from_file
    except Exception:
        print("No tasks found in the list ")
        return []



def sort_tasks():
    tasks_data = load_data()
    tasks_data.sort(key=lambda data:data ['priority'])
    for x in tasks_data:
        print(x)


def mark_as_done():
    tasks_data = load_data()
    task_name=input("Enter the task name: ")
    for task in tasks_data:
        if task['title'] == task_name:
            task['status'] = "Done"
    print(task_name +" : marked as Done")

    with open("tasks.json", "w") as file:
        json.dump(tasks_data, file, indent=4)
    return


def change_priority():
    tasks_data = load_data()
    task_name = input("Enter the task name: ")
    for task in tasks_data:
        if task['title'] == task_name:
            while True:
                try:
                    priority1 = int(input("Enter priority , [highest : 0 - lowest : 5] "))
                    if 0 <= priority1 <= 5:
                        break
                except ValueError:
                    print("Please enter a valid priority [0 - 5]")
            task['priority'] = priority1
            print(task_name +" :priority  changed successfully")

    with open("tasks.json", "w") as file:
        json.dump(tasks_data, file, indent=4)


def main():
    while True:
        menu()
        feature= input("Enter your choice please : ")
        match feature:
            case "1":
                print("Add Task")
                add_task()
            case "2":
                print("View Tasks")
                view_tasks(tasks)
            case "3":
                print("Sort Tasks")
                sort_tasks()
            case "4":
                print("Mark_As_Done")
                mark_as_done()
            case "5":
                print("Change priority")
                change_priority()
            case "6":
                print("Delete Task")
                #delete_task()
            case "7":
                print("Exit")
                exit()
            case "8":
                print("Save the list")
                save()
if __name__ == "__main__":
    main()



