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

    def sum_all(self):
        sum=0 
        if self.data:
            sum=sum+self.data
        if self.left:
            sum+=self.left.sum_all()
        if self.right:
            sum+=self.right.sum_all()
        return sum


    def max_element(self):
        max=0
        left=0
        right=0
        if self.data:
            if self.data>max:
                max=self.data
        
        if self.right:
            if self.right.max_element()>max:
                max=self.right.max_element()

        return max

    def min_element(self):
        min=self.data
        
        if self.data:
            if self.data<min:
                min=self.data
        if self.left:
            if self.left.min_element()<min:
                min=self.left.min_element()

        return min
    def delete_node(self,val):
        if val<self.data:
            if self.left:
                self.left.delete_node(val)
        elif val>self.data:
            if self.right:
                self.right.delete_node()

        else:
            if self.left and self.right is None:
                return self.data
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
        


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
    print(root.sum_all())
    print(root.max_element())
    print(root.min_element())
