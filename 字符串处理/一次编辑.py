class Solution(object):
    """字符串有三种编辑操作:插入一个英文字符、删除一个英文字符或者替换一个英文字符
    改进策略：可以加一个递归调用，让位置固定
    """
    def oneEditAway(self, first, second):
        m = len(first) #第一个字符串的长度
        n = len(second) #第二个字符串的长度
        absolute =abs(m - n)
        #长度相差大于1直接就不用判断了
        if absolute > 1:
            return False
        #长度相等同进退
        elif absolute ==0:
            flag = 0
            for i in range(m):
                if first[i] != second[i]:
                    flag += 1
                    if flag > 1:
                        return False
            return True
        #长度相差为1长的先走
        else:
            flag = 0
            i = 0 #指向第一个字符串
            j = 0 #指向第二个字符串
            while i<m and j<n: #and ——>并且、or ——>或者
                if first[i] != second[j]:
                   if len(first) > len(second):
                       i += 1
                   else:
                       j += 1
                   flag += 1
                   if flag > 1:
                       return False
                else:
                    i += 1
                    j += 1
            return True


    def oneEditAwayN2(self, first: str, second: str) -> bool:
        """官方代码"""
        m, n = len(first), len(second)
        # 1. 绝妙的预处理技巧
        if m < n:
            return self.oneEditAway(second, first)

        # 2. 快速失败
        if m - n > 1:
            return False

        # 3. 核心魔法：寻找第一个不同点
        for i, (x, y) in enumerate(zip(first, second)):
            #zip 函数的作用是将多个可迭代对象（比如这里的两个字符串 first 和 second）中对应位置的元素打包成一个个元组 (tuple)。zip 会在最短的那个可迭代对象耗尽时停止
            #enumerate 函数用于将一个可迭代对象（这里是 zip 的输出结果）组合为一个索引序列，同时列出数据下标和数据
            if x != y:
                # 4. 终极对决：一行代码判断所有情况
                return  first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]

        # 5. 完美匹配的情况
        return True

"""
三元等价运算符
first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]
if m == n:
    result = (first[i + 1:] == second[i + 1:])
    return result
else:
    result = (first[i + 1:] == second[i:])
    return result
"""






