import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

import schedule  

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
   # path= '/home/panda/Downloads'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
	# Scheduler
    def job():
        f = open("log.txt", "rt")
        data = f.read()
# Trying to replace
        data=data.replace('sh','ssh')
        f.close()
        f = open("log.txt", "wt")
        f.write(data) # Overwrite input file with resulting data
        f.close()
            
	 
    schedule.every(3).seconds.do(job)
    while True:
        schedule.run_pending()
        #time.sleep(1)


    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
