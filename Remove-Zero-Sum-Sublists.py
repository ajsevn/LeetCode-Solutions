class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_map = {0: dummy}
        
        current = head
        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_map:
                node = prefix_map[prefix_sum].next
                sum_in_between = prefix_sum
                while node != current:
                    sum_in_between += node.val
                    del prefix_map[sum_in_between]
                    node = node.next
                prefix_map[prefix_sum].next = current.next
            else:
                prefix_map[prefix_sum] = current
            current = current.next
        
        return dummy.next

# Example Usage
def list_to_linkedlist(arr):
    head = ListNode(arr[0])
    current = head
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    head1 = list_to_linkedlist([1, 2, -3, 3, 1])
    new_head1 = solution.removeZeroSumSublists(head1)
    print(linkedlist_to_list(new_head1))  # Output: [3, 1]

    # Example 2
    head2 = list_to_linkedlist([1, 2, 3, -3, 4])
    new_head2 = solution.removeZeroSumSublists(head2)
    print(linkedlist_to_list(new_head2))  # Output: [1, 2, 4]

    # Example 3
    head3 = list_to_linkedlist([1, 2, 3, -3, -2])
    new_head3 = solution.removeZeroSumSublists(head3)
    print(linkedlist_to_list(new_head3))  # Output: [1]
