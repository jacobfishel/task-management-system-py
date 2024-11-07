#This file is for general funnction implementations

#prints the beginning option screen
def printOptions():
    print("---Welcome to the task manager---")
    print("1. Default")
    print("2. Queue")
    print("3. Priority")
    print("4. Dependency (Must complete one task to do the next)")
    print("5. DELETE ALL TASKS")
    return input("Select task format: ")



#Prints the menu options for the default (dictionary)
def printDefaultMenu():
    print()
    print("1. Add a task")
    print("2. Mark a task complete")
    print("3. Print tasks")
    print("4. Back to menu options")

    return input("Enter a choice: ")

def printQueueMenu():

    print()
    print("1. Add a task")
    print("2. Completed task")
    print("3. Print tasks")
    print("4. Back to menu options")

    return input("Enter a choice: ")  

def printHeapMenu():
    print()
    print("1. Add a task")
    print("2. Completed task")
    print("3. Print tasks")
    print("4. Back to menu options")

    return input("Enter a choice: ")  


def printDict(dict):
    print()
    print("================Tasks=====================")
    print("Name     Description")
    print("=======  =====================================")
    for name, description in dict.items():
        print(f"{name:<8} {description}")

def printQueue(queue):
    print()
    print("================Tasks=====================")
    print("Name     Description")
    print("=======  =====================================")

    for task in queue:
        print(f"{task[0]:<8} {task[1]}")
    

def addToDict(name, description, dict):
    if name not in dict:
        dict[name] = description
    else:
        print("Task already active:")
        #TODO: write a function to print all dict keys and values with brackets around this key value
        print()

def deleteFromDict(task_name, dict):
     #delete the task
    try:
        del dict[task_name]
    except KeyError:
        print("Invalid task name. No task deleted")

def deleteFromQueue(task_name, task_queue):

    #loop through tasks in queue
    for i in range(len(task_queue)):
        task = task_queue[i]
        print(task)

        #if the task name matches the name to delete, delete it
        if task[0] == task_name:
            print(f"Deleted {task} from queue")
            del task_queue[i]
            return



    

       





