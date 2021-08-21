class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left= None
        self.right=None



    def add_child(self,data):
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinaryTree(data)
        elif data>self.data:
            if self.right:
                self.right.add_child(data)

            else:
                self.right=BinaryTree(data)
        else :
            return

   
    


def build(elements):
    root=BinaryTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__=="__main__":
    elements=[1500,7,12,14,27,900,88,23]

    root=build(elements)
    
