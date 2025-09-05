class Solution(object):
    """问题描述：有两个字符串，其中一个字符串重新排序后能否变成另一个字符串"""
    """问题关键：这两个字符串每种字符，以及字符的数量是否完全相同"""
    def CheckPermutationN1(self, s1, s2):
        """排序法：给两个字符串都重排看它们是否相同"""
        return sorted(s1) == sorted(s2)
    def CheckPermutationN2(self,s1,s2):
        """频度法：计算每个字符串出现的频度"""
        if len(s1) != len(s2):
            return False
        #手动为s1、s2创建频度计数字典
        freq_s1 = {}
        for i in s1:
            freq_s1[i] = freq_s1.get(i,0)+1
        freq_s2 = {}
        for j in s2:
            freq_s2[j] = freq_s2.get(j,0)+1
        #比较这两个字典看是否相同
        return freq_s1 == freq_s2

solution = Solution()
print(solution.CheckPermutationN2("aabc","abbc"))













