#!/usr/bin/env python3
import fileinput
filename ='Joint_Limit_Test.java'
with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
           print(line.replace('Thread.sleep(1000);', 'Thread.sleep(500);'), end='')
           
      
        
       
