class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    """
    题目描述：设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）
    如果指定节点没有对应的“下一个”节点，则返回null。
    """
    def inorderSuccessorN1(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        方法一：将二叉搜索树中序遍历进一个列表中，输出列表中指定节点的下一个节点
        """
        #将二叉树中序遍历进列表
        node_storage = []
        def get_node(node) -> None:
            if not node:
                return
            get_node(node.left)
            node_storage.append(node) # 存入节点对象
            get_node(node.right)
        get_node(root)
        #返回列表中指定节点的下一个节点
        try:
            index = node_storage.index(p)
            if index < len(node_storage) - 1:
                return node_storage[index + 1]
            else:
                # 如果是最后一个元素返回None
                return None
        except ValueError:
            # 如果 p 不在树中
            return None

    def inorderSuccessorN2(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        方法二：优化的中序遍历
        在遍历过程中实时寻找，无需存储整个列表。
        时间复杂度: O(N), 空间复杂度: O(H) (H是树的高度)
        """
        # 使用一个标志位来记录是否已经找到了节点 p
        self.found_p = False
        # 用来存储最终结果
        self.successor = None

        def inorder_traverse(node):
            if not node:
                return

            # 1. 递归遍历左子树
            inorder_traverse(node.left)

            # 如果已经找到了后继者，就没必要再继续遍历了
            if self.successor:
                return

            # 2. 处理当前节点 (中序遍历的“根”部)
            # 如果上一个节点是 p，那么当前节点就是我们要找的后继者
            if self.found_p:
                self.successor = node
                # 标记为 False 防止重复赋值，并可以提前结束
                self.found_p = False
                return

            # 检查当前节点是否是 p
            if node is p:
                self.found_p = True

            # 3. 递归遍历右子树
            inorder_traverse(node.right)

        inorder_traverse(root)
        return self.successor

    def inorderSuccessorN3(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        最优解法：利用二叉搜索树的特性
        时间复杂度: O(H), 空间复杂度: O(1)
        """
        # 情况1：如果 p 有右子树，后继者是右子树中的最小节点
        if p.right:
            current = p.right
            while current.left:
                current = current.left
            return current

        # 情况2：如果 p 没有右子树，后继者是它的某个祖先
        # 从根节点开始查找，最后一个比 p.val 大的节点就是后继者
        successor = None
        current = root
        while current:
            if current.val > p.val:
                successor = current  # 这个节点可能是后继者，先记下来
                current = current.left  # 去左边找更小的
            else:
                # 如果当前节点小于或等于p，后继者一定在右边
                current = current.right
        return successor