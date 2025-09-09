"""
题目描述：若链表中的某个节点，既不是链表头节点，也不是链表尾节点，则称其为该链表的「中间节点」。
假定已知链表的某一个中间节点，请实现一种算法，将该节点从链表中删除。
核心：非头尾节点
"""
#解题思路：从当前节点向后溯源
class Solution(object):
    def deleteNode(self,Node):
        Node.val = Node.next.val
        Node.next = Node.next.next