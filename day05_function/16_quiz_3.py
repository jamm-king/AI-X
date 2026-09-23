"""
3. 숫자 리스트를 매개변수로 전달받아, 리스트 안에 음수가 하나라도 있으면 True, 없으면 False를 반환하는 함수를 만들고 사용해 보세요. (any 사용)
"""

nums1 = [-1, 2, 3, 4, 5, 6]
nums2 = [1, 2, 3, 4, 5, 6]
print("nums1:", *nums1)
print("nums2:", *nums2)

def any_negative(nums):
    return any(num < 0 for num in nums)

print("nums1에 음수가 하나라도 있는가? =>", any_negative(nums1))
print("nums2에 음수가 하나라도 있는가? =>", any_negative(nums2))