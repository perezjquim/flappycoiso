import time
import threading

class CyclicThread(object):
    def __init__(self,method,sampling=1):
    	self.method = method;
    	self.sampling = sampling
	thread = threading.Thread(target=self.run, args=())
	thread.daemon = True                            # Daemonize thread
	thread.start()                                  # Start the execution

    def run(self):
        while 1:
            self.method()
            time.sleep(self.sampling)