def find_biggers(nums):
    lst = []
    for i in nums:
        count = 0
        for j in nums:
            if i > j:
                count+=1
        lst.append(count)
    return lst

nums = [8,1,2,2,3]
nums2 = [6,5,4,8]
nums3 = [7,7,7,7]
print(find_biggers(nums))