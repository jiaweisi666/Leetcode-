from collections import Counter

class Solution(object):
    def canPermutePalindromeN1(self, s):
        """题目要求判断是否为回文串
        方法：首先给字符串做频度统计，再判断奇数出现的数量如果奇数大于1，就不是回文串
        """
        freq = {}
        count = 0
        for i in s:
            freq[i] = freq.get(i,0) + 1
        print(freq)
        for j in freq.values():
            if j % 2 == 1:
                count += 1
                if count >= 2:
                    return False
        return True

    def canPermutePalindromeN2(self,s):
        """代码改进
        1、使用collections标准库中的Counter直接频度计数
        2、利用 Python 的生成器表达式和 sum() 函数
        """
        freq = Counter(s)
        counts = sum(i%2 for i in freq.values())
        return counts <=1
solution = Solution()
print(solution.canPermutePalindromeN2("aabc"))