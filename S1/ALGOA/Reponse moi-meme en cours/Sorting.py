'''
排序算法

'''

# 冒泡排序
def Bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        flag = False      # 记录是否有交换
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                flag = True
        if not flag:
            break     # 没有交换，全部排列好


# 选择排序
def Selection_sort(A):
    n = len(A)

    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]


# 插入排序
def Insert_sort(A):
    n = len(A)

    for i in range(1, n):
        base = A[i]
        j = i-1
        while j >= 0 and A[j] > base:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = base

# 快速排序
# 基于哨兵划分，选择哨兵，左右分治
def partition(A, left, right):
    i = left   # 选择哨兵
    j = right
    while i < j:
        while A[j] >= A[left] and i < j:    # 从右往左
            j -= 1
        while A[j] <= A[left] and i < j:    #从左往右
            i += 1
        A[i], A[j] = A[j], A[i]
    A[i], A[left] = A[left], A[i]    # 把哨兵交换到这里来
    return i

def Quick_sort(A):
    # 递归终止条件
    if len(A) < 2:
        return
    left = 0
    right = len(A) - 1
    # 哨兵划分
    pivot = partition(A, left, right)
    Quick_sort(A[: pivot])
    Quick_sort(A[pivot+1 :])


# 归并排序
def merge_sort(A, left, right):
    # 终止条件
    if left >= right:
        return
    mid = left + (right - left) // 2
    merge_sort(A, left, mid)
    merge_sort(A, mid+1, right)
    merge(A, left, mid, right)

def merge(A, left, mid, right):
    #左右数组已经排好
    # 暂存数组
    tmp = list(A[left: right+1])
    # 左右数组索引
    left_start = 0              # 指tmp的首端
    left_end = mid - left        # 指tmp的左半部分右端
    right_start = mid + 1 - left    
    right_end = right - left    # 指tmp的末端
    i = left_start
    j = right_start
    for k in range(len(A)):
        # 左边已经融合结束，要把右边的放进来
        if i > left_end:
            # j 是指引右边的
            A[k] = tmp[j]
            j += 1
        # 如果右边融合结束，或者左边的小于右边，那么就把左边的存进来
        elif j > right_end or tmp[i] < tmp[j]:
            A[k] = tmp[i]
            i += 1
        # 都没融合结束并且左边的大于右边的， 就把右边的存进来
        else:
            A[k] = tmp[j]
            j += 1

# 堆排序
def Heap_sort(A):
    # --todo--
    pass
    

if __name__ == '__main__':
    A = [10, 4, 2, 9, 13, 7, 8, 17, 14, 15, 20, 19]
    left = 0
    right = len(A) - 1
    merge_sort(A, left, right)
    print(A)