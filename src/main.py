#!/usr/bin/python
import time
import sys
import copy
import math
import numpy as np
import matplotlib.pyplot as plt
import sudoku.backtrack as bt

def main(argc, argv):
    print("Starting the backtracking sudoko solver tests")
    
    #decide how many tests there are

    #Load the test names

    trueAnswer = [[ 0, 1], [1, 0]]

    question = [[ -1, -1], [ 1, 0]]

    #For now we are going to use just one test and its going to be hardcoded
    for test in range(1):
        solver = bt.Sudoku(2)
        answer = solver.solve(question)
        print("Solution: ", answer);
        #This is where we should validate
        
    #This is where we should show menchmarks and stuff
    
if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
