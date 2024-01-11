from manim import *

class BinaryTree(Scene):
    def construct(self):
        tree = self.create_binary_tree()
        self.play(Create(tree))

    def create_binary_tree(self):
        nodes = [TreeNode(str(i)) for i in range(7)]

        # Set positions for each node
        nodes[0].shift(2*UP)

        nodes[1].shift(2*LEFT)
        nodes[3].shift(3*LEFT + DOWN)
        nodes[4].shift(DOWN - RIGHT)


        nodes[2].shift(2*RIGHT)
        nodes[5].shift(DOWN - LEFT)
        nodes[6].shift(3*RIGHT + DOWN)

        # Connect nodes to create edges
        edges = [
            (0, 1),
            (0, 2),
            (1, 3),
            (1, 4),
            (2, 5),
            (2, 6)
        ]

        # Create tree
        tree = VGroup(*nodes)
        for edge in edges:
            tree.add(self.connect_nodes(nodes[edge[0]], nodes[edge[1]]))

        return tree

    def connect_nodes(self, node1, node2):
        return Line(node1.get_center(), node2.get_center(), buff=0.1)

class TreeNode(Tex):
    def __init__(self, label, **kwargs):
        super().__init__(label,**kwargs)

