class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 브루트포스: 모든 조합 경우의 수 + 인덱스 갱신해서 target 나올 때까지 돌린다
        # 2개의 정수 합으로만 답이 나온다
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]




