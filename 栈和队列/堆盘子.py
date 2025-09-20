class StackOfPlates:
    """
    题目描述：设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，
    我们就会另外堆一堆盘子。请实现数据结构SetOfStacks，模拟这种行为。
    SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。
    SetOfStacks.push()和SetOfStacks.pop()应该与普通栈的操作方法相同（也就是说，pop()返回的值，
    应该跟只有一个栈时的情况一样）。
    进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。
    """
    def __init__(self, cap: int):
        self.stack = [] #创建总栈，也就是盘子堆
        self.cap = cap #每个盘子堆的高度限制

    def push(self, val: int) -> None:
        if self.cap <= 0:  #边界测试会卡这里
            return
        if not self.stack or len(self.stack[-1]) == self.cap:
            self.stack.append([val])
        else:
            self.stack[-1].append(val)

    def pop(self) -> int:
        if not self.stack:
            return -1
        value = self.stack[-1].pop()
        if not self.stack[-1]:
            del self.stack[-1]
        return value

    def popAt(self, index: int) -> int:
        if not self.stack or index < 0 or index >= len(self.stack):
            return -1
        value = self.stack[index].pop()
        if not self.stack[index]:
            del self.stack[index]
        return value