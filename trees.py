# a tree is anon-linear data structure that stores data in hierarchical form
# A tree is made up of a root, braches and leaves. Leaves are nodes with no children
# branches are nodes with children
# the basic structure is that of parent-child rltnship
# each child has one or more ancestor
# each parent has one or more descendant
# the hierarchy is based on levels, where the root node is at level 0

class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def print_tree(self):
        spaces="  "*self.get_level()
        prefix=spaces+"|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
        
def build_tree():
    # creating root
    root = Treenode("Electronics")
    # creating laptop node and its leaves
    laptop=Treenode("Laptops")
    laptop.add_child(Treenode("Macbook"))
    laptop.add_child(Treenode("Microsoft"))
    laptop.add_child(Treenode("Thinkpad"))
    # creating cellphone node and its leaves
    cellphone=Treenode("Cellphones")
    cellphone.add_child(Treenode("Iphone"))
    cellphone.add_child(Treenode("Google Pixel"))
    cellphone.add_child(Treenode("Vivo"))
    # creating TV node and its leaves
    TVs=Treenode("TV Sets")
    TVs.add_child(Treenode("Samsung"))
    TVs.add_child(Treenode("LG"))
    # adding them as children of the root
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(TVs)
    return root
if __name__=="__main__":
    root = build_tree()
    # print(root.get_level())
    root.print_tree()
    
