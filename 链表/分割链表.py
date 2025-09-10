# D:/程序设计/python项目/PythonProject/链表/分割链表.py

# 方案一：使用 from ... import ... 直接导入需要的函数和类
from 创建和打印链表 import ListNode, create_linked_list, print_linked_list


class Solution(object):
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        最优解法：双链表拼接法
        创建两个虚拟头节点，分别管理“小于x”和“大于等于x”的两个子链表，最后拼接。
        """
        # 1. 创建两个虚拟头节点和对应的尾指针
        small_head = ListNode(0)
        large_head = ListNode(0)
        small_tail = small_head
        large_tail = large_head

        current = head
        while current:
            # 2. 根据节点值，将其分配到对应的子链表中
            if current.val < x:
                small_tail.next = current
                small_tail = small_tail.next
            else:
                large_tail.next = current
                large_tail = large_tail.next

            # 移动到原始链表的下一个节点
            current = current.next

        # 3. 将 "large" 链表的末尾设为 None，避免产生环
        large_tail.next = None

        # 4. 将 "small" 链表的尾部连接到 "large" 链表的头部
        small_tail.next = large_head.next

        # 5. 返回新链表的头节点
        return small_head.next
