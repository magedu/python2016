from stack import Stack
from queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node):
        self.root = node

    def add_left(self, tree):
        self.root.left = tree

    def add_right(self, tree):
        self.root.right = tree

    @property
    def left(self):
        return self.root.left

    @property
    def right(self):
        return self.root.right

    def visit_first(self, fn):
        fn(self.root.value)
        if self.left:
            self.left.visit_first(fn)
        if self.right:
            self.right.visit_first(fn)

    def visit_middle(self, fn):
        if self.left:
            self.left.visit_middle(fn)
        fn(self.root.value)
        if self.right:
            self.right.visit_middle(fn)

    def visit_last(self, fn):
        if self.left:
            self.left.visit_last(fn)
        if self.right:
            self.right.visit_last(fn)
        fn(self.root.value)

    def iter_visit_first(self, fn):
        stack = Stack()
        stack.push(self)
        while stack.top:
            p = stack.pop()
            fn(p.root.value)
            if p.right:
                stack.push(p.right)
            if p.left:
                stack.push(p.left)

    def visit_level(self, fn):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            p = queue.get()
            fn(p.root.value)
            if p.left:
                queue.put(p.left)
            if p.right:
                queue.put(p.right)


if __name__ == '__main__':
    d = Tree(Node('D'))
    e = Tree(Node('E'))
    b = Tree(Node('B'))
    b.add_left(d)
    b.add_right(e)
    f = Tree(Node('F'))
    g = Tree(Node('G'))
    c = Tree(Node('C'))
    c.add_left(f)
    c.add_right(g)
    a = Tree(Node('A'))
    a.add_left(b)
    a.add_right(c)

    from functools import partial
    p = partial(print, end='')
    a.visit_first(p)
    print()
    a.iter_visit_first(p)
    print()
    a.visit_middle(p)
    print()
    a.visit_last(p)
    print()
    a.visit_level(p)

#TODO 中序、后序便利的非第归方法

# ABDECFG first
# DBEAFCG middle
# DEBFGCA last

# ABCDEFG