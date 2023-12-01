from threading import Thread

from multiprocessing import Pipe

from Lamport_timestamp import lamport_timestamp

from os import getpid

# This section, we test the Lamport_timestamp implementation from lamport_timestamp class,
# by defining the different 3 processes and in each processes, we call events that are gonna happen. 
# After defining the processes. We use the Pipe() to connect them and that are representing distributed systems. 

# The different pipes are used to create connection between processes. 
# For example, pipe 12 is for process one and two, pipe 32 is for process
# three and two and so on. 

# Different processes are created so that it represents a distributed system with threads
# and Pipe. 

def process_one(pipe12, pipe13):

    process = lamport_timestamp() 
    id = getpid()
    process.counter_process = 0

    process.increment_process(id)
    process.increment_process(id)
    process.received_signal(pipe13, id)
    process.received_signal(pipe12, id)
    process.send_signal(pipe12, id)
    process.send_signal(pipe13, id)
      
#def process_two(pipe21, pipe23):
def process_two(pipe21):
    process = lamport_timestamp()
    id = getpid() + 1
    process.counter_process = 0

    process.send_signal(pipe21, id)
    process.received_signal(pipe21, id)
    process.increment_process(id)
    

def process_three(pipe31):
    process = lamport_timestamp()
    id = getpid() + 2
    process.counter_process = 0

    process.send_signal(pipe31, id)
    process.received_signal(pipe31, id) 


if __name__ == '__main__':
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()
    oneandthree, threeandone = Pipe()

    # Create a thread that...
    thread1 = Thread(target = process_one,
                     args = (oneandtwo, oneandthree)) 
    
    # This thread...
    thread2 = Thread(target = process_two,
                     args = (twoandone, ))
    
    # This thread...
    thread3 = Thread(target = process_three,
                     args = (threeandone, ))
    
    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Flow of execution
    thread1.join()
    thread2.join()
    thread3.join()