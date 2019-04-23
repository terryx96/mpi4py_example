from mpi4py import MPI 
import threading
import random
import statistics

#Initialize MPI environment
#size = num processes (determined by -n command line flag)
#rank = process the code is running on
#name = name of the processor 
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

#create a random list of integers 
numList = list(random.sample(range(1,100), 20))

#determines where to split the list 
splitNum = len(numList)//size


print("I am process number %d" % rank)
if(rank == 0):
    workerList = (numList[:splitNum])
elif(rank == size-1):
    workerList = (numList[rank*splitNum:])
else:
    workerList = (numList[rank*splitNum:(rank+1)*splitNum])

def taskmean(lst):
    print("Mean: %d\n" % statistics.mean(lst))

def taskmedian(lst):
    print("Median: %d\n" % statistics.median(lst))

#create tasks to run on threads
t1 = threading.Thread(name='t1', target=taskmean, args=(workerList,))
t2 = threading.Thread(name='t2', target=taskmedian, args=(workerList,))

#run the tasks 
t1.start()
t2.start()

print(workerList)

print('\n')