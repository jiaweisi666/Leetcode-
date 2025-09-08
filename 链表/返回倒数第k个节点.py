from 创建和打印链表 import ListNode

class SolutionN1(object):
    def kthToLast(self,head,k):
        #计算链表的长度
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        #找出倒数第k个节点
        current = head
        for i in range(length-k+1):
            if i == length-k:
                return current.val
            current = current.next


class Solution(object):
    def kthToLast(self, head: ListNode, k: int):
        """
        快慢指针法 (推荐)
        时间复杂度: O(N), 空间复杂度: O(1)
        """
        fast = head
        slow = head

        # 1. 快指针先向前移动 k 步
        for _ in range(k):
            # 这个检查可以处理 k 大于链表长度的情况
            if not fast:
                return None
            fast = fast.next

        # 2. 快慢指针一起移动，直到快指针到达链表末尾
        # 当 fast 为 None 时，slow 正好指向倒数第 k 个节点
        while fast:
            fast = fast.next
            slow = slow.next

        return slow.val





