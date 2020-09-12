class Solution:
    def canJump(self, nums):
        if nums[0] == 0:
            if len(nums) > 1:
                return False
            else:
                return True
        if len(nums) == 0:
            return False
        if 0 not in nums[:-1]:
            return True
        for i in range(1,len(nums)):
            if nums[i] == 0:
                flag = False
                for j in range(0,i):
                    if (j + nums[j]) > i:
                        flag = True
                        break
                    elif (j+nums[j]) == i and i == len(nums)-1:
                        flag = True
                        break
                if flag==False:
                    return False
        return True


if __name__ == "__main__":
    sl = Solution()
    test = [3,0,0,0]
    res = sl.canJump(test)
    print(res)
