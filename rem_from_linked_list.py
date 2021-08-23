class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        out = []
        deleted = False
        while head.next:
            val = head.val
            head = head.next
            out.append(val)
        if not head.next:
            out.append(head.val)

        del out[-1 * n]

        output = None
        for i in range(1, len(out) + 1):
            output = ListNode(out[-1 * i], output)

        return output