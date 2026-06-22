# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        from collections import deque
        container=deque()
        itenode=head
        while itenode is not None:
            container.append(itenode.val)
            itenode=itenode.next
        result=0
        while container:
            front=container.popleft()
            back=container.pop()
            result=max(result,front+back)
        return result
        