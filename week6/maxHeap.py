# 無迴圈思考版QQ
arr = [7,12,2,4]
# print(*arr)

maxi = arr[0]
m_index = 0
size = len(arr)

def find_index(i):
    main_index = (i-1)//2
    left_index = 2*i+1
    right_index =2*i+2
    return [main_index, left_index, right_index]

if arr[find_index(0)[1]] < arr[find_index(0)[2]]:
    if arr[find_index(0)[2]] > arr[0]:
        arr[0], arr[find_index(0)[2]] = arr[find_index(0)[2]], arr[0]
elif arr[find_index(0)[1]] > arr[find_index(0)[2]]:
    if arr[find_index(0)[1]] > arr[0]:
        arr[0], arr[find_index(0)[1]] = arr[find_index(0)[1]], arr[0]
        if find_index(1)[2] < len(arr) and arr[find_index(1)[1]] > arr[find_index(1)[2]] :
            if arr[find_index(1)[1]] > arr[1]:
                arr[1], arr[find_index(1)[1]] = arr[find_index(1)[1]] , arr[1]
        elif find_index(1)[2] < len(arr) and arr[find_index(1)[1]] > arr[find_index(1)[2]]:
            if arr[find_index(1)[2]] > arr[1]:
                arr[1], arr[find_index(1)[2]] = arr[find_index(1)[1]] , arr[2]
                
arr [0], arr[len(arr)-1] = arr[len(arr)-1], arr [0]

if arr[find_index(0)[1]] < arr[find_index(0)[2]]:
    if arr[find_index(0)[2]] > arr[0]:
        arr[0], arr[find_index(0)[2]] = arr[find_index(0)[2]], arr[0]
elif arr[find_index(0)[1]] > arr[find_index(0)[2]]:
    if arr[find_index(0)[1]] > arr[0]:
        arr[0], arr[find_index(0)[1]] = arr[find_index(0)[1]], arr[0]
        if find_index(1)[2] < len(arr)-1 and arr[find_index(1)[1]] > arr[find_index(1)[2]] :
            if arr[find_index(1)[1]] > arr[1]:
                arr[1], arr[find_index(1)[1]] = arr[find_index(1)[1]] , arr[1]
        elif find_index(1)[2] < len(arr)-1 and arr[find_index(1)[1]] > arr[find_index(1)[2]]:
            if arr[find_index(1)[2]] > arr[1]:
                arr[1], arr[find_index(1)[2]] = arr[find_index(1)[1]] , arr[2]
                
arr [0], arr[len(arr)-2] = arr[len(arr)-2], arr [0]

if find_index(0)[2]<len(arr)-2 and arr[find_index(0)[1]] < arr[find_index(0)[2]]:
    if arr[find_index(0)[2]] > arr[0]:
        arr[0], arr[find_index(0)[2]] = arr[find_index(0)[2]], arr[0]
elif find_index(0)[2]<len(arr)-2 and arr[find_index(0)[1]] > arr[find_index(0)[2]]:
    if arr[find_index(0)[1]] > arr[0]:
        arr[0], arr[find_index(0)[1]] = arr[find_index(0)[1]], arr[0]
        if find_index(1)[2] < len(arr)-2 and arr[find_index(1)[1]] > arr[find_index(1)[2]] :
            if arr[find_index(1)[1]] > arr[1]:
                arr[1], arr[find_index(1)[1]] = arr[find_index(1)[1]] , arr[1]
        elif find_index(1)[2] < len(arr)-2 and arr[find_index(1)[1]] > arr[find_index(1)[2]]:
            if arr[find_index(1)[2]] > arr[1]:
                arr[1], arr[find_index(1)[2]] = arr[find_index(1)[1]] , arr[2]

# for a in arr:
#     print(find_index(a))
# arr

# if maxi < arr[find_index(0)[1]]:
#     arr[0], arr[find_index(0)[1]] = arr[find_index(0)[1]], arr[0]
print(arr)
