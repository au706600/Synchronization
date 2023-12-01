

from threading import Thread
from multiprocessing import Pipe

from Lamport_timestamp import lamport_timestamp
from os import getpid

# The different pipes are used to create connection between processes. 
# For example, pipe 12 is for process one and two, pipe 32 is for process
# three and two and so on. 


# Different processes are created so that it represents a distributed system with threads
# Pipe

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

    #---------------------------------------------------

from threading import Thread
from multiprocessing import Pipe

from vector_clock import vector_clocks


def one_process(pipe12, pipe13):
    vectorclock = vector_clocks()
    id = 0
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.increment_vector(id) 
    vectorclock.send_signal(pipe12, id) 
    vectorclock.counter_process_vector = vectorclock.received_signal(pipe12, id)
    #vectorclock.received_signal(pipe12, id) 
    vectorclock.send_signal(pipe13, id)
    vectorclock.counter_process_vector = vectorclock.received_signal(pipe12, id)
    #vectorclock.received_signal(pipe13, id) 
    vectorclock.send_signal(pipe12, id)
    vectorclock.increment_vector(id)

#def two_process(pipe21, pipe23):
def two_process(pipe21):
    vectorclock = vector_clocks()
    id = 1
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.send_signal(pipe21, id)
    vectorclock.counter_process_vector = vectorclock.received_signal(pipe21, id)
    vectorclock.counter_process_vector = vectorclock.received_signal(pipe21, id)
    #vectorclock.received_signal(pipe21, id)
    #vectorclock.received_signal(pipe21, id) 

#def three_process(pipe32, pipe31):
def three_process(pipe31):
    vectorclock = vector_clocks()
    id = 2
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.increment_vector(id)
    vectorclock.send_signal(pipe31, id)
    vectorclock.counter_process_vector = vectorclock.received_signal(pipe31, id)
    #vectorclock.received_signal(pipe31, id)

if __name__ == '__main__':
    
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()
    oneandthree, threeandone = Pipe()

    threadone = Thread(target = one_process, 
                    args=(oneandtwo, oneandthree))
    
    threadtwo = Thread(target = two_process, 
                    args = (twoandone, ))
    
    threadthree = Thread(target = three_process, 
                        args = (threeandone, ))
    
    threadone.start()
    threadtwo.start()
    threadthree.start()

    threadone.join()
    threadtwo.join()
    threadthree.join()

#-----------

# second test case

from threading import Thread
from multiprocessing import Pipe

from vector_clock import vector_clocks

def one_process(pipe12):
    vectorclock = vector_clocks()
    id = 0
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.increment_vector(id) 
    vectorclock.send_signal(pipe12, id)
    vectorclock.increment_vector(id)
    vectorclock.counter_process_vector = vectorclock.received_signal(pipe12, id)
    vectorclock.increment_vector(id)

#def two_process(pipe21, pipe23):
def two_process(pipe21, pipe23):
    vectorclock = vector_clocks()
    id = 1
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.increment_vector(id)
    vectorclock.counter_process_vector = vectorclock.received_signal(pipe21, id)
    vectorclock.counter_process_vector = vectorclock.received_signal(pipe23, id)
    vectorclock.send_signal(pipe21, id)
    vectorclock.increment_vector(id)

#def three_process(pipe32, pipe31):
def three_process(pipe32):
    vectorclock = vector_clocks()
    id = 2
    vectorclock.counter_process_vector = [0,0,0]

    vectorclock.send_signal(pipe32, id)
    vectorclock.increment_vector(id)

if __name__ == '__main__':
    
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()
    oneandthree, threeandone = Pipe()

    threadone = Thread(target = one_process, 
                    args=(oneandtwo, ))
    
    threadtwo = Thread(target = two_process, 
                    args = (twoandone, twoandthree))
    
    threadthree = Thread(target = three_process, 
                        args = (threeandtwo, ))
    
    threadone.start()
    threadtwo.start()
    threadthree.start()

    threadone.join()
    threadtwo.join()
    threadthree.join()


