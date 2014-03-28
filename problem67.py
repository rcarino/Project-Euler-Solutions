__author__ = 'rcarino'

def make_tree(txt):
    unparsed = txt.strip().split('\n')
    tree = TreeNode(int(unparsed.pop(0)))
    parents = [tree]
    while unparsed:
        current = [int(s) for s in unparsed.pop(0).split(' ')]
        parent = parents[0]
        left = TreeNode(current.pop(0), parent=parent)
        right = TreeNode(current.pop(0), parent=parent)
        parent.left = left
        parent.right = right
        new_parents = [left, right]
        while current:
            parents.pop(0)
            parent = parents[0]
            left = right
            left.parents += [parent]
            right = TreeNode(current.pop(0), parent=parent)
            parent.left = left
            parent.right = right
            new_parents.append(right)
        parents = new_parents
    return tree



class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.parents = []
        if parent:
            self.parents += [parent]
        self.val = val
        self.left = left
        self.right = right

    def max_path(self):
        # BFS to set max_paths for node
        queue = [self]
        while queue:
            cur = queue.pop(0)
            prev_maxes = [parent.max_path for parent in cur.parents]
            prev_max = max(prev_maxes) if prev_maxes else 0
            cur.max_path = cur.val + prev_max
            for child in [cur.left, cur.right]:
                if child and child not in queue:
                    queue.append(child)
        # BFS again to get the max path
        max_path = 0
        queue = [self]
        while queue:
            cur = queue.pop(0)
            max_path = max(max_path, cur.max_path)
            for child in [cur.left, cur.right]:
                if child and child not in queue:
                    queue.append(child)
        return max_path

with open("triangle.txt") as f:
    content = f.read()
    t = make_tree(content)
    print t.max_path()