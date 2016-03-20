#!/usr/bin/python
import copy
import numpy as np
import sys
import math

class Sudoku:
    def __init__(self, size):
        self.size = size 
        self.maxIndex = size * size

        if size %3 != 0:
            raise ValueError("Sudoku must be in sets of 3")
   
    def solve(self, matrix):
        return self.solveRec(matrix, 0)
 
    def solveRec(self, matrix, box):
    
        ##print("Continue?");
        #sys.stdin.readline()
 
        #if box > 6:
            #sys.exit()
 
        #print("\nSolving ------------")
        ##print(matrix)
        #self.show(matrix)
 
        if( self.reject(matrix)):
            #print("Rejected")
            
            return None

        if( self.accept(matrix)):
            #print("Solved")
            return matrix

        if( box >= self.maxIndex):
            #print("Stopping")
            return None

        #print("\nIterating from node")
        #self.show(matrix)
        x, y = self.getIndex(box)

        if self.isempty(matrix[x][y]) == False:
            #print("Skipping " + str(box))
            return self.solveRec(matrix, box+1)

        node = copy.deepcopy(matrix)
        for reci in range(self.size):
            i = reci+1
            node[x][y] = i
            #print("Recusing on:")
            #self.show(node)
            result = self.solveRec(node, box+1)
            if result != None:
                return result
        return None
            

    def reject(self, matrix):
        #Ensure there are no duplicates

        #Check all X
        for i in range(self.size):
            x = set()
            for j in range(self.size):
                if matrix[i][j] > 0:
                    if matrix[i][j] in x:
                        #print("Issue in the y");
                        return True
                    x.add(matrix[i][j])

        #Check all Y
        for j in range(self.size):
            y = set()
            for i in range(self.size):
                if matrix[i][j] > 0:
                    if matrix[i][j] in y:
                        #print("Issue in the x")
                        return True
                    y.add(matrix[i][j])

        #Check sets of 3
        bracketx = self.size/3
        brackety = self.size/3
        for xoff in range(3):
            for yoff in range(3):
                valid = set()
                #print("Square set ", valid, "for", xoff, yoff)
                for i in range(bracketx):
                    for j in range(bracketx):

                        indexx = xoff*bracketx+i
                        indexy = yoff*brackety+j

                        if matrix[indexx][indexy] > 0:
                            if matrix[indexx][indexy] in valid:
                                return True
                            #print("Adding parts", xoff*3+i, xoff*3+j, valid)
                            valid.add(matrix[indexx][indexy])
        
            
        return False;

    def accept(self, matrix):
        #Ensure there are no duplicates

        #Check all X
        for i in range(self.size):
            x = set()
            for j in range(self.size):
                if matrix[i][j] > 0:
                    if matrix[i][j] in x:
                        return False
                    x.add(matrix[i][j])
                else:
                    return False

        #Check all Y
        for j in range(self.size):
            y = set()
            for i in range(self.size):
                if matrix[i][j] > 0:
                    if matrix[i][j] in y:
                        return False
                    y.add(matrix[i][j])
                else:
                    return False

        #Check sets of 3
        bracketx = self.size/3
        brackety = self.size/3
        for xoff in range(3):
            for yoff in range(3):
                valid = set()
                for i in range(bracketx):
                    for j in range(brackety):
                        indexx = xoff*bracketx+i
                        indexy = yoff*brackety+j

                        if matrix[indexx][indexy] > 0:
                            if matrix[indexx][indexy] in valid:
                                return False
                            valid.add(matrix[indexx][indexy])
                        else:
                            return False
        

        return True

    def getIndex(self, index):
        return ( index / self.size, index % self.size)
            
    def isempty(self, val):
        if( val <= 0):
            return True
        return False

    def show(self, matrix):
        for i in range(self.size):
            print(matrix[i])
