import json
import heapq
from functions import *
from json_utils import *

#after every change, write to file(update it)

#local task_dict: Will be read from the tasks.json file to start, then written to tasks.json to save tasks
task_dict = {}

#Task queue to implement a fifo data structure
task_queue = []

#heap to implement priority queue
task_min_heap = []

while True:
    #Update the data structures with the tasks.json file each loop
    write_to_dict(task_dict, filename='tasks.json')
    write_to_queue(task_queue, task_dict)
    write_to_heap(task_min_heap, task_dict)



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
                        addToQueue(task_name, task_description, task_queue)
                        
                        #update the file and the queue
                        write_to_file(task_dict)                    

                    #Mark a task as complete (delete task)
                    case '2':
                        printDict(task_dict)
                        task_name = input("Which task would you like to delete? (Enter task name): ")

                        deleteFromDict(task_name, task_dict)
                        deleteFromQueue(task_name, task_queue)

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
                
                        #add task to queue
                        addToQueue(task_name, task_description, task_queue)

                        #add task to dict
                        addToDict(task_name, task_description, task_dict)

                        #update the file
                        write_to_file(task_dict)

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
            while True:
                heap_choice = printHeapMenu()

                match str(heap_choice):

                    #Add a task
                    case '1':
                        priority = input("Enter the priority: ")
                        task_name = input("Enter a task name: ")
                        task_description = input("Enter task description: ")

                        priotiry_task = tuple([priority, {task_name: task_description}])

                        #add to the heap
                        heapq.heappush(task_min_heap, priotiry_task)
                
                        #add task to queue
                        addToQueue(task_name, task_description, task_queue)

                        #add task to dict
                        addToDict(task_name, task_description, task_dict)

                        #update the file
                        write_to_file(task_dict)

                    #Remove task from queue (Completed)
                    case '2':
                        #pop from heap
                        highest_priority = heapq.heappop(task_min_heap)

                        #access the actual task
                        task = highest_priority[1]

                        task_name = task.keys()

                        #delete from queue
                        deleteFromQueue(task_name, task_queue)

                        #update dict
                        deleteFromDict(task_name, task_dict)

                        #update file
                        write_to_file(task_dict)

                        print(f"{task_name} complete")

                    

                    case '4':
                        pass
                        #TODO:  print heap tasks
                    
                    case '5':
                        break

                    case _:
                        break

        case '5':
            deleteAllTasks(task_dict, task_queue, task_min_heap)
            print("All tasks deleted.")




