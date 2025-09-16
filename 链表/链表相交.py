class Solution(object):
    """
    题目描述：编写一个程序，找到两个单链表相交的起始节点。
    """
    def getIntersectionNodeN1(self, headA, headB):
        """
        方法一：哈希集合法
        将一个链表的节点存入哈希集合，然后遍历另一个链表检查节点是否存在。
        时间复杂度: O(M + N), 空间复杂度: O(N)
        """
        nodes_in_A = set()  # 创建集合，可以快速判断节点是否存在
        current_A = headA
        while current_A:
            nodes_in_A.add(current_A)
            current_A = current_A.next

        current_B = headB
        while current_B:
            if current_B in nodes_in_A:
                return current_B
            current_B = current_B.next
        return None

    def getIntersectionNodeN2(self, headA, headB):
        """
        最优解法：双指针法
        让两个指针分别走完两个链表，它们走过的总路程相等，若有交点则必定相遇。
        时间复杂度: O(M + N), 空间复杂度: O(1)
        """
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA is not pB: #is not 判断内存地址是否相同
            # 如果 pA 走到头，就让他去走链表 B；否则，走一步
            pA = pA.next if pA else headB
            # 如果 pB 走到头，就让他去走链表 A；否则，走一步
            pB = pB.next if pB else headA
        # 循环结束时，pA 和 pB 要么在交点相遇，要么都为 None
        return pA


