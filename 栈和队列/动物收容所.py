from collections import deque
from typing import List


class AnimalShelfN1:
    """
    动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。
    在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，
    或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。
    请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。
    """
    def __init__(self):
        self.any_queue = [] #创建总列表
        self.dog_queue = [] #创建狗列表
        self.cat_queue = [] #创建猫列表

    def enqueue(self, animal: List[int]) -> None:
        self.any_queue.append(animal)
        if animal[1] == 0: #这是一只猫
            self.cat_queue.append(animal)
        else :
            self.dog_queue.append(animal)

    def dequeueAny(self) -> List[int]:
        if not self.any_queue:
            return [-1, -1]
        animal = self.any_queue.pop(0)
        if animal[1] == 0:
            self.cat_queue.pop(0)
        else:
            self.dog_queue.pop(0)
        return animal

    def dequeueDog(self) -> List[int]:
        if not self.dog_queue:
            return [-1, -1]
        animal = self.dog_queue.pop(0)
        self.any_queue.remove(animal)
        return animal

    def dequeueCat(self) -> List[int]:
        if not self.cat_queue:
            return [-1, -1]
        animal = self.cat_queue.pop(0)
        self.any_queue.remove(animal)
        return animal

'''
解题日志：在dequeueCat和dequeueDog方法中移除any_queue列表中的的元素，我开始想的是，
通过self.any_queue.pop(animal[0])，但这个方法是行不通的
首先：真实的动物标签并不一定是顺序排列，其次：就算是顺序排列，动物的标签也不能用来表示列表元素的位置。
所以直接用remove方法更好
'''

class AnimalShelfN2:
    """
    动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。
    在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，
    或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。
    请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。
    """

    def __init__(self):
        # 最优解法：使用 deque 实现 O(1) 的出队和入队
        self.dog_queue = deque()
        self.cat_queue = deque()
        # 使用一个时间戳来记录动物的进入顺序
        self.timestamp = 0

    def enqueue(self, animal: List[int]) -> None:
        # 为进入的动物打上时间戳，然后根据类型放入对应的队列
        # 存储格式: (时间戳, [动物编号, 动物类型])
        if animal[1] == 0:  # 这是一只猫
            self.cat_queue.append((self.timestamp, animal))
        else:
            self.dog_queue.append((self.timestamp, animal))

        # 时间戳递增，为下一个动物做准备
        self.timestamp += 1

    def dequeueAny(self) -> List[int]:
        # 如果两个队列都为空，则无动物可收养
        if not self.dog_queue and not self.cat_queue:
            return [-1, -1]
        # 如果狗队列为空，只能收养猫
        if not self.dog_queue:
            return self.dequeueCat()
        # 如果猫队列为空，只能收养狗
        if not self.cat_queue:
            return self.dequeueDog()

        # 比较猫和狗的“时间戳”，时间戳小的更“老”
        dog_timestamp = self.dog_queue[0][0]
        cat_timestamp = self.cat_queue[0][0]

        if dog_timestamp < cat_timestamp:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self) -> List[int]:
        if not self.dog_queue:
            return [-1, -1]
        # popleft() 是 O(1) 操作
        timestamp, animal_data = self.dog_queue.popleft()
        return animal_data

    def dequeueCat(self) -> List[int]:
        if not self.cat_queue:
            return [-1, -1]
        # popleft() 是 O(1) 操作
        timestamp, animal_data = self.cat_queue.popleft()
        return animal_data