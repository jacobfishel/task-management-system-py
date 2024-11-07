import json


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
                print("Not task_data")
                return  
            
            for task, description in task_data.items():

                #check for existing task
                if task in task_dict.keys():
                    print("Data already here")
                    continue

                #else add the task to the dict
                task_dict[task] = description
                print("Data added to dict")

        except FileNotFoundError:
            print("File not found")





#function to write data to the queue every time the program is opened
    #returns the queue after adding tasks.json data to it
    #can just take in the dict as a parameter and write from there since we already read from the file
def write_to_queue(task_queue, task_dict):

    for task in task_dict.items():
        #Add the task to the queue
        task_queue.append(task)

    