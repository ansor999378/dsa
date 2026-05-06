# 1. Bizda bir quti bor (Ichida sonlar bor)
# quti = [10, 50, 99, 7]

# # 2. Bizga kerak bo'lgan narsa
# kerakli_son = 99

# # 3. Funksiya: Qidiruvchi robot
# def qidirish(quti, kerakli_son):
    
#     # Ro'yxatdagi har bir narsani bittalab olib ko'ramiz
#     # i = tartib raqami (index), son = o'sha qutidagi narsa
#     for i, son in enumerate(quti):
        
#         # Ekranga nima qilayotganimizni yozamiz (tushunish uchun)
#         print(f"Hozir {son} ni tekshiryapman...")
        
#         # AGAR biz qidirgan son shu bo'lsa:
#         if son == kerakli_son:
#             return f"Topdim! U {i}-xonasida turibdi."
            
#     # Agar hamma qutini ko'rib bo'lib ham topmasak:
#     return "Afsuski, bunaqa son yo'q."

# # --- Dasturni ishlatamiz ---
# natija = qidirish(quti, kerakli_son)
# print("----------------")
# print(natija)'
# class Solution:
#     def binary_search(self, ruyxat, nishon): # 1. self qo'shildi
#         past = 0
#         baland = len(ruyxat) - 1
        
#         while past <= baland:
#             orta = (past + baland) // 2
#             ortadagi_son = ruyxat[orta]
#             print(f'qidirypamn {ortadagi_son} index da ekan')
#             if ortadagi_son == nishon:
#                 return orta # LeetCode odatda faqat indeksni so'raydi
            
#             if ortadagi_son < nishon:
#                 past = orta + 1
#             else:
#                 baland = orta - 1
#         return -1
# yechim = Solution()
# mening_ruyxatim = [1, 3, 5, 7, 9, 11, 13, 15] # ALBATTA TARTIBLANGAN BO'LSIN!
# kerak = 13
# natija = yechim.binary_search(mening_ruyxatim, kerak)
# print(natija)




# class Solution:
#     def twoSum(self, nums, target):
#         savat = {} 
#         for i, son in enumerate(nums):
#             kerakli_son = target - son    
#             if kerakli_son in savat:
#                 return [savat[kerakli_son], i]
#             savat[son] = i

# yechim = Solution()
# mening_ruyxatim = [5, 11, 2, 8, 1] 
# kerak = 13
# natija = yechim.twoSum(mening_ruyxatim, kerak)

# print(natija) 
# from typing import List
# class Solution:
#     def reverseString(self, s: List[str]):
#         """ Bu funksiya hech narsa qaytarmaydi (None), u berilgan 's' ro'yxatining o'zini o'zgartiradi."""
#         L = 0               # Chap (L
#         R = len(s) - 1      # O'ng (Right) oxirida
#         while L < R:
#             s[L], s[R] = s[R], s[L]
#             L += 1  
#             R -= 1  
# if __name__ == "__main__":
#     yechim = Solution()
#     soz = ["H", "e", "l", "l", "o"]
#     print(f"Boshida: {soz}")
#     yechim.reverseString(soz)
#     print(f"Teskari: {soz}") 


# def merge(nums1, m, nums2, n):

#     i, j, k = m-1, n-1, m+n-1
#     while i >= 0 and j >= 0:
#         if nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -= 1
#     while j >= 0:
#         nums1[k] = nums2[j]
#         j -= 1
#         k -= 1

# nums1 = [1, 3, 5, 0, 0, 0]  
# m = 3  
# nums2 = [2, 4, 6]
# n = 3
# merge(nums1, m, nums2, n)
# print(nums1) 


# def moveZeroes(nums):
#     slow = 0
#     for fast in range(len(nums)):
#         if nums[fast] != 0:
#             nums[slow], nums[fast] = nums[fast], nums[slow]
#             slow += 1

# nums = [0, 1, 0, 3, 12]
# moveZeroes(nums)
# print(nums)

# def isPalindrome(s):
#     left, right = 0, len(s)-1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True




# def move_zeroes(nums):
#     slow = 0
#     for fast in range(len(nums)):
#         if nums[fast] != 0:
#             nums[slow], nums[fast] = nums[fast], nums[slow]
#             slow += 1


# def remove_element(nums, val):
#     slow = 0
#     for fast in range(len(nums)):
#         if nums[fast] != val:
#             nums[slow] = nums[fast]
#             slow += 1
#     return slow


# def three_sum(nums):
#     nums.sort()
#     result = []

#     for i in range(len(nums)):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue

#         l, r = i+1, len(nums)-1

#         while l < r:
#             s = nums[i] + nums[l] + nums[r]
#             if s == 0:
#                 result.append([nums[i], nums[l], nums[r]])
#                 l += 1
#                 r -= 1
#                 while l < r and nums[l] == nums[l-1]:
#                     l += 1
#             elif s < 0:
#                 l += 1
#             else:
#                 r -= 1
#     return result

# print(three_sum([-1,0,1,2,-1,-4]))


# def max_subarray_sum(nums, k):

#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     for i in range(1, len(nums) - k + 1):
#         window_sum = window_sum - nums[i-1] + nums[i+k-1]
#         max_sum = max(max_sum, window_sum)

#     return max_sum


# nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
# k = 4
# [1, 2, 3, 4, 6]
# def two_sum(nums,target):
#     result ={}


#     for i , son in enumerate(nums):


#         kerakli_son = target - son
#         if kerakli in result:
#             return [result[kerakli_son]]
#         else:


#             result [son] = i

# nums = [2,4,2,1]
# target = 6
# print(two_sum(nums,target))

from collections import Counter

class Solution:
    def findAnagrams(s,p):
        
        result = []

        p_count = Counter(p)
        window_count = Counter()
        
        left = 0
        p_len = len(p)
        s_len = len(s)
        
        for right in range(s_len):
            window_count[s[right]] += 1
                
            if right - left + 1 > p_len:
                char_to_remove = s[left]
                window_count[char_to_remove] -= 1
                
                if window_count[char_to_remove] == 0:
                    del window_count[char_to_remove]
                
                left += 1
            
            if window_count == p_count:
                result.append(left)
        return result

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))


def longestConsecutive(nums):

    num_set = set(nums)   # barcha sonlarni set ga o'tkazamiz
    longest = 0

    for num in num_set:

        if num - 1 not in num_set:

            length = 1
            current = num

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))


 for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0


s = list(s)

result  = ''.join(s.pop() for _ in range(len(s)))

return result


def nextGreater(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]

        stack.append(i)

    return result


print(nextGreater([2,1,2,4,3]))