class Solution(object):
    """
    题目描述：编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
    例如：输入：[1, 2, 3, 3, 2, 1] 输出：[1, 2, 3]
    """
    def removeDuplicateNodesN1(self,head):
        """方法一思路：通过一个记事本，把元素放入记事本中，如果重复就把那个节点删除"""
        if not head:
            return None
        seen =  {head.val}
        current = head
        while current.next:
            if current.next.val in seen:
                current.next = current.next.next #如果是重复节点就跳过，既将其删除
            else:
                seen.add(current.next.val) #如果不是重复节点，记录下来，移动到下一个
                current = current.next
        return head
    def removeDuplicateNodesN2(self,head):
        """
        方法二思路:这个方法不使用任何额外的数据结构，而是通过两层循环（两个指针）来实现。
        外层指针 current 遍历链表，内层指针 runner 负责检查 current 之后的所有节点，
        并移除与 current 值相同的节点。
        """
        if not head:
            return None
        current = head
        while current:
            # runner 指针从 current 开始，检查后面的所有节点
            runner = current
            while runner.next:
                if runner.next.val == current.val:
                    # 发现重复，移除 runner 的下一个节点
                    runner.next = runner.next.next
                else:
                    # 不重复，runner 正常后移
                    runner = runner.next
            # current 检查完毕，移动到下一个节点
            current = current.next

        return head
