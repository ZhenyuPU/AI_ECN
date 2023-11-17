import random


def sift_down(nums: list[int], n: int, i: int):
    """ 堆的长度为 n ，从节点 i 开始，从顶至底堆化"""
    # while True:
    # 判断节点 i, l, r 中值最大的节点，记为 ma
    l = 2 * i + 1
    r = 2 * i + 2
    ma = i
    if l < n and nums[l] > nums[ma]:
        ma = l
    if r < n and nums[r] > nums[ma]:
        ma = r
    # 若节点 i 最大或索引 l, r 越界，则无须继续堆化，跳出
    if ma == i:
        return
    # 交换两节点
    else:
        nums[i], nums[ma] = nums[ma], nums[i]
        # 循环向下堆化
        sift_down(nums, n, ma)

def heap(nums: list[int]):
    """ 堆排序"""
    # 建堆操作：堆化除叶节点以外的其他所有节点
    for i in range(len(nums) // 2 - 1, -1, -1):
        sift_down(nums, len(nums), i)
        # 从堆中提取最大元素，循环 n-1 轮
    for i in range(len(nums) - 1, 0, -1):
        # 交换根节点与最右叶节点（即交换首元素与尾元素）
        nums[0], nums[i] = nums[i], nums[0]
        # 以根节点为起点，从顶至底进行堆化
        sift_down(nums, i, 0)

# 确保永远是最大堆
def heap_fix_down_max(A, i, n):
    # 找到这一个节点加子树的最大值
    largest = i
    left  =2*i + 1
    right = 2*i + 2
    # print(left, right)

    if left < n and A[left] > A[largest]:
        largest = left
    # 实际上这里largest要变
    if right < n and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        heap_fix_down_max(A, largest, n)
     



def heapsort(A):
    n = len(A)
    for i in range(n//2-1, -1, -1):
        # 从右下角开始，倒数第二排右下角的子树排好
        # 然后逐步递减，直到0
        # 把最大的放到第一个位置上
        heap_fix_down_max(A, i, n)
    
    for i in range(n-1, 0, -1):
        # 把最大的放回最后的位置，然后不算最大的那个
        A[0], A[i] = A[i], A[0]
        heap_fix_down_max(A, 0, i)


def heap_insert(A,x, n):
    A.append(x)
    n += 1
    heap_fix_up(A, n-1)


# i est l'indice de element
def heap_fix_up(A, i):
  p = (i - 1) // 2
  while p >= 0:
    if A[p] > A[i]:
        A[p], A[i] = A[i], A[p]
        i = p
        p = (i - 1) // 2
    else:
        break

def heap_del(A, x):
    i = A.index(x)
    n = len(A)
    A[i] = A[n-1]
    n = n-1
    A.pop()
    heap_fix_down(A, i, n)

def heap_fix_down(A, i, n):
    longest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and right < n:
        if A[longest] > A[left] and A[longest] > A[right] and left < n and right < n:
            if A[left] > A[right]:
                A[longest], A[right] = A[right], A[longest]
                longest = left
            else:
                A[longest], A[left] = A[left], A[i]
                longest = right
        elif A[longest] > A[left] and A[longest] < A[right] and left < n and right < n:
            A[longest], A[left] = A[left], A[longest]
            longest = left
        elif A[longest] > right and A[longest] < A[left]:
            A[longest], A[right] = A[right], A[longest]
            longest = right
    elif left < n and right > n:
        if A[longest] > A[left]:
            A[longest], A[left] = A[left], A[longest]
            longest = left

    # if left < n and A[left] < A[max]:
    #     max = left
    
    # if right < n and A[right] < A[max]:
    #     max = right
    if longest != i:
        # A[max], A[i] = A[i], A[max]
        heap_fix_down(A, longest, n)
    return



if __name__ == '__main__':
    n = 8
    B = [random.randint(2, 20) for _ in range(n)]   
    B = [2, 3, 13, 17, 14, 11, 18, 20]
    # heapsort(B)
    # print(B)
    A = []
    # n indice
    for i in range(8):
        a = random.randint(1, 50)
        print(f"a = {a}")
        heap_insert(A, x = a, n = i)
    
    print(A)
    print(a)
    heap_del(A, x = a)
    print(A)

    

    
    