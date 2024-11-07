import json
from functions import *
from json_utils import *

#after every change, write to file(update it)

#local task_dict: Will be read from the tasks.json file to start, then written to tasks.json to save tasks
task_dict = {}
#Task queue to implement a fifo data structure
task_queue = []
    
while True:
    #Update the data structures with the tasks.json file each loop
    write_to_dict(task_dict, filename='tasks.json')
    write_to_queue(task_queue, task_dict)

    #Select which type of structure to hold tasks
    print()
    choice = printOptions()

    match str(choice):

        #DEFAULT (DICTIONARY) MENU
        case '1':
            while True:
                default_choice = printDefaultMenu()

                match str(default_choice):
                    

                    #Add a task to the dict
                    case '1':
                        
                        #user input for name and description
                        print()
                        task_name = input("Enter a task name: ")
                        task_description = input("Enter task description: ")
                        
                        #add task to the dict, then update the file with the dict
                        addToDict(task_name, task_description, task_dict)
                        write_to_file(task_dict)
                    

                    #Mark a task as complete (delete task)
                    case '2':
                        printDict(task_dict)
                        task_name = input("Which task would you like to delete? (Enter task name)")

                        deleteFromDict(task_name, task_dict)

                        #update the file
                        write_to_file(task_dict)

                    #print tasks
                    case '3':
                        printDict(task_dict)

                    case '4':
                        break

                    case _:
                        break

        #QUEUE MENU
        case '2':
            while True:
                queue_choice = printQueueMenu()

                match str(queue_choice):

                    #Add a task
                    case '1':
                        task_name = input("Enter a task name: ")
                        task_description = input("Enter task description: ")
                        task = tuple([task_name, task_description])
                
                        #add task to queue
                        task_queue.append(task)

                        #add task to dict
                        addToDict(task_name, task_description, task_dict)

                        #update the file
                        write_to_file(task_dict)
                        print("Task added")

                    #Remove task from queue (Completed)
                    case '2':
                        task = task_queue.pop(0)
                        task_name = task[0]

                        #update dict
                        deleteFromDict(task_name, task_dict)

                        #update file
                        write_to_file(task_dict)

                        print(f"{task_name} complete")

                    #Print tasks from queue
                    case '3':
                        printQueue(task_queue)
                    
                    case '4':
                        break

                    case _:
                        break
            
        #PRIORITY QUEUE
        #TODO: implement priority queue
        #TODO probably need to erase the queue then update it when deleting from a dict
        case '3':
            pass


