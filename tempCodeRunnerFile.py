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
    vectorclock.increment_vector(id)

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
    #vectorclock.received_signal(pipe21, id)

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