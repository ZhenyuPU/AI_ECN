# -*- coding: utf-8 -*-'

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        prev, slow, fast = None, head, head

        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next

        prev.next = None  # 将链表切断，分为head和slow两条子链

        """
        等价以下代码
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)
        """
        return self.merge(*map(self.sortList, (head, slow)))

    def merge(self, l1, l2):
        dummy = l = ListNode(None)

        while l1 and l2:
            if l1.val < l2.val:
                l.next, l, l1 = l1, l1, l1.next
            else:
                l.next, l, l2 = l2, l2, l2.next

        l.next = l1 or l2
        """
        l1,l2长度不一样时，l.next为l1,l2中比另一个长度长的子链
        如 l1: 1->2  l2: 3->4->5, l.next为5
        等价于以下代码
        if l1:
            l.next = l1
        else:
            l.next = l2
        """

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    l = head = ListNode(None)
    for val in [0, 4, 1, 6, 7]:
        l.next = ListNode(val)
        l = l.next

    li = s.sortList(head.next)
    while li:
        print li.val
        li = li.next

