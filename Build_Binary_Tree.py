# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        # The last element in postorder is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # Find the index of the root in inorder array
        inorder_index = inorder.index(root_val)

        # Build the right subtree first because we are reducing postorder from the end
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)

        return root

# Example usage:
# You can test the function with example inputs.
solution = Solution()
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = solution.buildTree(inorder, postorder)

def print_tree(node):
    if not node:
        return "null"
    left = print_tree(node.left)
    right = print_tree(node.right)
    return f"{node.val}, {left}, {right}"

print(print_tree(root))  # Output should be: "3, 9, null, null, 20, 15, null, null, 7, null, null"
