#!/usr/bin/python
import time
import sys
import copy
import math
import numpy as np
import matplotlib.pyplot as plt
import sudoku.backtrack as bt

def getMatrixFromFile(file):
    lines = [line.rstrip('\n') for line in open(file)]

    matrix = []
    for line in lines:
        row = []
        for num in line.split(","):
             row.append(int(num))

        matrix.append(row)
    
    return matrix
 
def main(argc, argv):
    #print("Starting the backtracking sudoko solver tests")
    
    #decide how many tests there are

    #Load the test names

    #question = [ [0]*9 for _ in xrange(9) ] 
    
    if argc != 2:
        print("Need to know the file")
        sys.exit(1)
    
    question = getMatrixFromFile(argv[1])

    #print("Question", question)

    #For now we are going to use just one test and its going to be hardcoded
    solver = bt.Sudoku(len(question))
    answer = solver.solve(question)

    if answer == None:
        print("No solution found");
        
    else:
        #print("Solved")
        solver.show(answer)
        
if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
