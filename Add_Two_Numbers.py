class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # A dummy node to handle the result linked list
        current = dummy  # A pointer to construct the new linked list
        carry = 0  # Initialize carry to 0

        # Iterate as long as there is a node in l1, l2, or there is a carry left
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0  # Get value from l1 or 0 if l1 is None
            val2 = l2.val if l2 is not None else 0  # Get value from l2 or 0 if l2 is None
            
            # Calculate the sum and update the carry
            total = val1 + val2 + carry
            carry = total // 10
            sum_value = total % 10

            # Create a new node with the sum value
            current.next = ListNode(sum_value)
            current = current.next  # Move to the next node in the result list

            # Move to the next nodes in l1 and l2, if they are available
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next  # The first node is dummy, so we return the next node
