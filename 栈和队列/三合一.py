class TripleInOne(object):
    """
    三合一。描述如何只用一个数组来实现三个栈。
    """
    def __init__(self, stackSize: int):
        """
        构造函数：初始化数据结构
        """
        # 1. 存储每个栈的容量
        self.stackSize = stackSize
        # 2. 创建一个大数组，总容量为 3 * stackSize
        self.stack = [0] * (stackSize * 3)
        # 3. 创建一个指针数组，记录每个栈当前的元素个数（大小）
        #    初始时，每个栈的大小都为 0
        self.pointers = [0, 0, 0]

    def push(self, stackNum: int, value: int) -> None:
        """
        将 value 压入 stackNum 对应的栈
        """
        # 检查栈是否已满
        if self.pointers[stackNum] == self.stackSize:
            return  # 栈满，不执行任何操作

        # 计算要插入的索引位置
        # 索引 = 栈的起始位置 + 当前栈的大小
        index = stackNum * self.stackSize + self.pointers[stackNum]

        # 将值放入数组
        self.stack[index] = value

        # 更新对应栈的大小（指针）
        self.pointers[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        """
        从 stackNum 对应的栈弹出并返回栈顶元素
        """
        # 检查栈是否为空
        if self.isEmpty(stackNum):
            return -1

        # 更新对应栈的大小（指针），先减一
        self.pointers[stackNum] -= 1

        # 计算栈顶元素的索引位置
        # 索引 = 栈的起始位置 + 新的栈的大小
        index = stackNum * self.stackSize + self.pointers[stackNum]

        # 获取栈顶元素的值
        value = self.stack[index]
        return value

    def peek(self, stackNum: int) -> int:
        """
        返回 stackNum 对应的栈的栈顶元素，但不弹出
        """
        # 检查栈是否为空
        if self.isEmpty(stackNum):
            return -1

        # 计算栈顶元素的索引位置
        # 索引 = 栈的起始位置 + 当前栈的大小 - 1
        index = stackNum * self.stackSize + self.pointers[stackNum] - 1

        # 获取栈顶元素的值
        return self.stack[index]

    def isEmpty(self, stackNum: int) -> bool:
        """
        检查 stackNum 对应的栈是否为空
        """
        return self.pointers[stackNum] == 0
