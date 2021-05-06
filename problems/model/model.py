class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'val={self.val}, next={self.next}'


class Node:

    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

    def __repr__(self):
        return f'Node (val={self.val}, children={self.children})'


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'[{self.val}]'
