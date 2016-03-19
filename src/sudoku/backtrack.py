#!/usr/bin/python
import copy
import numpy as np
import sys
import math

class Sudoku:
    def __init__(self, size):
        self.size = size 
        self.maxIndex = size * size
   
    def solve(self, matrix):
        return self.solveRec(matrix, self.maxIndex -1)
 
    def solveRec(self, matrix, box):
         
        if( self.reject(matrix)):
            return None

        if( self.accept(matrix)):
            return node

        x, y = self.getIndex(box)

        print("Checking x, y" , x , y)

        if self.isempty(matrix[x][y]) == False:
            return solveRec(matrix, box-1)

        node = copy.deepcopy(matrix)
        for i in range(self.size):
            node[x][y] = i
            if solveRec(node, box-1):
                return node
        return None
            

    def reject(self, matrix):
        #Ensure there are no duplicates
        return False;

    def accept(self, matrix):
        return False

    def getIndex(self, index):
        return ( index / self.size, index % self.size)
            
    def isempty(self, val):
        if( val <= 0):
            return True
        return False
