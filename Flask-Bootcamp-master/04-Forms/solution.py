# # arr = [0,0,0,0,0,0,1,2,3,4,5]
# # arr2 = [55,0,4,2,1,0,0,0,0,4,5,6,7,0,0]
# # arr3 = [0,5,5,5,0,5,0,5,0]
# #
# # def move_zero(lst):
# #     n = len(lst)
# #     if n == 0 or 0 not in lst:
# #         return lst
# #     i = lst.index(0)
# #     j = i+1
# #     while(i >len(lst)):
# #
# #         pass
#
# def move(lst):
#     if len(lst) == 0:
#         return lst
#     i = 0
#     j = 1
#     k = len(lst)-1
#     while j != k:
#         if (lst[i] == 0) and (lst[j] == 0):
#          j = j+1
#
#         if lst[i] == 0 and lst[j] != 0:
#             lst[i], lst[j] = lst[j], lst[i]
#             i = i+1
#
#         if lst[i] != 0 and lst[j] == 0:
#             j = j+1
#             i = j+1
#     return lst
#
#


lsts = [9,0,0,0,0,0,7,5,4,3,2,0,2,0,0,0,2,2,2,0,2,2,2000,2]



#
# lst = [0,0,0,0,0,1]
#
# print(move(lst))
# #
# # #####mergersort
# #
# #
# #
# #
# # ######selectionsort
# #
# def lensy(lst):
#     n = len(lst)
#     if n ==0 or 0 not in lst:
#         return lst
#     i = lst.index(0)
#     j = i+1
#
#     while j < n-1:
#         if lst[i] != 0:
#             i +=1
#         if lst[j] == 0:
#             j +=1
#
#         if lst[i] ==0 and lst[j] !=0:
#             lst[i], lst[j] = lst[j],lst[i]
#             i +=1
#
#     return lst

#
# def two_num(k, arr):
#     num = 0
#     j = len(arr)
#     while num != j - 1:
#         for i in range(len(arr) - 1):
#             if arr[num] + arr[i] == k:
#                 print("{} and {}".format(arr[num], arr[i]))
#         num += 1
#     else:return 0
#
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(two_num(10, arr))
#
#
#
# import pandas as pd
#
# pd.read_json()
import os

path = 'MoodToolsData.zip\MoodToolsData'

folder = os.fsencode(path)

filenames = []

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.json') ): # whatever file types you're using...
        filenames.append(filename)

filenames.sort()

