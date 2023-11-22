
    # Vector clocks

    # 1) All counters are set to zero, for example [0,0,0]

    # 2) Each time a process experiences an event, it increments its own counter in the vector by one

    # 3) Each time a process sends a message, it includes a copy of its own incremented vector in the image

    # 4) Each time a process receives a message, it increments its own counter in the vector by one and 

    # updates each element in its vector by taking the maximum of the value in its own vector counter 

    # and the value in the vector in the received message. 

from datetime import datetime

class vector_clocks:
    def __init__(self):
        self.current_time = datetime.now()
        self.counter_process_vector = self.current_time

    def local_time(self):
        return f" Lamport time = {self.counter_process_vector}, Local time = {self.current_time} "
    
    def increment_vector(self, id):
        self.counter_process_vector[id] += 1
        
        print("An event happened at: " + str(id) + str(self.local_time()))
        return self.counter_process_vector
    
    def max_process(self, received_timestamp):
        for i in range(len(self.counter_process_vector)):
            self.counter_process_vector[i] = max(self.counter_process_vector[i], received_timestamp[i])
        
        return self.counter_process_vector
    

    def received_signal(self, pipe, id):
        timestamp = pipe.recv()
        self.counter_process_vector = self.max_process(timestamp)

        self.increment_vector(id)

        #print("Message received at: " + str(id) + str(self.local_time()) + f"sent from {timestamp}")
        print(f" Message received at: {id} {self.local_time()} sent from {timestamp} ")
        return self.counter_process_vector
    

    def send_signal(self, pipe, id):
        self.counter_process_vector = self.increment_vector(id)
        pipe.send(self.counter_process_vector)
        print(" Message sent from: " + str(id) + str(self.local_time()))
        return self.counter_process_vector
        
