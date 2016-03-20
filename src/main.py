#!/usr/bin/python
# Written By: Nicolas C. Broeking
# File: main.py
# Description: This program takes a file as input and solves it for the correct sudoku

import time
import sys
import copy
import math
import numpy as np
import matplotlib.pyplot as plt
import sudoku.backtrack as bt

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
   
    #There always needs to be an arg 
    if argc != 2:
        print("Need to know the file")
        sys.exit(1)
    
    #Get the matrix to solve
    question = getMatrixFromFile(argv[1])

    #Create the solver to solve sudoku
    solver = bt.Sudoku(len(question))

    #The answer that the solver has calculated
    answer = solver.solve(question)

    #If none then there was not a possible solution
    if answer == None:
        print("No solution found");
    
    #We found a solution so we should print the answer to stdout   
    else:
        #print("Solved")
        solver.show(answer)
        
#If the main module call main
if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
