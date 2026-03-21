class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.get_inorder(self.arr, root)
        
        self.i = 0
        self.l = len(self.arr)
    
    
    def get_inorder(self, arr, root):
        if not root:
            return
        
        
        self.get_inorder(arr, root.left)
        arr.append(root.val)
        self.get_inorder(arr, root.right)


    def next(self) -> int:
        ans = self.arr[self.i]
        self.i += 1
        return ans
    

    def hasNext(self) -> bool:
        return self.l > self.i