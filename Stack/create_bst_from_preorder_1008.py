from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_bst_from_preorder(preorder: List[int]) -> Optional[TreeNode]:
    if preorder == []:
        return None
    else:
        head = preorder[0]
        i = 1
        while i != len(preorder) and preorder[i] < head:
            i += 1
        left = preorder[1:i]
        right = preorder[i:]
        return TreeNode(head, create_bst_from_preorder(left), create_bst_from_preorder(right))

