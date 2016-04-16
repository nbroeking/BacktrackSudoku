#!/usr/bin/python
# Written By: Nicolas C. Broeking
# File: benchmarks.py
# Description: This program gets the benchmark data for different matricies 

import time
import sys
import copy
import math
import numpy as np
import matplotlib.pyplot as plt
import sudoku.backtrack as bt
import sudoku.generator as gen

#Read the matrix from the input file
def getMatrixFromFile(file):
    lines = [line.rstrip('\n') for line in open(file)]
    matrix = []
    
    #For each one of the lines we are going to split the intergers from , and then add them to the list
    for line in lines:
        row = []
        for num in line.split(","):
             row.append(int(num))

        matrix.append(row)
    
    return matrix
 
#The main function gets called when this is the main module
def main(argc, argv):

    #Benchmark all values of N up to 150

    fig = plt.figure()
    points = set()
    fakei = 3

    i = fakei*fakei

    for hints in range(0, 20):
        print "\t hints = " + str(hints)
        success = 1
        
        total = 30
        if fakei >= 4:
            total = 3
    
        while success <= total: 
            print "\t\tN = " + str(fakei) + " hints = " + str(hints) + " Success: " + str(success)+"/"+str(total)
            solver = bt.Sudoku()
            
            question = gen.generate(i, hints)
            
            #print("Question?", i)
            #solver.show(question)
            
            time1 = time.time()
            try:
                answer = solver.solve(question, i)
                time2 = time.time()
            
                calcTime = time2 - time1
            
                calcTime += calcTime*1000 
            #print("Answer")
            
                if answer != None:
                    #solver.show(answer)
                    success += 1
                    points.add((hints, calcTime))
            except ValueError as err:
                print "Skipping: "
                points.add((hints, 3600000))
       
    print "Completed Procesing"
 
    rate = list()

    x,y = zip(*points)
    plt.scatter(x,y)
    plt.xlabel("Hints")
    plt.ylabel("Time to solve (ms)")
    plt.suptitle("Time to Solve Matrix for n = 3")

    fig.savefig("nine.jpg")

    
    plt.show()

#If the main module call main
if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
