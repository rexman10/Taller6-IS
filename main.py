##Suggested Features: 
## Add a task to the to-do list. 
## List all tasks in the to-do list. 
## Mark a task as completed. 
## Clear the entire to-do list. 
##Note: Add two more features, so it becomes 6 in total.

tasks = []
status = []

def add_task(tarea):
    tasks.append(tarea)
    status.append("Pending")

def remove_task(tarea):
    indice = search_task(tarea)
    tasks.remove(tarea)
    status.pop(indice)

def list_tasks(lista):
    print("Tasks:")
    for tarea in lista:
        print("- "+tarea)

def search_task(entrada):
    i = 0
    for tarea in tasks:
        if entrada == tarea:
            return i
        else:
            i += 1

def mark_completed(tarea):
    index = search_task(tarea)
    status[index] = "Completed"

def mark_inProgress(tarea):
    index = search_task(tarea)
    status[index] = "In Progress"

def clear_todo_list():
    tasks = []
    status = []

def print_opciones():
    print("1. Show Tasks\n2. Add tasks\n3. Remove tasks\n4. Complete tasks\n5. Progress task\n6. Clear tasks")

def todo_list():
    print_opciones()
    while True:
        entrada = int(input("Choose an option: "))
        match entrada:
            case 1:
                list_tasks(tasks)
                print()
                print_opciones()
            case 2:
                entrada = input("Write a task to add: ")
                add_task(entrada)
                print()
                print_opciones()
            case 3:
                list_tasks(tasks)
                entry = input("Write a task to remove: ")
                remove_task(entry)
                print()
                print_opciones()
            case 4:
                task_to_complete = input("Write a task to complete: ")
                mark_completed(task_to_complete)
                print()
                print_opciones()
            case 5:
                task_to_progress = input("Write a task to set in progress: ")
                mark_inProgress(task_to_progress)
                print()
                print_opciones()
            case 6:
                clear_todo_list()
                print()
                print_opciones()
            case _:
                print("Invalid choice")
                break

add_task("Buy groceries")
add_task("Pay bills")

todo_list()


    