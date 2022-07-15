# Already looked at answer, and at this youtube explanation: https://www.youtube.com/watch?v=gBTe7lFR3vc

def is_list_cyclic(head):

    def cycle_len(end):
        start = end
        step = 0
        while True:
            start = start.next
            step +=1
            if start == end:
                return step

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:

            num_steps_to_end = cycle_len(slow)
            cycle_len_adv_iter = head
            for _ in range(num_steps_to_end):
                cycle_len_adv_iter = cycle_len_adv_iter.next

            it = head
            while it is not cycle_len_adv_iter:
                it = it.next
                cycle_len_adv_iter = cycle_len_adv_iter.next

            return it

    return None

