import heapq
import task


class TaskStorage():
    def __init__(self, task_array=[], task_queue=[], task_heap=[]):
        self.task_array = task_array
        self.task_queue = task_queue
        self.task_heap = task_heap

    def addToList(self, task):
        self.task_array.append(task)
        self.task_array.append(task)
        heapq.heappush(self.task_heap, (task.priority, task))   #create a tuple to sort by priority
        
        #add to the heap based on priorityqueue

    def addToQueue(self):
        pass

    def addToHeap(self):
        pass

    def deleteFromList(self):
        pass

    def deleteFromQueue():
        pass

    def deleteFromHeap():
        pass

    def writeToAll(self):
        pass

        


        
        
    