class Solution(object):
    """
    题目描述：编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
    解题思路：先找出零的位置，并标记。再清零。
    """
    def setZeroesN1(self, matrix):
        n = len(matrix) #矩阵有几行
        m = len(matrix[0]) #矩阵有几列
        location_x = []
        location_y = []
        #寻找为零的数，标记出行数和列数
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    location_x.append(i)
                    location_y.append(j)

        for i in location_x:
            for j in range(m):
                matrix[i][j] = 0 #将整行置零

        for i in location_y:
            for j in range(n):
                matrix[j][i] = 0 #将整列置零

    def setZeroesN2(self,matrix):
        """
        优化点：将第一行和第一列作为标记。节省内存空间
        """
        m = len(matrix)  # 矩阵有几行
        n = len(matrix[0])  # 矩阵有几列



        #检查第一行和第一列是否存在0
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # 遍历除第一行/列外的其余部分。
        # 如果 matrix[i][j] 为 0，就用第一行/列来标记。
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3. 根据标记，将对应的行和列（除第一行/列外）置零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4. 最后，根据第1步的记录，处理第一行和第一列
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
