import os

class Monkey(object):
    def __init__(self):
        self._cached_stamp = 0
        self.filename = '/home/panda/Downloads/log.txt'

     def replace_word():
	f = open("log.txt", "rt")
     	data = f.read()
        data=data.replace('sh','ssh')
        f.close()
        f = open("log.txt", "wt")
        f.write(data) # Overwrite input file with resulting data
        f.close()
       

    def ook(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            # File has changed, so do something...
	    replace_word()
	    
            

