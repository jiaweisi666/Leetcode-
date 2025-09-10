class ListNode(object):
    """链表节点"""
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def create_linked_list(items: list) -> ListNode:
    """根据列表来创建链表"""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

def print_linked_list(head: ListNode):
    """打印链表"""
    current = head
    items = []
    while current:
        items.append(str(current.val))
        current = current.next
    print(" -> ".join(items))
