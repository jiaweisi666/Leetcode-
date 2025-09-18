class MinStack:
    """
    题目描述：请设计一个栈，除了常规栈支持的pop与push函数以外，
    还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。
    """
    def __init__(self):
        self.stack = [] #创建主栈
        self.min_stack = [] #创建辅助栈，它的唯一任务就是在任何时刻，它的栈顶元素都保存着主栈当前状态下的最小值

    def push(self, x: int) -> None:
        """
        将元素压入栈顶
        """
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        """
        弹出栈顶元素
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def min(self) -> int:
        return self.getMin()


    def top(self) -> int:
        """
        返回主栈的栈顶元素，不弹出。
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        """
        直接返回辅助栈栈顶元素
        """
        if self.min_stack:
            return self.min_stack[-1]
        return None