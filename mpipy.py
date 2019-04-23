from mpi4py import MPI 
import threading
import random
import statistics

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

numList = list(random.sample(range(1,100), 20))

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

t1 = threading.Thread(name='t1', target=taskmean, args=(workerList,))
t2 = threading.Thread(name='t2', target=taskmedian, args=(workerList,))

t1.start()
t2.start()

print(workerList)

print('\n')