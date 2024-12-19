#task management system using data structures in python

plan: 
have json files to read from and to write tasks into to save them

data structures:

    list for general storage of tasks
    dictionary for storing tasks with a title(might use this instead of list)

    heap to prioritize tasks

    graph to implement dependencies for tasks

    queue to manage tasks in a fifo order


#documentation:

dict will be stored:
     {'task_name': {'task_description': 'priority'}}
     
Heap/queue will be stored with data like:
     (priority, {'task_name': 'task_description'})

11.19.2024
overall making it so there is no duplicate priorities, since the heapq.heappush isnt allowing this, unless I can find another way to do this. 

Modified addToHeap to try to make it find the largest priority and make the new task being added include that value + 1. If I do this, I will need to change some other functions so that when you add a heap, it will reheapify and increase all priorities + 1 so that you can add whatever priority you like


