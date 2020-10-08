def function_buble_sort(list):

# Swap the elements to arrange in order
    for number in range(len(list)-1,0,-1): 
        for index in range(number):
            if list[index]>list[index+1]:
                temp = list[index]
                list[index] = list[index+1]
                list[index+1] = temp


# list = [19,2,31,45,6,11,121,27]
# function_buble_sort(list)
# print(list)
