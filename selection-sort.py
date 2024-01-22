#Selection sort
def sort(nums):
    for i in range (5):  # min value low to high index  max value high to low index
        minpos = i # which holds min position
# after every iteration first value is sorted so no need to verify  sorted list
        for j in range (i,6): # unsorted list will be reduced after every iteration
            if nums[j]< nums[minpos]:
                minpos=j

                temp = nums[i]
                nums[i]= nums[minpos]
                nums[minpos]= temp
        print(nums)

nums = [5,3,8,6,7,2]
sort(nums)

print(nums)
