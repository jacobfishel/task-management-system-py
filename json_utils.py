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
                return  
            
            for name, info in task_data.items():
                description = info.keys()
                priority = info[description]

                #check for existing task
                if name in task_dict.keys():
                    continue

                #else add the task to the dict
                task_dict[name] = {description: priority}

        except FileNotFoundError:
            print("File not found")





#function to write data to the queue every time the program is opened
    #returns the queue after adding tasks.json data to it
    #can just take in the dict as a parameter and write from there since we already read from the file
def write_to_queue(task_queue, task_dict):

    for dName, dInfo in task_dict.items():

        duplicate = False

        for tTask in task_queue:
            task_name = tTask[0]

            if task_name == dName:
                duplicate = True                

        if duplicate == True:
            continue

        else:
            description = dInfo.keys()
            task_queue.append(tuple([dName, description]))      
        continue


# write_to_queue(task_queue=[('1', '1'), ('2', 'two')], task_dict={'1': '1', '3': '3', '2': 'two'}) 
# 
# 
#TODO: write_to_min_heap
def write_to_heap(task_min_heap, task_dict, priority=5):
    #write all the new tasks to the heap with a priority of 5
#data structure
#dict:    {'name': {'desc': 'priotity'}}
#heap:    (priority, {'name': 'description'})  

        

         for dName, dInfo in task_dict.items():

            duplicate = False

            for hTask in task_min_heap:
                task_info = hTask[1]
                hName = task_info.keys()

                if hName == dName:
                    duplicate = True                

            if duplicate == True:
                continue

            else:
                description = task_info[hName]
                heapq.heappush(task_min_heap, tuple([priority, {dName: description}]))

            continue


def deleteAllTasks(task_dict, task_queue, task_min_heap, filename='tasks.json'):

    #clear dict and queue
    task_dict.clear()
    task_queue.clear()
    task_min_heap.clear()

    #dump an empty dict in the file to clear it
    with open(filename, 'w') as f:
        json.dump({}, f)

    