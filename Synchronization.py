

# Import the necessary modules. 
from threading import Thread

from multiprocessing import Pipe

from Lamport_timestamp import lamport_timestamp

from os import getpid

# This section, we test the Lamport_timestamp implementation from lamport_timestamp class
# by creating 3 different processes and in each processes, we envoke events by calling them from our class. In each process, 
# we want the id's it to be unique by using the getpid() function and increment it by 1 in process 2 and 2 in process 3. In each
# process, we initialize the counter to 0. After defining the processes. We use the Pipe() to connect them and that are representing distributed systems.
# We update the counter/timestamps by envoking the different events. 

# The different pipes are used to create connection between processes. 
# For example, pipe 12 is for process one and two, pipe 32 is for process
# three and two and so on. 

# Different processes are created so that it represents a distributed system with threads
# and Pipe. 

# Process one
def process_one(pipe12, pipe13):

    process = lamport_timestamp() 
    id = getpid()
    process.counter_process = 0

    process.increment_process(id)
    process.increment_process(id)
    process.received_signal(pipe13, id)
    process.increment_process(id)
    process.received_signal(pipe12, id)
    process.send_signal(pipe12, id)
    process.send_signal(pipe13, id)

# Process two
#def process_two(pipe21, pipe23):
def process_two(pipe21):
    process = lamport_timestamp()
    id = getpid() + 1
    process.counter_process = 0

    process.send_signal(pipe21, id)
    process.received_signal(pipe21, id)
    process.increment_process(id)
    

# Process three
def process_three(pipe31):
    process = lamport_timestamp()
    id = getpid() + 2
    process.counter_process = 0

    process.send_signal(pipe31, id)
    process.received_signal(pipe31, id) 


# In order to run the different processes, we need to start them by using Pipe() to connect them
# and then we need to join them by using join() function from threads.
if __name__ == '__main__':
    # Defining the pipes in order to connect them. 
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()
    oneandthree, threeandone = Pipe()

    # This thread have the function process_one() and the arguments are the pipes.
    # Thread() have the purpose of running the process in a different thread.
    thread1 = Thread(target = process_one,
                     args = (oneandtwo, oneandthree)) 
    
    # This thread have the function process_two() and the arguments are the pipes.
    # Thread() have the purpose of running the process in a different thread.
    thread2 = Thread(target = process_two,
                     args = (twoandone, ))
    
     # This thread have the function process_three() and the arguments are the pipes.
     # Thread() have the purpose of running the process in a different thread.
    thread3 = Thread(target = process_three,
                     args = (threeandone, ))
    
    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Flow of execution. After all the processes have run, quit the program.
    thread1.join()
    thread2.join()
    thread3.join()

    #---------------------------------------------------

# Import the necessary modules. 
from threading import Thread
from multiprocessing import Pipe

from vector_clock import vector_clocks


# This section, we test the vector_clock implementation from vector_clocks class,
# by defining the different 3 processes and in each processes, we call events that are gonna happen. 
# After defining the processes. We use the Pipe() to connect the processes and that are representing distributed systems
# like the lamport timestamp implementation. We update the counter/timestamps by envoking the different events (see above)

# This is the first test-case: 

# Process one
def one_process(pipe12, pipe13):
    vectorclock = vector_clocks()
    id = 0
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.increment_vector(id) 
    vectorclock.send_signal(pipe12, id) 
    vectorclock.increment_vector(id)
    vectorclock.received_signal(pipe13, id)
    vectorclock.send_signal(pipe12, id)

# Process two
def two_process(pipe21, pipe23):
    vectorclock = vector_clocks()
    id = 1
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.increment_vector(id)
    vectorclock.received_signal(pipe21, id)
    vectorclock.increment_vector(id)
    vectorclock.send_signal(pipe23, id)
    vectorclock.increment_vector(id)
    vectorclock.received_signal(pipe21, id)

# Process three
def three_process(pipe31, pipe32):
    vectorclock = vector_clocks()
    id = 2
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.increment_vector(id)
    vectorclock.received_signal(pipe32, id)
    vectorclock.increment_vector(id)
    vectorclock.send_signal(pipe31, id)

if __name__ == '__main__':
    
    # Defining the pipes in order to connect them.
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()
    oneandthree, threeandone = Pipe()

    # This thread have the function process_one() and the arguments are the pipes.
    # Thread() have the purpose of running the process in a different thread.
    threadone = Thread(target = one_process, 
                    args=(oneandtwo, oneandthree))
    
    # This thread have the function process_two() and the arguments are the pipes.
    # Thread() have the purpose of running the process in a different thread.
    threadtwo = Thread(target = two_process, 
                    args = (twoandone, twoandthree))
    
    # This thread have the function process_three() and the arguments are the pipes.
    # Thread() have the purpose of running the process in a different thread.
    threadthree = Thread(target = three_process, 
                        args = (threeandone, threeandtwo))
    
    # Start the threads
    threadone.start()
    threadtwo.start()
    threadthree.start()

    # Flow of execution. After all the processes have run, quit the program.
    threadone.join()
    threadtwo.join()
    threadthree.join()

#-----------

# second test case for vector_clock
# Import the necessary modules.
from threading import Thread
from multiprocessing import Pipe

from vector_clock import vector_clocks

# This section, we test the vector_clock implementation from vector_clocks class,
# by defining the different 3 processes and in each processes, we call events that are gonna happen.
# After defining the processes. We use the Pipe() to connect the processes and that are representing distributed systems

# This is the second test-case:

# Process one
def one_process(pipe12):
    vectorclock = vector_clocks()
    id = 0
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.increment_vector(id) 
    vectorclock.send_signal(pipe12, id)
    vectorclock.increment_vector(id)
    vectorclock.received_signal(pipe12, id)
    vectorclock.increment_vector(id)

# Process two
#def two_process(pipe21, pipe23):
def two_process(pipe21, pipe23):
    vectorclock = vector_clocks()
    id = 1
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.increment_vector(id)
    vectorclock.received_signal(pipe21, id)
    vectorclock.received_signal(pipe23, id)
    vectorclock.send_signal(pipe21, id)
    vectorclock.increment_vector(id)

# Process three
#def three_process(pipe32, pipe31):
def three_process(pipe32):
    vectorclock = vector_clocks()
    id = 2
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.send_signal(pipe32, id)
    vectorclock.increment_vector(id)

if __name__ == '__main__':
    # Defining the pipes in order to connect them.
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()
    #oneandthree, threeandone = Pipe()

    # This thread have the function process_one() and the arguments are the pipes.
    # Thread() have the purpose of running the process in a different thread.
    threadone = Thread(target = one_process, 
                    args=(oneandtwo, ))
    
    # This thread have the function process_two() and the arguments are the pipes.
    # Thread() have the purpose of running the process in a different thread.
    threadtwo = Thread(target = two_process, 
                    args = (twoandone, twoandthree))
    

    # This thread have the function process_three() and the arguments are the pipes.
    # Thread() have the purpose of running the process in a different thread.
    threadthree = Thread(target = three_process, 
                        args = (threeandtwo, ))
    
    # Start the threads
    threadone.start()
    threadtwo.start()
    threadthree.start()

    # Flow of execution. After all the processes have run, quit the program.
    threadone.join()
    threadtwo.join()
    threadthree.join()


