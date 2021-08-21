class tree:

    def __init__(self,data):
        self.data=data
        self.children= []
        self.parent=None

    def add_child(self,child):
        self.children.append(child)
        child.parent = self
    def level(self):
        c=0
        p= self.parent
        while(p):
            c+=1
            p=p.parent

        return c

    def print_tree(self):
        space= " "*self.level()*5
        print(space+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


    def call_parent(self):
        print(self.parent.data)

    def siblings(self):
        sibling=self.parent.children
        for i in sibling:
            print(i.data,end=" ")

def build():
    
    root=tree("car")

   
    car1=tree("car1")
    car1.add_child(tree("car11"))
    car1.add_child(tree("car12"))

    car2=tree("car2")
    car2.add_child(tree("car21"))
    car2.add_child(tree("car22"))


    car3=tree("car3")
    car3.add_child(tree("car23"))

    root.add_child((car1))
    root.add_child((car2))
    root.add_child((car3))

    root.print_tree()
    car1.call_parent()
    car1.siblings()




if __name__ == "__main__":

    build()
    
    
    
    