"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)

L, R will be integers L <= R in the range [1, 10^6].

"""

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        ### Because the number of bit are 10 at most
        ### which means if all are 1, the largest prime would be 11
        bits = len(bin(R))
        primes = [True for _ in range(bits)]
        primes[0] = primes[1] = False
        for i in range(2, int(bits ** 0.5)+1):
            if primes[i] == True:
                for j in range(i * 2,bits,i):
                    primes[j] = False
        count = 0
        for i in range(L, R+1):
            num = bin(i).count('1')
            if primes[num]:
                count += 1
        return count
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.countPrimeSetBits(842, 888) == 23
    assert sol.countPrimeSetBits(470321, 478504) == 2728