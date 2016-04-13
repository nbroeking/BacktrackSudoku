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
 
    for fakei in range(1, 5):
        print "Running sim for size " + str(fakei)
        i = fakei*fakei

        for hints in range(0, 15):
            print "\t hints = " + str(hints)
            success = 0
            
            total = 20
            if fakei > 4:
                total = 1

            while success < total: 
                print "\t\tN = " + str(i) + " hints = " + str(hints) + " Success: " + str(success)+"/"+str(total)
                solver = bt.Sudoku()
                
                question = gen.generate(i, hints)
                
                #print("Question?", i)
                #solver.show(question)
                
                time1 = time.time()
                answer = solver.solve(question, i)
                time2 = time.time()
                
                calcTime = time2 - time1
                
                calcTime += calcTime*1000 
                #print("Answer")
                
                if answer != None:
                    #solver.show(answer)
                    success += 1
                    points.add((fakei, calcTime))

        
    x,y = zip(*points)
    plt.scatter(x,y)
    plt.xlabel("Size of matrix")
    plt.ylabel("Time to solve (ms)")
    plt.suptitle("Time to solve matrix - No constraints")

    fig.savefig("noconstraints.jpg")

    plt.show()

#If the main module call main
if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
