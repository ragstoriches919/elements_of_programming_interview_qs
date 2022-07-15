class ListNode:
    def __init__(self, data = 0, next=None):
        self.data = data
        self.next = next

def delete_node_from_list(to_delete, head):
    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    while curr is not to_delete:
        prev = prev.next
        curr = curr.next

    prev.next = curr.next
    curr.next = None

