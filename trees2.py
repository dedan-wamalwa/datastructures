
class Treenode:
    def __init__(self,data,rank):
        self.data=data
        self.rank=rank
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def print_tree(self):
        spaces="  "*self.get_level()
        prefix=spaces+ "|__" if self.parent else ""
        print(prefix+self.data+" ( "+ self.rank +" )")
        if self.children:
            for child in self.children:
                child.print_tree()
    def print_name(self):
        spaces="  "*self.get_level()
        prefix=spaces+ "|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_name()
    def print_rank(self):
        spaces="  "*self.get_level()
        prefix=spaces+ "|__" if self.parent else ""
        print(prefix+self.rank)
        if self.children:
            for child in self.children:
                child.print_rank()
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level


def build_tree():
    root = Treenode("Nilpul","CEO") #creating the root node
    # first child of root node
    chimney= Treenode("Chimney","CTO")
    # chimney's first child
    vishwa= Treenode("Vishwa","Infrastrucutre Head")
    vishwa.add_child(Treenode("Dhaval","Cloud Manager"))
    vishwa.add_child(Treenode("Abhiji","App Manager"))
    # chimney's 2nd child
    amir= Treenode("Aamir","Application head")
    # adding the children to chimney
    chimney.add_child(vishwa)
    chimney.add_child(amir)
    # second child of the root node
    gels= Treenode("Gels","HR Head")
    # adding children to Gels
    gels.add_child(Treenode("Peter","Recruitment Manager"))
    gels.add_child(Treenode("Waqas","Policy Manager"))
    # adding children to the root
    root.add_child(chimney)
    root.add_child(gels)
    return root

if __name__ =="__main__":
    root=build_tree()
    # root.print_tree()
    root.print_rank()
    root.print_name()

