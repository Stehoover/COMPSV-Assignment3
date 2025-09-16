# Implement your Node class here
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<Node data={self.data}>"