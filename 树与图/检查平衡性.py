class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    题目描述：实现一个函数，检查二叉树是否平衡。
    平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。
    """
    def isBalanced(self, root:TreeNode) -> bool:
        """
        在递归调用时就检查子树，子树的子树的高度
        """
        def get_high(node) -> int:
            #递归最终终止条件
            if not node:
                return 0 #空节点高度为0
            #递归左子树
            '''
            要么返回左子树的高度值，要么返回警告信息-1
            '''
            left_high = get_high(node.left) #信任之跃
            if left_high == -1:
                return -1

            #递归右子树
            right_high = get_high(node.right)
            if right_high == -1:
                return -1

            #计算左右子树的高度差,判断是否为平衡树
            if abs(left_high - right_high) > 1:#abs()求绝对值
                return -1
            #返回高度
            return max(left_high, right_high) + 1

        #get_hige()能返回高度就说明是平衡树，返回-1说明不是
        return get_high(root) != -1

    def isBalanced_preorder(self, root: TreeNode) -> bool:
        """
        方法二：自顶向下的先序遍历 (Pre-order DFS) (效率较低)
        对每个节点，先计算其左右子树高度判断平衡，再递归检查子树。
        时间复杂度: O(N*logN) 到 O(N^2), 空间复杂度: O(H)
        """
        if not root:
            return True

        # 1. 检查当前节点是否平衡 (先序位置)
        left_height = self._get_height_helper(root.left)
        right_height = self._get_height_helper(root.right)
        if abs(left_height - right_height) > 1:
            return False

        # 2. 递归地检查左右子树是否也都平衡
        return self.isBalanced_preorder(root.left) and self.isBalanced_preorder(root.right)

    def _get_height_helper(self, node: TreeNode) -> int:
        """一个单纯用来计算高度的辅助函数"""
        if not node:
            return 0
        return 1 + max(self._get_height_helper(node.left), self._get_height_helper(node.right))




