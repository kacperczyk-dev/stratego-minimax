

class TreeNode(object):
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self, obj):
        obj.parent = self
        self.children.append(obj)
        return obj
