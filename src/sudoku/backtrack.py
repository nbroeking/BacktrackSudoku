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

    #Init all the variables to their default values
    def __init__(self, size):
        self.size = size 
        self.maxIndex = size * size

        if size %3 != 0:
            raise ValueError("Sudoku must be in sets of 3")
   
    #Main entry point takes a matrix and will solve it for a correct sudoku
    def solve(self, matrix):
        return self.solveRec(matrix, 0)
 
    #Recusivly solves the sudoku puzzle
    def solveRec(self, matrix, box):
    
        #If the matrix contains an invalid square then we reject the node
        #This prunes all sub states if we find an invalid state
        if( self.reject(matrix)):
            return None

        #If we found a solution then we should imidiatly return it and check nothing more
        if( self.accept(matrix)):
            return matrix
   
        #if we ran out of boxes then we didnt find a solution 
        if( box >= self.maxIndex):
            return None

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

        node = copy.deepcopy(matrix) 

        #We will do a depth first search for every state for box values 1-9
        #Once all child nodes fail for value 1 we try all child values for 2
        for i in range(1, self.size +1):
            node[x][y] = i
            
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
        for i in range(self.size):
            print(matrix[i])
