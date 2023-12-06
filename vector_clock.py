
    # Vector clocks

   # A vector clock of a system of N processes is a vector of N logical
   # clocks, one clock per process
    #I Initially all clocks are zero.
    #I Each time a process experiences an internal event, it
    #increments its own logical clock in the vector by one.
    #I Each time a process sends a message, it increments its own
    #logical clock in the vector by one and then sends a copy of its
    #own vector.
    #I Each time a process receives a message, it increments its own
    #logical clock in the vector by one and updates each element in
    #its vector by taking the element-wise maximum of the value in
    #its own vector clock and the value in the vector in the
    #received message

# Import necessary modules
from datetime import datetime

# The code is pretty much the same as in the lamport_timestamp.py file.
# The difference lies in how we calculate 

# class for vector_clocks. 
class vector_clocks:
    # Initialize initial time and vector clocks. Since we have vectors
    # and 3 processes, we have v(p0, p1, p2) with v being the vector. 
    def __init__(self):
        self.current_time = datetime.now()
        self.counter_process_vector = [0,0,0]

        # This function returns the lamport time and current time. 
    def local_time(self):
        return f" Lamport time = {self.counter_process_vector} "
    
    # This function increments the vector clocks of the process with id.
    # It's the same as lamport timestamp, but instead with vector, which we increment by incrementing
    # index. 
    def increment_vector(self, id):
        self.counter_process_vector[id] += 1
        
        # print the event happened.
        print("An event happened at: " + str(id) + str(self.local_time()))

        # return the vector clocks.
        return self.counter_process_vector
    
    # This function finds the maximum between the vector clocks of the process with id and the received timestamp.
    # As we work with vector, we can use for loop to iterate through the vector clocks.
    def max_process(self, received_timestamp):
        for i in range(len(self.counter_process_vector)):
            self.counter_process_vector[i] = max(self.counter_process_vector[i], received_timestamp[i])
        
        # return
        return self.counter_process_vector

    # This function receives the timestamp from the process with id from sender process
    def received_signal(self, pipe, id):
        # receive the timestamp from the sender process by using pipe.recv()
        timestamp = pipe.recv()
        # update the vector clocks with the maximum between the vector clocks of the process with id and the received timestamp.
        self.counter_process_vector = self.max_process(timestamp)

        # increment the vector clocks of the process with id.
        self.increment_vector(id)

        # print the event happened and which process it came from. 
        print(f" Message received at: {id} {self.local_time()} sent from {timestamp} ")
        # return
        return self.counter_process_vector
    

    # This function sends the message to the recipient process. 
    def send_signal(self, pipe, id):
        # increment the vector clocks of the process with id.
        self.counter_process_vector = self.increment_vector(id)
        # send the vector clocks to the recipient process by using pipe.send()
        pipe.send(self.counter_process_vector)
        # print the event happened and which process it sent from. 
        print(" Message sent from: " + str(id) + str(self.local_time()))
        # return
        return self.counter_process_vector
        
