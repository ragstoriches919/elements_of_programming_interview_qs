# Putting together everything I know
# Pretty good!

class ListNode:
    def __init__(self, data=0, next = None):
        self.data = data
        self.next = next


def check_cycle(head):

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow

    return False


def check_no_cycle_overlap(L0, L1):

    def get_length(head):
        length = 0
        while head:
            length +=1
            head = head.next

        return length

    len_L0 = get_length(L0)
    len_L1 = get_length(L1)

    if len_L0 > len_L1:
        L0, L1 = L1, L0

    # Get L1 to start where L0 is at.
    for _ in range(abs(len_L0 - len_L1)):
        L1 = L1.next

    return L0 is L1


def check_overlaps_maybe_cycle(L0, L1):

    L0_cycle = check_cycle(L0)
    L1_cycle = check_cycle(L1)

    # One has a cycle, one doesn't
    if L0_cycle is not L1_cycle:
        return False

    # Both have cycles
    elif L0_cycle and L1_cycle == True:
        # Need to write the has_cycle() function that gets the root
        pass


    # Neither has a cycle
    elif not L0_cycle and not L1_cycle:
        return check_no_cycle_overlap(L0, L1)
