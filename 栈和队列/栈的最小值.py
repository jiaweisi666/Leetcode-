class MinStack:
    """
    题目描述：请设计一个栈，除了常规栈支持的pop与push函数以外，
    还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。
    """
    def __init__(self):
        self.stack = [] #创建栈
        self.stack_index = 0 #栈顶指针

    def push(self, x: int) -> None:
        """
        将元素压入栈顶
        """
        self.stack[stack_index] = x
        self.stack_index += 1

    def pop(self) -> None:
        """
        弹出栈顶元素
        """
        self.stack_index -= 1
        return self.stack[self.stack_index]


    def min(self) -> int:



    def top(self) -> int:


    def getMin(self) -> int: