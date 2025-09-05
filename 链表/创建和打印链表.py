class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    #辅助函数根据列表来创捷链表
    def create_linked_list(self,items):
        if not items:
            return None
        head = ListNode(items[0])
        current = head
        for item in  items[1:]:
            current.next = ListNode(item)
            current = current.next
        return head

    #辅助函数打印链表
    def print_linked_list(self,head):
        current = head
        items = []
        while current:
            items.append(str(current.val))
            current = current.nex
        print("->".join(items))


