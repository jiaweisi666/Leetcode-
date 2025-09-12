class Solution(object):
    """
    题目描述：请编写一个函数，检查链表是否为回文。
    """
    def isPalindromeN1(self, head):
        """
        解法一：将链表转换为列表，通过列表的切片来判断是否为回文
        缺点：用到了额外的内存空间。
        时间复杂度为 O(N)，空间复杂度为 O(N)
        """
        current = head
        values = []
        while current:
            values.append(current.val)
            current = current.next
        return values == values[::-1]

    def isPalindrome(self, head: ListNode) -> bool:
        """
        解法二：快慢指针法：慢指针每次走一步，快指针每次走两步，当快指针走到末尾，慢指针刚好走到中间。
        然后再将后面翻转比较，最后再翻转回来。
        时间复杂度O(N),空间复杂度O(1)
        """
        if not head or not head.next:
            return True

        # 1. 使用快慢指针找到链表的中间节点
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 反转链表的后半部分
        # slow 现在指向后半部分的头节点
        second_half_head = self._reverse_list(slow)

        # 3. 比较前半部分和反转后的后半部分
        first_half_head = head
        result = True
        # 使用 second_half_head 作为循环条件，因为会先到达链表结尾
        while result and second_half_head:
            if first_half_head.val != second_half_head.val:
                result = False
            first_half_head = first_half_head.next
            second_half_head = second_half_head.next

        # 4. (可选，但好习惯) 恢复原始链表结构
        self._reverse_list(slow)  # 再次反转后半部分即可恢复

        return result

    def _reverse_list(self, head: ListNode) -> ListNode:
        """辅助函数：反转一个链表"""
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev