
class Treenode:
    def __init__(self,name,rank):
        self.name=name
        self.rank=rank
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def print_tree(self,data):
        data=str(data).lower()
        spaces="  "*self.get_level()
        prefix=spaces+ "|__" if self.parent else ""
        if data=="name":
            print(prefix+self.name)
        elif data== "designation":
            print(prefix+self.rank)
        else:
            print(prefix+self.name+" ( "+ self.rank +" )")
        if self.children:
            for child in self.children:
                child.print_tree(data)
    def print_upto_level(self,level):
        spaces="  "*self.get_level()
        prefix=spaces+ "|__" if self.parent else ""  
        print(prefix+self.name+" ( "+ self.rank +" )")
        if self.children:
            for child in self.children:
                if child.get_level()>level:
                    break
                else:
                    child.print_upto_level(level)
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
    # root.print_tree("name")
    # root.print_tree("designation")
    root.print_tree("both")
    root.print_upto_level(1)

