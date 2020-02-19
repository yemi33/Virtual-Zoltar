'''
fileProcessing.py

A Python program that processes, analyzes, and visualizes earthquake data. SOLUTIONS.

author: Yemi Shin
CS 111, Fall 2018
date: 5 October 2018
'''

def processFile(f):
    '''
    Reads in data from a file, and stores it in a list.

    PARAMETER:
        f - the name of the file

    RETURN VALUE:
        a list containing the data from the file.
    '''
    lst = []
    infile = open(f, "r")
    for line in infile:
        value = str(line)
        lst.append(value)
    
    infile.close()
    return lst
