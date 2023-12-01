
# https://towardsdatascience.com/understanding-lamport-timestamps-with-pythons-multiprocessing-library-12a6427881c6

# Lamport timestamp

# 1) All the process counters start with the value of 0

# 2) A process increments its counter for each event (internal event, message sending,
# message receiving) in that process

# 3) When a process sends a message, it includes its (incremented) counter value with the message

# 4) On receiving a message, the counter of the recipient is updated to the greater of its current
# counter (max) and the timestamp in the received message, and then incremented by one


# Initialize by setting the process counters with the value of 0

from datetime import datetime

class lamport_timestamp:
    def __init__(self):
        self.current_time = datetime.now()
        self.counter_process = 0

    def local_time(self):
        return f" Lamport time = {self.counter_process}, Local time = {self.current_time}. "

# This function has the purpose of...
    def increment_process(self, id):
        self.counter_process += 1

        print(" An event happened at: " + str(id) + str(self.local_time()))
        return self.counter_process
    
# This function has the purpose of...
    def max_process(self, timestamp_received):
        timestamp_received = timestamp_received["timestamp"]
        increment = max(self.counter_process, timestamp_received) + 1
        return increment
    

# This function has the purpose of...
    def received_signal(self, pipe, id):
        timestamp = pipe.recv()
        self.counter_process = self.max_process(timestamp)
        self.increment_process(id)
        print(f" Message received at: {id} {self.local_time()} sent from {timestamp}")
        return self.counter_process
    
# This function has the purpose of...
    def send_signal(self, pipe, id):
        self.counter_process = self.increment_process(id)
        message = {"process": id, "timestamp": self.counter_process}
        pipe.send(message)
        print(f" Message sent from: + {id} + {self.local_time()}")
        return self.counter_process



        





        

