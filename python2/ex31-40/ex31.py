class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, nodes):
        self._children.extend(nodes)
        return self

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        if len(self._children) == 0:
            print(self._value)
        for c in self:
            yield from c.depth_first()


# Example
if __name__ == '__main__':
    root = Node(None)
    root.add_child(
        list(map(lambda s: Node(s).add_child([Node('a'), Node('u')]) if s in ('S', 'T') else Node(s),
                 ['S', 'F', 'M', 'T', 'W'])))

    for ch in root.depth_first():
        pass
