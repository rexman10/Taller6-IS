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
    removedTask = tasks.pop(indice)
    removedStatus = status.pop(indice)
    return (removedTask, removedStatus)

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
    for i in range(len(tasks)):
        if tasks[i] == tarea:
            status[i] = "Completed"

def mark_inProgress(tarea):
    for i in range(len(tasks)):
        if tasks[i] == tarea:
            status[i] = "In Progress"

def clear_todo_list():
    for i in range(len(tasks)):
        tasks.pop()
        status.pop()

def print_opciones():
    print("1. Show Tasks\n2. Add tasks\n3. Remove tasks\n4. Complete tasks\n5. Progress task\n6. Clear tasks")

def todo_list():
    print_opciones()
    while True:
        entrada = int(input("Choose an option: "))
        if entrada == 1:
            list_tasks(tasks)
            print()
            print_opciones()
        elif entrada == 2:
            entrada = input("Write a task to add: ")
            add_task(entrada)
            print()
            print_opciones()
        elif entrada == 3:
            list_tasks(tasks)
            entry = input("Write a task to remove: ")
            remove_task(entry)
            print()
            print_opciones()
        elif entrada == 4:
            task_to_complete = input("Write a task to complete: ")
            mark_completed(task_to_complete)
            print()
            print_opciones()
        elif entrada == 5:
            task_to_progress = input("Write a task to set in progress: ")
            mark_inProgress(task_to_progress)
            print()
            print_opciones()
        elif entrada == 6:
            clear_todo_list()
            print()
            print_opciones()
        else:
            print("Invalid choice")
            break

def prepare_List():
    add_task("Buy groceries")
    add_task("Pay bills")
