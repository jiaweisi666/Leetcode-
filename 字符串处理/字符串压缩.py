class Solution(object):
    def compressString(self, S):
        i = 0
        result = []
        n = len(S)
        while i < n:
            j =i
            while j<n and S[j] == S[i]:
                j += 1
            count = j - i
            result.append(S[i])
            result.append(str(count))
            i = j
        compressed_s = "".join(result)
        return compressed_s if len(compressed_s) < n else S

solution = Solution()
print(solution.compressString("aabcccccaaa"))

