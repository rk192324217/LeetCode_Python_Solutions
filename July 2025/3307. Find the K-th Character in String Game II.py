# class Solution:
#     def kthCharacter(self, k: int, operations: List[int]) -> str:
#         # str_start="a"
#         # while len(str_start)<=k:
#         #     for opp in operations:
#         #         new_str=""
#         #         if opp == 0:
#         #                 new_str=str_start
#         #         else:
#         #             for i in str_start:
#         #                 new_str+=chr(ord(i)+1)
#         #         str_start+=new_str
#         # return str_start[k-1]


from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        level = 0
        shift = 0
        n=1
        while n<k:
            n*=2
            level+=1

        while n>1:
            if k > n//2:
                shift += operations[level-1]  # Char will be shifted
                k -= n//2
            n//=2
            level -= 1

        return chr(ord('a') + shift %26)
