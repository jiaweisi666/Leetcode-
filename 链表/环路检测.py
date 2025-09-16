class Solution(object):
    """
    题目描述：给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。
    若环不存在，请返回 null。
    """
    def detectCycle(self, head):
        """
        解法一：哈希集合法
        将链表的地址存储在集合中，然后再进行比较
        """
        nodes_site = set()
        current = head
        while current:
            if current in nodes_site:
                return current
            nodes_site.add(current)
            current = current.next
        return None

    def detectCycle(self, head: ListNode):
        """
        最优解法：快慢指针法
        时间复杂度: O(N), 空间复杂度: O(1)
        """
        # 步骤1: 使用快慢指针判断是否存在环
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                # 环存在，跳出循环，此时 slow 和 fast 在环中某点相遇
                break
        else:
            # 如果循环是正常结束的 (fast 走到了链表末尾)，说明无环
            return None

        # 步骤2: 寻找环的入口节点
        # 将一个指针放回链表头部
        ptr1 = head
        # 另一个指针保持在相遇点
        ptr2 = slow

        # 两个指针同时以相同速度前进，它们再次相遇的地方就是环的入口
        while ptr1 is not ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1