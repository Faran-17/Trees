"""Below is the code implementation of a basic tree"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self  # inheriting the parent property
        self.children.append(child)

    def get_level(self):  # For leveling of the tree in hierarchical manner
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent   # Recursion function

        return level

    def print_tree(self):  # function for printing the tree in proper structure
        spaces = '   ' * self.get_level()  # Getting the level of the node and adding space according to levels
        prefix = spaces + "|__" if self.parent else ""  # if-else is used so that leaf node should'nt have |__
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()      # Recursion to print the children of children


def build_product_tree():
    root = TreeNode("Electronics")  # This is the root node

    laptop = TreeNode("Laptops")   # Child 1 of root node
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))   # Children of laptop node
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phones")   # Child 2 of root node
    cellphone.add_child(TreeNode("IPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))  # Children of cellphone node
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")   # Child 3 of root node
    tv.add_child(TreeNode("Samsung"))  # Children of tv node
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    # print(root.get_level())
    root.print_tree()
    pass
