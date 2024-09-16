class Node:
    def __repr__(self):
        return f"Data: {self.data}" 
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __repr__(self):
        return f"Tree: {self.in_order()}"
    
    def __init__(self):
        self.root = None
    
    def insert(self, data): 
        #Add a value to the correct position in the binary tree

        if self.root == None:
            self.root = Node(data)
        else:
            current = self.root
            parent = None

            while current:
                parent = current
                if data < current.data:
                    current = current.left
                else:
                    current = current.right

            if data < parent.data:
                parent.left = Node(data)
            else:
                parent.right = Node(data)

    def remove(self, target):
        #Remove a value in the binary tree
        #Throw error if value not in tree

        if not self.has(target):
            raise Exception("Can't remove non-existent value")
        
        if self.root.data == target:
            self.root = None
        else:
            current = self.root
            parent = None

            while current.data != target:
                parent = current
                if target < current.data:
                    current = current.left
                else:
                    current = current.right

            if target < parent.data:
                parent.left = None
            else:
                parent.right = None

    def in_order(self):
        #Returns a list of the values in the tree, 
        #sorted in ascending order. 

        current = self.root
        stack = []
        result = []

        while current or stack:
            while current != None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.data)

            current = current.right

        return result

    def has(self, target): 
        #Verify if the item exists in the tree
            
        current = self.root

        while current:
            if target == current.data:
                return True
            elif target < current.data:
                current = current.left
            else:
                current = current.right
        return False

tree = Binary_Tree()

tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

print("In-order traversal:", tree.in_order())

print("Remove node 60")
tree.remove(60)
print("After removing 60:", tree.in_order())
print("Verifying removed node (60):", tree.has(60))

print("Insert node 60")
tree.insert(60)
print("After inserting 60:", tree.in_order())
print("Verifying removed node (60):", tree.has(60))
