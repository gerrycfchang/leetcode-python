
class BubbleSort(object):
    def sort(self, num):
        for i in range (len(num)):
            for j in range (len(num)-1):
                if num[j] > num[j+1]:
                    temp = num[j]
                    num[j] = num[j+1]
                    num[j+1] = temp
        return

class QuickSort(object):
    def sort(self, num, front, end):
        i = front - 1
        pivot = num[end]

        for j in range (front, end):
            if num[j] < pivot:
                i = i + 1
                self.swap(num, j, i)

        i = i + 1
        self.swap(num, i, end)
        if i - front> 1:
            self.sort(num, front, i - 1)
        if end - i > 1:
            self.sort(num, i+1, end)
        return

    def swap(self, nums, front, end):
        temp = nums[front]
        nums[front] = nums[end]
        nums[end] = temp
        return

class InsertionSort(object):
    def sort(self, num):
        for i in range(1, len(num)):
            key = num[i]
            j = i - 1
            while (key < num[j] and j >= 0):
                num[j+1] = num[j]
                j -= 1
            num[j+1] = key

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

