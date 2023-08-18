from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_maximum_binary_tree(nums: List[int]) -> Optional[TreeNode]:
    #ищем максимальный элемент и его индекс
    def _find_max(lst: List[int]) -> tuple:
        max_el = lst[0]
        max_i = 0
        for i in range(len(lst)):
            if lst[i] > max_el:
                max_el = lst[i]
                max_i = i
        return max_el, max_i

    if nums == []:
        return None
    else:
        find_max = _find_max(nums)
        root, root_i = find_max[0], find_max[1]
        prefix = nums[:root_i]
        suffix = nums[root_i+1:]
        return TreeNode(root, construct_maximum_binary_tree(nums=prefix),
                        construct_maximum_binary_tree(nums=suffix))

