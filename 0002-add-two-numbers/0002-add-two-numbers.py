# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            curr_sum = digit1 + digit2 + carry
            digit = curr_sum % 10
            carry = curr_sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
    
    """
    Explanation:
Create a placeholder node called dummyHead with a value of 0. This node will hold the resulting linked list.
Initialize a pointer called tail and set it to dummyHead. This pointer will keep track of the last node in the result list.
Initialize a variable called carry to 0. This variable will store the carry value during addition.
Start a loop that continues until there are no more digits in both input lists (l1 and l2) and there is no remaining carry value.
Inside the loop:
Check if there is a digit in the current node of l1. If it exists, assign its value to a variable called digit1. Otherwise, set digit1 to 0.
Check if there is a digit in the current node of l2. If it exists, assign its value to a variable called digit2. Otherwise, set digit2 to 0.
Add the current digits from l1 and l2, along with the carry value from the previous iteration, and store the sum in a variable called sum.
Calculate the unit digit of sum by taking the modulus (%) of sum by 10. This digit will be placed in a new node for the result.
Update the carry variable by dividing sum by 10 and taking the integer division (/) part. This gives us the carry value for the next iteration.
Create a new node with the calculated digit as its value.
Attach the new node to the tail node of the result list.
Move the tail pointer to the newly added node.
Move to the next nodes in both l1 and l2, if they exist. If either list is exhausted, set the corresponding pointer to nullptr.
After the loop, obtain the actual result list by skipping the dummyHead node.
Delete the dummyHead node.
Return the resulting list.
    """
        