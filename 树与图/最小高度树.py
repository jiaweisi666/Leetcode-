class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    题目描述：给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。
    """
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        # 1. 递归的终止条件
        # 如果数组是空的，说明这里没有节点，返回 None
        if not nums:
            return None

        # 2. 找到中间元素作为根节点
        mid_index = len(nums) // 2
        root = TreeNode(nums[mid_index])

        # 3. 递归地构建左子树
        root.left = self.sortedArrayToBST(nums[:mid_index])

        # 4. 递归地构建右子树
        root.right = self.sortedArrayToBST(nums[mid_index + 1:])

        # 5. 返回当前构建好的（子）树的根节点
        return root