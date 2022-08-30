#cheat ways naggaro
def getDepth(self, root):
    if not root:
        return 0
    leftSubtreeDepth = self.getDepth(root.left)
    rightSubtreeDepth = self.getDepth(root.right)
    return max(leftSubtreeDepth, rightSubtreeDepth) + 1


def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if root!=
    leftSubtreeDiameter = self.diameterOfBinaryTree(root.left)
    rightSubtreeDiameter = self.diameterOfBinaryTree(root.right)
    diameter = self.getDepth(root.left) + self.getDepth(root.right)
    diameter = max(diameter, max(leftSubtreeDiameter, rightSubtreeDiameter))
    return diameter