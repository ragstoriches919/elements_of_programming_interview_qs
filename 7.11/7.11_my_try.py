# My try after I alredy saw the answer...https://www.youtube.com/watch?v=yOzXms1J6Nk
# Better to use youtube than the EPI book

# And, it's absolutely perfect.
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = None


def check_sll_palindrome(L):

    slow = fast = L

    # Get to the halfway point of the list
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse the second half of the list
    prev = None
    while slow:
        tempNext = slow.next
        slow.next = prev
        prev = slow
        slow = tempNext

    # Compare the left and right parts of the new list
    left = L
    right = prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next

    return True


