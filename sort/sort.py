
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
