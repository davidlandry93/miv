#!/usr/share/env python

import inspect
import functools
import vim_commands

allCommands = inspect.getmembers(vim_commands, inspect.isfunction)

class VimBuffer:
    """ A bunch of text with a position. """
    
    def __init__(self, text, position):
        self.text = text
        self.position = position

@functools.total_ordering
class CommandTreeNode:
    """ A single node of the command tree we build to retrieve 
    the movement command. """

    def __init__(self, vimBuffer, parent, command, target):
        """ vimBuffer: the buffer state.
        parent: The node we started from to create this one.
        command: The command we used to reach that state.
        target: The selection we are aiming for.
        """
        self.vimBuffer = vimBuffer
        self.parent = parent
        self.children = []
        self.command = command
        self.target = target

    def __eq__(self, other):
        return (approx_distance(self.vimBuffer.text, self.vimBuffer.position, self.target[1]) ==
                approx_distance(other.vimBuffer.text, other.vimBuffer.position, self.target[1])) 

    def __lt__(self, other):
        return (approx_distance(self.vimBuffer.text, self.vimBuffer.position, self.target[1]) <
                approx_distance(self.vimBuffer.text, other.vimBuffer.position, self.target[1])) 

    def add_child(self, child):
        self.children.append(child)
        self.children.sort()

    def rebuild_solution(self):
        commandSequence = []
        cursor = self
        while(cursor.parent != None):
            commandSequence.insert(0, cursor.command)
            cursor = cursor.parent
        return commandSequence
        

def approx_distance(text, position1, position2):
    distance = 0
    # Check if the first position is further than the second position.
    if(position1[0] > position2[0] or
            (position1[0] == position2[0] and 
                position1[1] > position2[1])):
        position1, position2 = position2, position1
    line, col = position1
    while((line, col) != position2):
        if(col <= len(text[line])):
            distance = distance + 1
            col = col + 1
        else:
            distance = distance + 1
            line = line + 1
            col = 0
    return distance

def explore_node(node):
    for command in allCommands:
        name, f = command
        print("Trying command: " + name)
        newNode = CommandTreeNode(f(node.vimBuffer), node, name, node.target)
        node.add_child(newNode)
    print(node.children)

def reverse_engineer_rec(node, solutionsSoFar):
    if(node.vimBuffer.position == node.target):
        return node.rebuildSolution
    else:
        explore_node(node)
        for child_node in node.children:
            if (approx_distance(
                        child_node.vimBuffer.text,
                        child_node.vimBuffer.position, 
                        node.target[1]
                        ) < 
                    approx_distance(
                        node.vimBuffer.text, 
                        node.vimBuffer.position, 
                        node.target[1]
                        )
                ):
                solutionsSoFar.append(
                        reverse_engineer_rec(child_node, solutionsSoFar)
                        )

def reverse_engineer(textBuffer, target): 
    solutions = []
    rootNode = CommandTreeNode(textBuffer, None, None, target)
    reverse_engineer_rec(rootNode, solutions)
    return solutions
