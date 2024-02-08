class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        rootNode = Node(nums[0], 0)
        tree = Tree(rootNode)
        for i in range(1, len(nums)):
            node = Node(nums[i], i)
            tree.insert(node)
        return tree.search(target)

class Node:
    def __init__(self, value=None, index=None, left=None, right=None) -> None:
        self.value = value
        self.index = index
        self.left = left
        self.right = right

class Tree:
    def __init__(self, rootNode=None) -> None:
        self.rootNode = rootNode
    
    def insert(self, insertNode) -> None:
        node = self.rootNode
        inserted = False
        while inserted == False:
            if insertNode.value >= node.value:
                if node.right == None:
                    node.right = insertNode
                    inserted = True
                node = node.right
            else:
                if node.left == None:
                    node.left = insertNode
                    inserted = True
                node = node.left

    def search(self, value) -> int:
        node = self.rootNode
        while node != None:
            if node.value == value:
                return node.index
            if value >= node.value:
                if node.right == None:
                    return node.index + 1
                node = node.right
            else:
                if node.left == None:
                    return node.index  
                node = node.left
    
    def inorder(self, node) -> None:
        if node != None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

test = Solution()
print(test.searchInsert([1,3,5,6], 7))