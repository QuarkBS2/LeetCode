from collections import defaultdict


def findMatrix(nums):
    #We initialize the output matrix and the count dictionary
    res_matrix = [[]]
    count_map = defaultdict(list)

    for num in nums:
        #Update the count in dictionary in every iteration of the loop by adding 1 to the current value
        count_map.update({num: count_map.get(num, 0)+1})
        #If the times a number has been seen is larger than the length of the output matrix then
        # create a new row to append the current element
        if count_map.get(num) > len(res_matrix):
            res_matrix.append([num])
            continue
        #Else, we update the output matrix by appending the current element to the quantity of times an
        # element has been seen minus 1
        res_matrix[count_map.get(num)-1].append(num)

    return res_matrix


#Using first test case from LeetCode
print(findMatrix([1,3,4,1,2,3,1]))