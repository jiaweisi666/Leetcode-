class SortedStack:
    """
    题目描述：栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，
    但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。
    当栈为空时，peek 返回 -1。
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        """
        将元素压入栈顶，再使用冒泡排序
        """
        self.stack.append(val)
        #通过i从后往前依次取元素下标来实现冒泡排序，但该解法有点问题，
        # 因为我们把栈当作一个数组来处理是不符合题目要求的
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i]  > self.stack[i-1]:
                #交换位置，python简洁表示法
                self.stack[i], self.stack[i-1] = self.stack[i-1], self.stack[i]

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def isEmpty(self) -> bool:
        return not self.stack

    def push2(self, val: int) -> None:
        """
        最优解法：利用辅助栈进行插入排序
        在保持主栈排序的同时，将新元素插入到正确位置。
        """
        # 1. 将主栈中所有比 val "小" 的元素暂时移到辅助栈
        #    因为我们要保持栈顶最小，所以栈顶元素应该比下面的大
        while self.stack and self.stack[-1] < val:
            self.temp_stack.append(self.stack.pop())

        # 2. 此时，主栈的栈顶要么为空，要么是一个比 val 大的数。
        #    这是 val 应该在的正确位置，将其压入主栈。
        self.stack.append(val)

        # 3. 将辅助栈中的元素（都是比 val 小的）移回主栈，
        #    这样它们就自然地落在了 val 的上方，保持了整体的排序。
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())



