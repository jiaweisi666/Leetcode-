class Solution(object):
    """将字符串URL化"""
    def replaceSpacesN1(self, S, length):
        """双指针"""
        #1、将字符串转换成列表
        char_list = list(S)
        #2、初始化双指针
        p1 = length - 1 #读指针 指向真实字符串的末尾
        p2 = len(S) - 1 #写指针 指向完整缓冲区的末尾
        #3、从后往前遍历
        while p1 >= 0:
            if char_list[p1] == ' ':
                #如果是空格填上%20
                char_list[p2-2:p2+1] = ['%','2','0']
                p2 -= 3
            else:
                #如果不是空格直接复制
                char_list[p2] = char_list[p1]
                p2 -= 1
            p1 -= 1
        return "".join(char_list[p2 + 1:])

    def replaceSpacesN2(self,S,length):
        """利用replace()方法"""
        return S[:length].replace(" ","%20")

    def replaceSpacesN3(self,S,length):
        """自创拼接法"""
        result_parts = []
        # 2. 只遍历真实长度的部分
        for i in range(length):
            char = S[i]
            if char == ' ':
                result_parts.append('%20')
            else:
                result_parts.append(char)

        # 3. 一次性合并成最终字符串，这是高效的
        return ''.join(result_parts)




solution = Solution()
print(solution.replaceSpacesN3("  ",2))














