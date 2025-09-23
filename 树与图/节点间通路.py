import collections

class Solution:
    """
    题目描述：节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。
    """
    def findWhetherExistsPath(self, n: int, graph: list[list[int]], start: int, target: int) -> bool:
        """
        深度优先搜索（DFS）
        1. 构建邻接表来表示图，方便快速查找一个节点的邻居。
        2. 从 start 节点开始进行深度优先搜索。
        3. 使用一个 visited 集合来记录访问过的节点，防止在环中无限循环。
        4. 在搜索过程中，如果遇到 target 节点，则说明路径存在。
        """
        # 边界情况：如果起点和终点相同，路径显然存在
        if start == target:
            return True

        # 1. 构建邻接表
        # 使用 defaultdict 可以简化代码，当访问一个不存在的键时，会自动创建一个空列表
        adjacency_list = collections.defaultdict(list)
        for u, v in graph:
            adjacency_list[u].append(v)

        # 2. 创建一个 visited 集合来记录已访问的节点
        visited = set()

        # 3. 使用栈来实现迭代版的 DFS（也可以用递归）
        # 栈中存放待访问的节点，首先将起点放入
        stack = [start]
        visited.add(start)

        while stack:
            # 从栈顶取出一个节点进行探索
            current_node = stack.pop()

            # 探索当前节点的所有邻居
            for neighbor in adjacency_list[current_node]:
                # 4. 如果邻居就是目标节点，说明找到了路径，直接返回 True
                if neighbor == target:
                    return True
                
                # 如果这个邻居还没有被访问过，则加入栈和 visited 集合，留待后续探索
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        # 如果栈变空了，说明从 start 出发的所有路径都走完了，但仍未找到 target
        return False
#问题一：add()和append()的区别：add()适用于集合、append()适用于列表

    def findWhetherExistsPath_dfs_recursive(self, n: int, graph: list[list[int]], start: int, target: int) -> bool:
        if start == target:
            return True

        adjacency_list = collections.defaultdict(list)
        for u, v in graph:
            adjacency_list[u].append(v)

        visited = set()

        def dfs(current_node):
            # 如果当前节点就是目标，返回 True
            if current_node == target:
                return True

            # 标记当前节点为已访问
            visited.add(current_node)

            # 探索所有邻居
            for neighbor in adjacency_list[current_node]:
                if neighbor not in visited:
                    # 如果从邻居出发能找到目标，则整条路径都成立
                    if dfs(neighbor):
                        return True

            # 从当前节点出发的所有路径都走不通
            return False

        # 从起点开始递归搜索
        return dfs(start)

    # 广度优先搜索 (BFS),非常适合用来找最短路径（在无权图中）
    def findWhetherExistsPath_bfs(self, n: int, graph: list[list[int]], start: int, target: int) -> bool:
        if start == target:
            return True

        adjacency_list = collections.defaultdict(list)
        for u, v in graph:
            adjacency_list[u].append(v)

        # BFS 使用队列
        queue = collections.deque([start])
        visited = {start}

        while queue:
            # 从队首取出一个节点
            current_node = queue.popleft()

            for neighbor in adjacency_list[current_node]:
                if neighbor == target:
                    return True

                if neighbor not in visited:
                    visited.add(neighbor)
                    # 将新发现的节点加入队尾
                    queue.append(neighbor)

        return False

'''
DFS 模板：需要一个 stack 和一个 visited 集合。循环的核心是 pop 一个节点，然后把它所有未访问的邻居 push 进去。
BFS 模板：需要一个 queue 和一个 visited 集合。循环的核心是 popleft 一个节点，然后把它所有未访问的邻居 append 进去。
'''
