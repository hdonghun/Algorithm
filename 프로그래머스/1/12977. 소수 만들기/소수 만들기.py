def solution(nums):
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                current_num = nums[i]+nums[j]+nums[k]
                True_or_False = True
                
                for z in range(2, current_num):
                    if current_num % z == 0:
                        True_or_False = False
                        break
                        
                if True_or_False:
                    answer+=1
    return answer