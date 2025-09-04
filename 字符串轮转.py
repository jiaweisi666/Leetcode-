from collections import Counter
class Solution(object):
    """
    题目描述：字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成
    核心思路:
        1. 如果两个字符串长度不同，则 s2 不可能是 s1 的旋转，直接返回 False。
        2. 如果 s2 是 s1 的一个旋转，那么 s2 必定是 s1 与自身拼接后形成的新字符串 (s1+s1) 的一个子串。
        3. 这个方法同时处理了空字符串等边界情况。
    """
    def isFlipedStringN1(self, s1, s2):
        #检查长度是否相等
        if len(s1) != len(s2):
           return False

        #检查频度是否一样
        F_s1 = Counter(s1)
        F_s2 = Counter(s2)
        if F_s1 != F_s2:
            return False

        #检查顺序是否一样
        T_s1 = s1 + s1
        if s2 in T_s1:
            return True
        else:
            return False

    def isFlipedStringN2(self, s1: str, s2: str) -> bool:
        """
        优化版
        """
        # 长度检查是必要且最高效的第一步
        if len(s1) != len(s2):
            return False
        return s2 in s1 + s1

    def isFlipedString_Simulation(self, s1: str, s2: str) -> bool:
        """
        使用“模拟法”检查 s2 是否为 s1 旋转而成。
        这个方法会生成 s1 的所有旋转结果，并逐一与 s2 比较。
        """
        # 1. 预检查：长度不同，绝对不可能旋转而成。
        if len(s1) != len(s2):
            return False

        # 2. 边界情况：如果两个都是空字符串，它们互为旋转。
        if not s1:
            return True

        # 3. 开始模拟：遍历每一种可能的“切分点”
        #    对于长度为 n 的字符串，有 n 种旋转方式。
        for i in range(len(s1)):
            # 将 s1 在 i 处切开，分成两部分
            # part1 是 s1 的后半部分 (从 i 到结尾)
            # part2 是 s1 的前半部分 (从开头到 i)
            part1 = s1[i:]
            part2 = s1[:i]

            # 将两部分拼接，形成一个旋转后的新字符串
            rotated_s1 = part1 + part2

            # 打印出每次旋转的结果，帮助理解
            print(f"旋转 {i} 次: 切下'{part2}'，拼到后面，得到 -> '{rotated_s1}'")

            # 检查这个旋转结果是否与 s2 相等
            if rotated_s1 == s2:
                # 如果找到了，就没必要再继续试了，直接返回成功
                return True

        # 4. 如果循环跑完了，所有旋转方式都试过了，还是没找到匹配的
        #    那就说明 s2 不是 s1 的旋转。
        return False
