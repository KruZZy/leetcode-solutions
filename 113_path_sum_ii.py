class Solution(object):
    def pathSum(self, root, targetSum):
        return [s[::-1] for s in self.path(root, targetSum)]
    
    def path(self, root, remSum):
        if not root:
            return []
        if root.left == None and root.right == None and remSum-root.val == 0:
            return [[root.val]]

        leftCand = self.path(root.left, remSum - root.val)
        rightCand = self.path(root.right, remSum - root.val)
        
        return [sol + [root.val] for sol in leftCand + rightCand]