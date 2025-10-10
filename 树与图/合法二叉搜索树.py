class TreeNode:
    """
    二叉节点数的定义
    """
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    """
    题目描述：实现一个函数，检查一棵二叉树是否为二叉搜索树
    """
    def isValidBST_inorder_list(self, root: TreeNode) -> bool:
        """
        方法一：中序遍历 + 列表判断
        时间复杂度: O(N), 空间复杂度: O(N)
        """
        node_storage = []
        def get_node(node) -> None:
            if not node:
                return
            get_node(node.left)
            node_storage.append(node.val)
            get_node(node.right)

        get_node(root)
        # 检查中序遍历的结果是否严格递增
        return all(a<b for a,b in zip(node_storage, node_storage[1:]))

    def isValidBST_inorder_optimized(self, root: TreeNode) -> bool:
        """
        方法二：中序遍历 + 记录前驱节点
        在遍历过程中进行比较，避免存储整个列表。
        时间复杂度: O(N), 空间复杂度: O(H) (H是树的高度)
        """
        self.prev_val = float('-inf') # 初始化前一个值为负无穷

        def is_increasing(node: TreeNode) -> bool:
            if not node:
                return True
            
            # 1. 递归检查左子树
            if not is_increasing(node.left):
                return False
            
            # 2. 检查当前节点
            if node.val <= self.prev_val:
                return False
            self.prev_val = node.val # 更新前一个值为当前节点值
            
            # 3. 递归检查右子树
            return is_increasing(node.right)

        return is_increasing(root)

    def isValidBST(self, root: TreeNode) -> bool:
        """
        最优解法：递归定义法 + 传递上下界
        时间复杂度: O(N), 空间复杂度: O(H) (H是树的高度)
        """
        def is_valid(node, lower=float('-inf'), upper=float('inf')) -> bool:
            # 递归终止条件：空树是合法的
            if not node:
                return True
            
            # 检查当前节点的值是否在合法范围内
            if not (lower < node.val < upper):
                return False
            
            # 递归检查左右子树，并收紧范围
            # 左子树的上限是当前节点的值
            # 右子树的下限是当前节点的值
            return (is_valid(node.left, lower, node.val) and
                    is_valid(node.right, node.val, upper))
        
        return is_valid(root)
