class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_out = []
        while l1 is not None:
            ele1 = l1.val
            if l2 is None:
                l_out.append(ele1)
                l1 = l1.next
            elif l2.val > ele1:
                l_out.append(ele1)
                l1 = l1.next
            elif ele1 > l2.val:
                l_out.append(l2.val)
                l2 = l2.next
            elif ele1 == l2.val:
                l_out.append(ele1)
                l_out.append(l2.val)
                l1 = l1.next
                l2 = l2.next

        while l2 is not None:
            ele2 = l2.val
            l_out.append(ele2)
            l2 = l2.next

        l_n_out = None
        for i in range(1, len(l_out) + 1):
            l_n_out = ListNode(l_out[-1 * i], l_n_out)

        return l_n_out