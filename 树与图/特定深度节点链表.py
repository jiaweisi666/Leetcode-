class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import collections
class Solution:
    """
    题目描述：给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表，
    将这些链表的头结点存到一个数组中并返回。
    """
    def listOfDepthN1(self, tree):
        """
        方法一：广度优先遍历
        """
        #创建一个列表，里面装载的是各层链表的头结点
        finally_list = []
        deque = collections.deque([tree])

        while deque:
            #按层处理，并为当前层创建头节点
            layer_number = len(deque) #每层节点数
            head = ListNode()
            current = head

            for _ in range(layer_number):
                tree_node = deque.popleft()
                current.next = ListNode(tree_node.val)
                current = current.next
                #将下一层存储到队列中
                if tree_node.left: deque.append(tree_node.left)
                if tree_node.right: deque.append(tree_node.right)
            #将链表头存储到列表中
            head = head.next
            finally_list.append(head)

        #返回列表
        return finally_list

    def listOfDepthN2(self, tree: TreeNode) -> list[ListNode]:
        """
        方法二：深度优先搜索 (DFS) + 层级参数
        时间复杂度: O(N), 空间复杂度: O(H) (H是树的高度，递归栈的深度)
        """
        res = []

        def dfs(node: TreeNode, level: int):
            if not node:
                return

            # 如果是第一次到达这个层级
            if level == len(res):
                # 创建一个新的链表头
                res.append(ListNode(node.val))
            else:
                # 在现有链表的头部插入新节点
                # (因为我们先遍历右边，所以每次都在头部插入，最后顺序就是对的)
                new_head = ListNode(node.val)
                new_head.next = res[level]
                res[level] = new_head

            # 先遍历右子树，再遍历左子树
            # 这样可以保证我们是从右往左构建每一层的链表
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(tree, 0)
        return res



        
