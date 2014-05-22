# Created on 22/05/2014
# Author: Tartuffe

import sys

def reverse_string(string):
    print "Reversed string is: "
    for i in range(len(string)):   
       sys.stdout.write(string[-1-i]) 
    sys.stdout.write("\n")
       
if __name__ == '__main__':
    string = raw_input("Please, input your string:")
    print "Reversed string is: "
    for i in range(len(string)):   
       sys.stdout.write(string[-1-i])
       """
         Instead it could be also used this:
         sys.stdout.softspace = 0 #no space between characters
         print string[-1-i],      #all output in same line
       """
