import json
import heapq


#Function to write data to the tasks.json file to store tasks
def write_to_file(data = {}):

    try:
        with open('tasks.json', 'w') as f:
            json.dump(data, f)

    except FileNotFoundError:
        print("Could not write data to file. File not found.")

def read():

    try:
        with open('tasks.json', 'r') as f:
                for task in f:
                    print(task)

    except FileNotFoundError:
        print("Could not read data. File not found")


#function to write data to the queue every time the program is opened
    #returns the queue after adding tasks.json data to it
def write_to_dict(task_dict, filename='tasks.json'):

    with open(filename, 'r') as f:
 
        try:
            task_data = json.load(f)

            #if file is empty return
            if not task_data:
                print("In write_to_dict. Nothing to write")
                return  
            
            for name, info in task_data.items():
                description = list(info.keys())[0]
                priority = info[description]

                #check for existing task
                if name in task_dict.keys():
                    print("In write_to_dict. Duplicate task")
                    continue

                #else add the task to the dict
                task_dict[name] = {description: priority}

        except FileNotFoundError:
            print("In write_to_dict. File not found")





#function to write data to the queue every time the program is opened
    #returns the queue after adding tasks.json data to it
    #can just take in the dict as a parameter and write from there since we already read from the file
def write_to_queue(task_queue, task_dict):

    for dName, dInfo in task_dict.items():
        dDescription = list(dInfo.keys())[0]
        dPriority = dInfo[dDescription]

        duplicate = False

        for tTask in task_queue:
            task_info = tTask[1]
            task_name = list(task_info.keys())[0]

            if task_name == dName:
                duplicate = True                

        if duplicate == True:
            continue

        else:
            task_queue.append((dPriority, {dName: dDescription}))      
        continue



def write_to_heap(task_min_heap, task_dict):
    #write all the new tasks to the heap with a priority of 5
#data structure
#dict:    {'name': {'desc': 'priotity'}}
#heap:    (priority, {'name': 'description'})  


         for dName, dInfo in task_dict.items():

            if not task_min_heap:
                description = list(dInfo.keys())[0]
                priority = dInfo[description]
                heapq.heappush(task_min_heap, (priority, {dName: description}))
                continue
                
            #if its not empty:
                #verify there is no duplicate
            else:
                duplicate = False

                for hTask in task_min_heap:
                    task_info = hTask[1]
                    hName = list(task_info.keys())[0]
                    hDescription = task_info[hName]

                    if hName == dName:
                        duplicate = True    
                                    

                if duplicate == True:
                    continue

                else:
                    heapq.heappush(task_min_heap, (priority, {dName: hDescription}))

                continue



def deleteAllTasks(task_dict, task_queue, task_min_heap, filename='tasks.json'):

    #clear dict and queue
    task_dict.clear()
    task_queue.clear()
    task_min_heap.clear()

    #dump an empty dict in the file to clear it
    with open(filename, 'w') as f:
        json.dump({}, f)
