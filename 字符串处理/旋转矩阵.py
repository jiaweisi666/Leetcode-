class Solution(object):
    """方法一：旋转法把矩阵看成一圈一圈的，每一圈中的每个元素旋转
       难点一：很难想到是四个一变换。难点二：给这四个元素分别定位
    """
    def rotateN1(self,matrix):
        n = len(matrix)
        for layer in range(n//2):
            first = layer
            last = n-layer-1
            for i in range(first,last):
                temp = matrix[first][i]
                matrix[first][i] = matrix[n-i-1][first]
                matrix[n-i-1][first] = matrix[last][n-i-1]
                matrix[last][n-i-1] = matrix[i][last]
                matrix[i][last] = temp
                '''
                元素定位：
                左上：matrix[first][i]  右上：matrix[i][last]
                左下：matrix[n-i-1][first] 右下：matrix[last][n-i-1]
                '''
    """
    方法二：翻折法，先沿对角线翻折，再沿竖直对称线翻折
    """
    def rotateN2(self,matrix):
        n = len(matrix)

        # 步骤 1: 矩阵转置
        # 沿着主对角线（左上到右下）进行翻转
        # 我们只需要遍历上三角部分（j 从 i 开始）即可完成交换，避免重复交换
        for i in range(n):
            for j in range(i, n):
                # 使用元组赋值来交换 matrix[i][j] 和 matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 步骤 2: 水平翻转
        for i in range(n):
            # 使用 Python 列表的 reverse() 方法原地反转每一行
            matrix[i].reverse()
            # 也可以使用切片赋值的方式: matrix[i] = matrix[i][::-1]




