#!/usr/bin/python
# Written By: Nicolas C. Broeking
# File: backtrack.py
# Description: This file contains the class that is used to solve sudoku
#   solve is the main entry point.

import copy
import numpy as np
import sys
import math

class Sudoku:

    def __init__(self, debug = False, inputlen = 0):
        self.debug = debug
        self.inputlen = inputlen

    def solve(self, matrix, origSize):
        self.innerSize = int(math.sqrt(origSize))
        self.size = origSize
        self.found = 0
        self.maxIndex = self.size * self.size

        return self.solveRec(matrix, 0)
 
    #Recusivly solves the sudoku puzzle
    def solveRec(self, matrix, box):
  
        #self.percentage(matrix)
         
        if self.debug and self.inputlen != 0 and box > self.inputlen:
            print "Continue?"
            sys.stdin.readline()

        if self.debug:
            print "Trying to reject"
        
        #If the matrix contains an invalid square then we reject the node
        #This prunes all sub states if we find an invalid state
        if( self.reject(matrix)):
            return None

        if self.debug:
            print "Trying to accept"

        #If we found a solution then we should imidiatly return it and check nothing more
        if( self.accept(matrix)):
            return matrix
   
        if self.debug:
            print "checking boxes"

        #if we ran out of boxes then we didnt find a solution 
        if( box >= self.maxIndex):
            return None

        if self.debug:
            print "get index"

        #The index of the box that we are now iterating values of
        x, y = self.getIndex(box)

        
        
        #If we found a box that already has a value then it is a fixed value and we need to ignore it
        if self.isempty(matrix[x][y]) == False:
            #print("Skipping " + str(box))
            
            return self.solveRec(matrix, box+1)

        #We found a new valid state now we need to check all child states recursivly
        
        #Deep copy the graph so we can pop out and use previous nodes
        #without this step every iteration we loose the previous states because python just loves 
        #pointers so much

        if self.debug:
            print "Attempting to deepcopy"
        node = copy.deepcopy(matrix) 
        #node = matrix
        if self.debug:
            print "attempting to loop"
        
        #We will do a depth first search for every state for box values 1-9
        #Once all child nodes fail for value 1 we try all child values for 2
        for i in range(1, self.size +1):
            node[x][y] = i
 
            if self.debug:
                print "In box " + str(box) + " trying val " + str(i)
                self.show(node)
            
            #Depth first search
            result = self.solveRec(node, box+1)
    
            #if we found a result then we want to return it
            if result != None:
                return result
        #but we probably didnt so if we get none then we want to backtrack and try other states
        return None
            

    #Reject checks to see if any states are invalid
    #If they are then we want to imidiatly return true
    #If there is nothing wrong with the state we return false
    #Matching the form of n^2 * n^2
    def reject(self, matrix):
        
        #Check that for each row there are no duplicate values
        for i in range(self.size):
            x = set()
            for j in range(self.size):
                if matrix[i][j] > 0:
                    if matrix[i][j] in x:
                        #print("Issue in the y");
                        return True
                    x.add(matrix[i][j])

        #Check that for each column there are no duplicate values
        for j in range(self.size):
            y = set()
            for i in range(self.size):
                if matrix[i][j] > 0:
                    if matrix[i][j] in y:
                        #print("Issue in the x")
                        return True
                    y.add(matrix[i][j])

        #Each 3rd of the grid should not have any duplicate values
        #Check the n^2 x n^2
        for xoff in range(self.innerSize):
            for yoff in range(self.innerSize):
                valid = set()
                #print("Square set ", valid, "for", xoff, yoff)
                for i in range(self.innerSize):
                    for j in range(self.innerSize):

                        indexx = xoff*self.innerSize+i
                        indexy = yoff*self.innerSize+j

                        if matrix[indexx][indexy] > 0:
                            if matrix[indexx][indexy] in valid:
                                return True
                            #print("Adding parts", xoff*3+i, xoff*3+j, valid)
                            valid.add(matrix[indexx][indexy])
        return False;

    #We can accept a node if all values are filled in and there are no duplicates
    def accept(self, matrix):

        #ensure that no row has no duplicates and that every value is filled in
        for i in range(self.size):
            x = set()
            for j in range(self.size):
                if matrix[i][j] > 0:
                    if matrix[i][j] in x:
                        return False
                    x.add(matrix[i][j])
                else:
                    return False

        #ensure that every column has no duplicates and that every value is filled in
        for j in range(self.size):
            y = set()
            for i in range(self.size):
                if matrix[i][j] > 0:
                    if matrix[i][j] in y:
                        return False
                    y.add(matrix[i][j])
                else:
                    return False

        #Ensure that every 3rd is fully filled in without duplicates

        for xoff in range(self.innerSize):
            for yoff in range(self.innerSize):
                valid = set()
                for i in range(self.innerSize):
                    for j in range(self.innerSize):
                        indexx = xoff*self.innerSize+i
                        indexy = yoff*self.innerSize+j

                        if matrix[indexx][indexy] > 0:
                            if matrix[indexx][indexy] in valid:
                                return False
                            valid.add(matrix[indexx][indexy])
                        else:
                            return False
        return True

    #converts the index ie 64->0 to the x,y cordinate of the matrix
    #box 63 gets converted to [8][8]
    def getIndex(self, index):
        return ( index / self.size, index % self.size)
    
    #If the value in the matrix is 0 then it is not filled in yet
    def isempty(self, val):
        if( val <= 0):
            return True
        return False

    #Print the sudoko matrix
    def show(self, matrix):
        for i in range(len(matrix)):
            print(matrix[i])

    def percentage(self, matrix):
        found = 0;
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j]:
                    found+=1;
        
        if found > self.found:
            print("Found = " + str(found))
            self.show(matrix)
            self.found = found
