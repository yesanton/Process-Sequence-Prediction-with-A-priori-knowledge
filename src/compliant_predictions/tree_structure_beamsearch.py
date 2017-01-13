'''
this file is to build the data structure for beam search

Author: Anton Yeshchenko
'''


class Node_status():
    discovered, closed = range(2)

class MultileafTree():
    def __init__(self, depth, data, cropped_line, total_predicted_time, parent = None):
        self.descendants = [None] * depth
        # parent node for backtracking
        self.parent = parent

        self.data = data
        self.node_status = Node_status.discovered

        self.cropped_line = cropped_line
        self.total_predicted_time = total_predicted_time


    #this function will backtrack in the tree until finds the non-closed node
    def choose_next_top_descendant(self):
        #we can close the node, because we always move forward,
        #and when backtracking starts we wont need any already visited nodes
        self.node_status = Node_status.closed

        for i in range(len(self.descendants)):
            if self.descendants[i] != None:
                if self.descendants[i].node_status == Node_status.discovered:
                    return self.descendants[i]
        if self.parent != None:
            return self.parent.choose_next_top_descendant()
        else:
            return None

