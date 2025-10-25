class TreeNode:
    """Definition for a binary tree node"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    题目描述：设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。
    不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。（最近公共祖先节点可以为节点本身）
    """
    def lowestCommonAncestorN1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''找出二叉树中两个节点的最近祖先节点'''
        # 使用一个实例变量来存储最终答案
        self.ans = None
        def dfs(node:TreeNode)->bool:
            '''返回一个bool值，告诉上层调用：在以node为根的子树中，是否找到了p或q'''
            if node is None:
                return False

            #检查左右子树是否包含p或q
            left_found = dfs(node.left)
            right_found = dfs(node.right)
            #检查当前节点是否是p或q
            mid_found = (node is p) or (node is q)

            #汇总检查当前节点是否为祖先节点
            if left_found + right_found + mid_found == 2:
                self.ans = node

            #向上层汇报：有一个True就说明找到了目标之一
            return left_found or right_found or mid_found

        dfs(root)
        return self.ans


    def lowestCommonAncestorN2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        最优解法：递归 (后序遍历思想)，直接通过返回值传递节点。
        时间复杂度: O(N), 空间复杂度: O(H) (H是树的高度)
        """
        # 1. 递归的终止条件
        if root is None:
            return None
        # 如果当前节点是 p 或 q，它就是其自身子树中能找到的最重要节点
        if root is p or root is q:
            return root

        # 2. 递归“甩锅”给左右孩子
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # 3. 根据左右子树的返回结果，在当前节点做决策
        # 情况一：p 和 q 分别在左右子树，那么当前 root 就是 LCA
        if left_lca and right_lca:
            return root

        # 情况二：p 和 q 都在左子树或右子树中，或者其中一个还没找到
        # 此时，只需返回那个非 None 的结果即可。
        # 如果两边都返回 None，这里也会正确地返回 None。
        return left_lca if left_lca is not None else right_lca


