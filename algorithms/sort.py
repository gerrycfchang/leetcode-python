
class BubbleSort(object):
    def sort(self, num):
        for i in range (len(num)):
            for j in range (i+1,len(num)):
                if num[i] > num[j]:
                    num[i], num[j] = num[j], num[i]
        return

class SelectionSort(object):
    def sort(self, num):
        for i in range (len(num)):
            minIndex = i
            for j in range (i+1, len(num)):
                if num[j] < num[minIndex]:
                    minIndex = j
            num[i], num[minIndex] = num[minIndex], num[i]

class InsertionSort(object):
    def sort(self, num):
        for i in range(1, len(num)):
            key = num[i]
            j = i - 1
            while (key < num[j] and j >= 0):
                num[j+1] = num[j]
                j -= 1
            num[j+1] = key

class QuickSort(object):
    def sort(self, num, front, end):
        if front < end:
            pivot = self.partition(num, front, end)
            self.sort(num, front, pivot-1)
            self.sort(num, pivot + 1, end)
    
    def partition(self, num, front, end):
        i = front - 1
        pivot = num[end]

        for j in range (front, end):
            if num[j] < pivot:
                i = i + 1
                #swap
                num[j], num[i] = num[i], num[j]
        i = i + 1
        #swap
        num[i], num[end] = num[end], num[i]
        return i

class MergeSort(object):
    def sort(self, num, front, end):
        if front < end:
            mid = (front + end) / 2
            self.sort(num, front, mid)
            self.sort(num, mid + 1, end)
            self.merge(num, front, mid, end)
    
    def merge(self, num, front, mid, end):
        leftList  = num[front:mid+1]
        rightList = num[mid+1:end+1]
        leftList.append(float('inf'))
        rightList.append(float('inf'))

        leftIndex, rightIndex = 0, 0
        for i in range (front, end+1):
            if leftList[leftIndex] < rightList[rightIndex]:
                num[i] = leftList[leftIndex]
                leftIndex += 1
            else:
                num[i] = rightList[rightIndex]
                rightIndex += 1

class HeapSort(object):
    def sort(self, num):
        self.buildHeap(num)
        i = len(num)
        while i > 1:
            num[i-1], num[0] = num[0], num[i-1]
            i -= 1
            self.maxHeapify(num, 0, i)

    def buildHeap(self, num):
        i = len(num) /2
        while i >=0:
            self.maxHeapify(num, i, len(num))
            i -= 1

    def maxHeapify(self, num, idx, length):
        largest  = idx
        leftIdx  = idx*2 + 1
        rightIdx = idx*2 + 2

        if leftIdx < length and num[leftIdx] > num[idx]:
            largest = leftIdx
        if rightIdx < length and num[rightIdx] > num[largest]:
            largest = rightIdx

        if largest != idx:
            num[idx], num[largest] = num[largest], num[idx]
            self.maxHeapify(nums, largest, length)

class RadixSort(object):
    def sort(self, num, d):
        length = len(num)
        temp = [[0 for _ in range(length)] for _ in range(10)]
        order = [0 for _ in range(10)]
        k, n = 0, 1
        while n <= d:
            for i in range(length):
                lsd = (num[i]/n) % 10
                temp[lsd][order[lsd]] = num[i]
                order[lsd] += 1

            for i in range(10):
                if order[i] != 0:
                    for j in range (order[i]):
                        num[k] = temp[i][j]
                        k += 1
                order[i] = 0
                
            k = 0
            n *= 10


if __name__ == '__main__':
    obj = BubbleSort()
    nums = [4, 2, 6, 1]
    obj.sort(nums)
    assert (nums == [1, 2, 4, 6])

    nums = [4, 24, 6, 1, 17, 3, 89, 43, 45]
    obj.sort(nums)
    assert (nums == [1, 3, 4, 6, 17, 24, 43, 45, 89])

    q = QuickSort()
    nums = [4, 2, 6, 1, 7, 3]
    q.sort(nums, 0, 5)
    assert (nums == [1, 2, 3, 4, 6, 7])

    nums = [4, 24, 6, 1, 17, 3, 89, 43, 45]
    q.sort(nums, 0, 8)
    assert (nums == [1, 3, 4, 6, 17, 24, 43, 45, 89])

    isort = InsertionSort()
    nums = [4, 2, 6, 1, 7, 3]
    isort.sort(nums)
    assert (nums == [1, 2, 3, 4, 6, 7])

    m = MergeSort()
    nums = [4, 2, 6, 1, 7, 3]
    m.sort(nums, 0, 5) 
    assert nums == [1, 2, 3, 4, 6, 7]

    s = SelectionSort()
    nums = [4, 2, 6, 1, 7, 3]
    s.sort(nums) 
    assert nums == [1, 2, 3, 4, 6, 7]

    h = HeapSort()
    nums = [4, 2, 6, 1, 7, 3]
    h.sort(nums) 
    assert nums == [1, 2, 3, 4, 6, 7]

    r = RadixSort()
    nums = [4, 2, 6, 1, 7, 3]
    r.sort(nums, 1) 
    assert nums == [1, 2, 3, 4, 6, 7]

    nums = [73, 22, 93, 43, 55, 14, 28, 65, 39, 81, 33, 100]
    r.sort(nums, 100) 
    assert nums == [14, 22, 28, 33, 39, 43, 55, 65, 73, 81, 93, 100]



