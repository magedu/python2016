import math
import random


class Heap:
    def __init__(self):
        self.__data = []

    def insert(self, value):
        self.__data.append(value)
        idx = len(self.__data) - 1
        parent = math.floor((idx - 1) / 2)
        while parent >= 0 and self.__data[parent] < value:
            self.__data[idx] = self.__data[parent]
            self.__data[parent] = value
            idx = parent
            parent = math.floor((idx - 1) / 2)

    def pop(self):
        if not self.__data:
            raise Exception('Empty')
        ret = self.__data[0]
        value = self.__data.pop()
        self.__data[0] = value
        idx = 0
        left = 2 * idx + 1
        right = 2 * idx + 2
        while len(self.__data) > left:
            tmp_idx = left
            if len(self.__data) > right and self.__data[right] > self.__data[left]:
                tmp_idx = right
            if self.__data[tmp_idx] > value:
                self.__data[idx] = self.__data[tmp_idx]
                self.__data[tmp_idx] = value
            else:
                return ret
            idx = tmp_idx
            left = 2 * idx + 1
            right = 2 * idx + 2
        return ret

    def remove(self, i):
        if len(self.__data) - 1 < i:
            raise Exception('Empty')
        ret = self.__data[i]
        value = self.__data.pop()
        self.__data[i] = value
        idx = i
        left = 2 * idx + 1
        right = 2 * idx + 2
        while len(self.__data) > left:
            tmp_idx = left
            if len(self.__data) > right and self.__data[right] > self.__data[left]:
                tmp_idx = right
            if self.__data[tmp_idx] > value:
                self.__data[idx] = self.__data[tmp_idx]
                self.__data[tmp_idx] = value
            else:
                return ret
            idx = tmp_idx
            left = 2 * idx + 1
            right = 2 * idx + 2
        return ret

    def view(self):
        print(self.__data)

if __name__ == '__main__':
    heap = Heap()
    for _ in range(8):
        i = random.randint(0, 100)
        print('i is ', i)
        heap.insert(i)
    heap.view()
    #heap.pop()
    heap.remove(1)
    heap.view()
