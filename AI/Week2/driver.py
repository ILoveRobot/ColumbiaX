#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Solving Week 2 Assignment - n-puzzle game

Author: Bruno G. Eilliar

Notes:
    - Code for grading (everything must be on a single file)
    - 'UDLR' stands for  [‘Up’, ‘Down’, ‘Left’, ‘Right’]
    - Breadth-First Search. Enqueue in UDLR order; dequeuing results in UDLR order.
    - Depth-First Search. Push onto the stack in reverse-UDLR order; popping off results in UDLR order.
"""

import sys, ast, math, copy
DEBUG = True

######################################################
# Classes
######################################################
class State(object):
    def __init__(self, initialState):
        self.iState = initialState
        self.currentState = initialState
        self.dim = len(initialState)    # State Dimension
        self.parent = None

    def __str__(self):
        return "{}".format(self.currentState)

    def current(self):
        return self.currentState

    def parent(self, state):
        self.parent = state

    def children(self):
        child_list = []
        moves = self.get_legal_moves()
        zero = self.find(0)
        for m in moves:
            l = list(self.current())
            l[zero+m], l[zero] = l[zero], l[zero+m]
            #child_list.append(l)
            child_list.append(State(l))

        return child_list

    def get_legal_moves(self):
        moves = []
        # Size of the board
        n = math.sqrt(self.dim)
        # Find empty space position on board
        zero = self.find(0)
        # if not in row 0: can go U (pos -n)
        if not(zero <= n-1):
            moves.append(-n)
        # if not in row n-1: can go D (pos +n)
        if not(zero >= (n**2) - n):
            moves.append(+n)
        # if not in col 0: can go L (pos -1)
        if not(zero%n == 0): 
            moves.append(-1)
        # if not in col n-1: can go R (pos +1)
        if not((zero+1)%n == 0):
            moves.append(+1)

        return [int(x) for x in moves]

    def find(self, value):
        return int(self.currentState.index(value))

    def swap(self, z_index, move):
        self.currentState[z_index+move], self.currentState[z_index] = self.currentState[z_index], self.currentState[z_index+move]

class Queue(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        return "{}".format(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

######################################################
# Functions
######################################################
def goalTest(state):
    """
    """
    goal = range(0, state.dim)
    if state.current() == goal:
        return True
    else:
        return False
    
def Breadth_First_Search(initialState, goalTest, debug = False):
    """Use BFS to solve n-puzzle

    Inputs:
    - initialState ->
    - goalTest -> Function to test if the current state is the goal.
    Outputs:

    """
    frontier = Queue() # Queue.new(initialState)
    frontier.enqueue(initialState)
    explored = set()

    while not frontier.isEmpty():
        state = frontier.dequeue()
        explored.add(state)

        if goalTest(state):
            if debug:
                print("Success! Goal State: {}\nNumber of explored states: {}".format(state, len(explored)))
            return state

        for neighbor in state.children():
            test1 = neighbor.current() not in [x.current() for x in frontier.items]
            test2 = neighbor.current() not in [x.current() for x in explored]
            if (test1) and (test2):
                frontier.enqueue(neighbor)

    return -1

def solve_puzzle(solver, initialState):
    """"""
    if (solver == 'bfs'):
        Breadth_First_Search(initialState, goalTest, DEBUG)
    elif (solver == 'dfs'):
        return "Sorry"
    elif (solver == 'ast'):
        return "Sorry"
    elif (solver == 'ida'):
        return "Sorry"
    else:
        return "Wring method, choose between bsf, dfs, ast or ida solvers"

if __name__ == '__main__':
    # Get input parameters
    arg_list = sys.argv
    solver = arg_list[1]
    initial_board = list(ast.literal_eval(arg_list[2]))
    print("Method: {}\tBoard Initial State: {}".format(solver, initial_board))
    # Solve it
    state = State(initial_board)
    solve_puzzle(solver, state)
