class MyQueue:
    """
    题目描述：使用两个栈实现队列的如下操作
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #将一个栈中的元素，主键递归pop到另一个栈，实现反转
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return  self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        #peek只检查，不弹出
        return self.out_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.in_stack and not self.out_stack


'''
9月21日bug日志：
1、就是关于题目思路，题目要求使用两个栈操作来实现队列，而我刚开始想的是，直接使用一个列表来实现队列操作。
2、就是在empty方法中，应该两个列表都要检查，不然会出现遗漏的情况
'''