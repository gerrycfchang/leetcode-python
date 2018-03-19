# 599. Minimum Index Sum of Two Lists
# 
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
# 
# You need to help them find out their common interest with the least list index sum. 
# If there is a choice tie between answers, output all of them with no order requirement. 
# You could assume there always exists an answer.
# 
# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).# 


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """        
        c = {k: v for v, k in enumerate(list1)}
        minSum = float('inf')
        res = []
        for i in range(len(list2)):
            if list2[i] in c:
                if minSum >= i+c[list2[i]]:
                    minSum = i+c[list2[i]]
                    res = [list2[i]]
                elif minSum == i+c[list2[i]]:
                    res.append(list2[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    a = ["Shogun","Tapioca Express","Burger King","KFC"]
    b = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]  
    assert sol.findRestaurant(a, b) == ['Shogun']

    a = ["Shogun","Tapioca Express","Burger King","KFC"]
    b = ["KFC","Shogun","Burger King"]
    assert sol.findRestaurant(a, b) == ['Shogun']
        