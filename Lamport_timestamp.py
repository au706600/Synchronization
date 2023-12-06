
# https://towardsdatascience.com/understanding-lamport-timestamps-with-pythons-multiprocessing-library-12a6427881c6

# Lamport timestamp

# 1) All the process counters start with the value of 0

# 2) A process increments its counter for each event (internal event, message sending,
# message receiving) in that process

# 3) When a process sends a message, it includes its (incremented) counter value with the message

# 4) On receiving a message, the counter of the recipient is updated to the greater of its current
# counter (max) and the timestamp in the received message, and then incremented by one


# Initialize by setting the process counters with the value of 0

# Import necessary modules
from datetime import datetime

# lamport timestamp class
class lamport_timestamp:
    # Initialize initial time and counter process 
    # and all the necessary initialization that might be needed. 
    def __init__(self):
        self.current_time = datetime.now()
        self.counter_process = 0

        # function to return the local time and lamport time
    def local_time(self):
        return f" Lamport time = {self.counter_process}. "

# This function has the purpose of incrementing the process counter for 
# each event (internal event, message sending, message receiving) in that process
    def increment_process(self, id):
        # Increment the process counter
        self.counter_process += 1

        # Print the lamport time and local time. 
        print(" An event happened at: " + str(id) + str(self.local_time()))
        # return
        return self.counter_process
    
# This function has the purpose of finding the maximum value of the process counter and the timestamp in the received message
    def max_process(self, timestamp_received):
        # This line accepts a dictionary with the process id. 
        timestamp_received = timestamp_received["Lamport-timestamp"] 
        # Find maximum value of the process counter and the timestamp in the received message and increment
        increment = max(self.counter_process, timestamp_received) + 1
        # return
        return increment
    

# This function has the purpose of receiving a message from the sender process
    def received_signal(self, pipe, id):
        # pipe.recv() function receives the message from the sender process
        timestamp = pipe.recv()
        # Find maximum value of the process counter and the timestamp in the received message
        # by calling function
        self.counter_process = self.max_process(timestamp)
        # increment after finding the maximum
        self.increment_process(id)
        # print the message received from the sender process and which process
        # it comes from. 
        print(f' Message received at: {id} {self.local_time()} sent from {timestamp}')
        # return
        return self.counter_process

    
# This function has the purpose of sending a message to the recipient process
    def send_signal(self, pipe, id):
        # increment the process counter
        self.counter_process = self.increment_process(id) 
        # create a dictionary with the process id and timestamp
        message = {"process-Id": id, "Lamport-timestamp": self.counter_process} 
        # send the message with the process id to the recipient process by using pipe.send()
        pipe.send(message) 
        # print the message sent
        print(f" Message sent from process-Id: {id} and {self.local_time()}") 
        # return the process counter
        return self.counter_process 



        





        

