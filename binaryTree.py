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
    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements=[]

        elements.append(self.data)

        if self.left:
            elements+=self.left.pre_order_traversal()

        if self.right:
            elements+=self.right.pre_order_traversal()

        return elements


    def post_order_traversal(self):
        elements=[]

        

        if self.left:
            elements+=self.left.post_order_traversal()

        if self.right:
            elements+=self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    

   
    


def build(elements):
    root=BinaryTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__=="__main__":
    elements=[1500,7,12,14,27,900,88,23]

    root=build(elements)
    print(root.in_order_traversal())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())
