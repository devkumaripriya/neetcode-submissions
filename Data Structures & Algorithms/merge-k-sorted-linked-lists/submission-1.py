import heapq

class Solution:
    def mergeKLists(self, lists):

        min_heap = []

        # Add first node of every linked list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(
                    min_heap, (node.val, i, node)
                )

        dummy = ListNode(0)
        current = dummy

        while min_heap:

            val, i, node = heapq.heappop(min_heap)

            current.next = node
            current = current.next

            # Add next node from the same list
            if node.next:
                heapq.heappush(
                    min_heap,
                    (node.next.val, i, node.next)
                )

        current.next = None

        return dummy.next