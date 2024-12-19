import heapq
from collections import deque
import math

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

    for name, info in dict.items():
        #turn the view object of the keys into a list to access description
        description = list(info.keys())[0]
        print(f"{name:<8} {description}")


def printQueue(queue):
    print()
    print("================Tasks=====================")
    print("Name     Description")
    print("=======  =====================================")

    # print(queue)
    if queue:
        for task in queue:
            info = task[1]
            task_name = list(info.keys())[0]
            task_description = info[task_name]

            print(f"{task_name:<8} {task_description}")
    else:
        print("Queue is empty")

def printHeap(heap):
    print()
    print("======================Tasks===========================")
    print("Priority      Name       Description")
    print("========      =========  =============================")

    temp = heap.copy()

    while temp:

        task = heapq.heappop(temp)
        task_priority = task[0]
        task_info = task[1]
        task_name = list(task_info.keys())[0]
        task_description = task_info[task_name]

        print(f"{task_priority:<13} {task_name:<10} {task_description}")

    

def addToDict(name, description, dict, priority=5):
    #{'name': {"description": "priority"}}
    if name not in dict:
        info = {description: priority}
        dict[name] = info
    else:
        print("Task already active:")
        #TODO: write a function to print all dict keys and values with brackets around this key value
        print()
        return

def addToQueue(task_name, task_description, task_queue, priority=5):

    for task in task_queue:
        qInfo = task[1]
        qName = list(qInfo.keys())[0]

        if qName == task_name:
            print("Task already in queue.")
            return
        
    valid_task = (priority, {task_name: task_description})
    task_queue.append(valid_task)

def addToHeap(task_name, task_description, task_min_heap, priority=5):
    #used when the other data structures are being modified to add tasks here in the background

    for task in task_min_heap:
        task_info = task[1]
        name = list(task_info.keys())[0]

        if name == task_name:
            print("Task already in queue")
            return
        largestPriority = searchHeapPriority(task_min_heap, priority)            
        priority = largestPriority + 1

        valid_task = (priority, {task_name: task_description})
        heapq.heappush(task_min_heap, valid_task)



def deleteFromDict(task_name, dict):
     #delete the task
    try:
        del dict[task_name]
    except KeyError:
        print("In deleteFromDict. Invalid task name. No task deleted")

def deleteFromQueue(task_name, task_queue):

    #loop through tasks in queue
    for i in range(len(task_queue)):
        task = task_queue[i]
        task_info = task[1]
        tName = list(task_info.keys())[0]

        #if the task name matches the name to delete, delete it
        if tName == task_name:
            del task_queue[i]
            return
    print("Could Not find task in queue")
        


def searchHeap(task_name, task_min_heap, priority=5):
    #implementing a breadth first search to use the heap data structure

    #search the heap for this task name and return True if found else False

    #start with root index
    if not task_min_heap:
        print("In searchHeap. Heap empty")
        return -1
    
    queue = deque([0])  #root node

    while queue:

        index = queue.popleft()

        task = task_min_heap[index]
        task_priority = task[0]
        task_info = task[1]
        taskName = list(task_info.keys())[0]

        if taskName == task_name:
            return index
        
        left = index * 2 + 1
        right = index * 2 + 2

        if left < len(task_min_heap) and task_priority <= priority:
            queue.append(left)
        if right < len(task_min_heap) and task_priority <= priority:
            queue.append(right)

    return -1

def searchHeapPriority(task_min_heap):
    #start at leafTotal - 1 and go to n
    #2->1
    #3->2
    #4->2
    #5->3
    #6->3
    #7->4
    #8->4
    #9->5
    n = len(task_min_heap)
    leafTotal = math.floor(n/2)
    maxVal = 0
    for i in range((leafTotal - 1), leafTotal):
        currentVal = task_min_heap[i]
        if currentVal > maxVal:
            maxVal = currentVal
    return maxVal


    



def deleteFromHeap(task_name, task_min_heap, priority=5):

    #True if the task is in the heap, and the index of it
    index = searchHeap(task_name, task_min_heap, priority)

    if index == -1:
        print("In deleteFromHeap. Task not found in heap")
        return
       
    else:
        del task_min_heap[index]    



#I need the priority to implement the breadth first search in the heap
def getPriority(task_name, task_dict):
    #return the priority of the task 
    task_info = task_dict[task_name]
    description = list(task_info.keys())[0]
    priority = task_info[description]
    
    return priority
        


def practice(arr=[(1, {'task1':'desc1'}), (2, {'task2': 'desc2'}), (2, {'task3': 'desc3'}), (5, {'task4': 'desc4'})], priority=5):
    
    if 1 in arr:
        print("1")

practice()
    


    

