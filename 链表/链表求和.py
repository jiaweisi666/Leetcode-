from 创建和打印链表 import ListNode, create_linked_list, print_linked_list

class Solution(object):
    def addTwoNumbersN1(self,l1,l2):
        # 创建两个链表的游标
        current1 = l1
        current2 = l2
        #将链表中的值转换成字符串然后拼接
        s1 = ""
        while current1:
            s1 += str(current1.val)
            current1 = current1.next
        s2 = ""
        while current2:
            s2 += str(current2.val)
            current2 = current2.next
        #字符串翻转再转换成整数求和
        num1 = int(s1[::-1])
        num2 = int(s2[::-1])
        sum = num1 + num2
        #将总值转换成字符串
        str_sum = str(sum)

        #创建虚拟头结点
        head = ListNode(0)
        current = head
        #创建链表
        for i in reversed(str_sum):
            #将字符串转换成整数
            i = int(i)
            current.next = ListNode(i)
            current = current.next
        return head.next

    def addTwoNumbersN2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        最优解法：模拟“列竖式”加法
        逐位相加，并使用一个 carry 变量来处理进位。
        """
        # 创建一个虚拟头节点，这可以极大地简化头节点的处理
        dummy_head = ListNode(0)
        current = dummy_head

        # 初始化进位为 0
        carry = 0

        # p1 和 p2 作为两个链表的移动指针
        p1, p2 = l1, l2

        # 循环直到两个链表都遍历完，并且没有剩余的进位
        while p1 or p2 or carry:
            # 获取当前节点的值，如果节点不存在（链表已遍历完），则其值为 0
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            # 计算当前位的和 = 两个节点的值 + 上一位的进位
            current_sum = val1 + val2 + carry

            # 更新进位，为下一次循环做准备 (例如，15 // 10 = 1)
            carry = current_sum // 10
            # 获取当前位的值 (例如，15 % 10 = 5)
            current_digit = current_sum % 10

            # 创建新节点，并将其链接到结果链表的末尾
            current.next = ListNode(current_digit)
            current = current.next

            # 移动指针到下一个节点
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        # 虚拟头节点的下一个节点才是我们真正想要的链表的头
        return dummy_head.next

list_l1 = [7,1,6]
list_l2 = [5,9,2]
head_l1 = create_linked_list(list_l1)
head_l2 = create_linked_list(list_l2)
solution = Solution()
head_sum = solution.addTwoNumbers(head_l1,head_l2)
print_linked_list(head_sum)



