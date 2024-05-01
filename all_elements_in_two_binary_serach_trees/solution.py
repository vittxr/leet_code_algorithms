from typing import List, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def store_in_list(self, tree: TreeNode, lst: list[int]) -> list[int]:
        if not tree:
            return lst

        lst.append(tree.val)
        self.store_in_list(tree.left, lst)
        self.store_in_list(tree.right, lst)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res: list[int] = []

        self.store_in_list(root1, res)
        self.store_in_list(root2, res)

        return sorted(res)
