class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        temp = self.head.next
        i = 0
        while(temp):
            if i == index:
                return temp.val
            i += 1
            temp = temp.next
        return -1

    def insertHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head.next
        self.head.next = temp
        if not temp.next:
            self.tail = temp

    def insertTail(self, val: int) -> None:
        temp = Node(val)
        self.tail.next = temp
        self.tail = temp
        

    def remove(self, index: int) -> bool:
        before = self.head
        i = 0
        while i < index and before:
            i += 1
            before = before.next

        if before and before.next:
            if before.next == self.tail:
                self.tail = before
            before.next = before.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        temp = self.head.next
        values = []

        while temp:
            values.append(temp.val)
            temp = temp.next

        
        return values
        
