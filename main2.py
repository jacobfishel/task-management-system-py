import json
import heapq
from functions import *
from json_utils import *



while True:
    
    #Select which type of structure to hold tasks
    print()
    choice = printOptions()

    match str(choice):

        #DEFAULT (DICTIONARY) MENU
        case '1':
            pass
           
        #QUEUE MENU
        case '2':
            pass
        case '3':
            pass
           
        case '5':
            deleteAllTasks(task_dict, task_queue, task_min_heap)
            print("All tasks deleted.")




