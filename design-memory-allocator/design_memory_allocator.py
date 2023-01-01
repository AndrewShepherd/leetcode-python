class ListNode:
    def __init__(self, size: int, mID, next):
        self.size = size
        self.mID = mID
        self.next = next

def iterate_through_list(node):
    while(node):
        yield node
        node = node.next

class Allocator:

    def __init__(self, n: int):
        self.head = ListNode(0, -1, None)
        
        tailNode = ListNode(0, -1, None)

        actualNode = ListNode(n, None, tailNode)
        self.head.next = actualNode


    def allocate(self, size: int, mID: int) -> int:
        index = 0
        for node in iterate_through_list(self.head):
            if node.mID == None and node.size >= size:
                node.mID = mID
                if size < node.size:
                    newNode = ListNode(node.size-size, None, node.next)
                    node.size = size
                    node.next = newNode
                return index
            index += node.size
        return -1


    def free(self, mID: int) -> int:
        nodes = [n for n in iterate_through_list(self.head) if n.mID == mID]
        total_size = sum([n.size for n in nodes])
        for n in nodes:
            n.mID = None
        n = self.head
        while(n):
            while n.mID == None and n.next.mID == None:
                nodeToGo = n.next
                n.size += nodeToGo.size
                n.next = nodeToGo.next
            n = n.next
        return total_size


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)