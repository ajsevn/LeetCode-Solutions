class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # Dictionary to save the cloned nodes
        cloned_nodes = {}
        
        # Recursive DFS function to clone the graph
        def clone(node):
            if node in cloned_nodes:
                return cloned_nodes[node]
            
            # Clone the current node
            copy = Node(node.val)
            cloned_nodes[node] = copy
            
            # Recursively clone all the neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            
            return copy
        
        return clone(node)

# Example usage:
# Create the original graph using the Node class
# and call Solution().cloneGraph with the reference to the starting node.
