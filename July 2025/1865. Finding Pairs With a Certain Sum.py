from collections import Counter

class FindSumPairs(object):
    
    def __init__(self, num1, num2):
        """
        Constructor to initialize the object with two lists:
        - num1: static list (does not change)
        - num2: dynamic list (can be modified with add())
        
        Also maintains a Counter for num2 to efficiently track frequency
        of elements, which helps optimize the count() method.
        """
        self.num1 = num1
        self.num2 = num2
        self.cnt = Counter(num2)  # Frequency map of elements in num2

    def add(self, index, val):
        """
        Add a value 'val' to the element at position 'index' in num2.
        Also updates the frequency Counter (self.cnt) accordingly.

        Time Complexity: O(1)
        """
        temp_num2 = self.num2
        temp_cnt = self.cnt

        old_val = temp_num2[index]             # Current value at index
        new_val = old_val + val                # New value after addition

        temp_cnt[old_val] -= 1                 # Decrease count of old value
        if temp_cnt[old_val] == 0:
            del temp_cnt[old_val]              # Optional cleanup for 0-count

        temp_num2[index] = new_val             # Update the value in num2
        temp_cnt[new_val] += 1                 # Increase count of new value

    def count(self, tot):
        """
        Returns the number of pairs (i, j) such that:
        num1[i] + num2[j] == tot

        For each element in num1, check if (tot - num1[i]) exists in num2
        using the frequency map for fast lookup.

        Time Complexity: O(len(num1))
        """
        count = 0
        for i in self.num1:
            rem = tot - i                      # The required complement
            count += self.cnt.get(rem, 0)      # Add its frequency (if exists)
        return count

        # -------------------------------
        # Alternatives for educational purposes:
        # -------------------------------

        # # Slightly less efficient version (rebuilds frequency map every time)
        # cnt = 0
        # count = Counter(self.num2)
        # for i in self.num1:
        #     find = tot - i
        #     if find in count:
        #         cnt += count[find]
        # return cnt

        # # Brute Force: O(n*m) — not suitable for large input sizes
        # for i in self.num1:
        #     for j in self.num2:
        #         if i + j == tot:
        #             count += 1
        # return count

# Example usage:
# obj = FindSumPairs([1, 2, 3], [3, 4])
# obj.add(0, 1)         # Adds 1 to num2[0], num2 becomes [4, 4]
# print(obj.count(6))   # Returns number of pairs summing to 6
