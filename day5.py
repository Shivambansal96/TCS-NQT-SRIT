

# class Node:

#     def __init__(self, data):
#         self.data = data # currentValue
#         self.next = None # memory address

# Node1 = Node(5)
# Node2 = Node(10)
# Node3 = Node(15)
# Node4 = Node(20)
# Node5 = Node(25)
# Node6 = Node(30)
# Node7 = Node(290)

# Node1.next = Node2
# Node1.next.next = Node3
# Node1.next.next.next = Node5
# # Node1.next.next.next.next = Node5
# Node1.next.next.next.next = Node6
# Node1.next.next.next.next.next = Node7

# #insert at the beginning
# head = Node(2)
# head.next = Node1

# currentNode = head
# while currentNode != None:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next

# print(None)






# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         newNode = Node(data)

#         if not self.head:
#             self.head = newNode
#             return
        
#         currentNode = self.head

#         while currentNode.next:
#             currentNode = currentNode.next

#         currentNode.next = newNode

#     def printList(self):
#         currentNode = self.head

#         while currentNode:
#             print(currentNode.data, end=" -> ")
#             currentNode = currentNode.next

#         print(None)

#     def deleteNode(self, value):
#         temp = Node(0)

#         temp.next = self.head

#         currentValue = temp
#         while currentValue.next:
#             if(currentValue.next.data == value):
#                 currentValue.next = currentValue.next.next
#                 break
            
#             currentValue = currentValue.next

#         self.head = temp



# li = LinkedList()
# li.append(5)
# li.append(15)
# li.append(57)
# li.append(54000)

# print("original List:", end=" ")
# li.printList()

# li.deleteNode(57)

# print("Updated List:", end=" ")
# li.printList()

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# def mergeLinkedLists(head1, head2):
#     temp = Node(0)
#     tail = temp

#     while head1 and head2:
#         if head1.data <= head2.data:
#             tail.next = head1
#             head1 = head1.next
#         else:
#             tail.next = head2
#             head2 = head2.next

#         tail = tail.next

#     if head1:
#         tail.next = head1
#     if head2:
#         tail.next = head2

#     return temp.next



# a = Node(5)
# a.next = Node(10)
# a.next.next = Node(15)

# b = Node(2)
# b.next = Node(4)
# b.next.next = Node(6)

# res = mergeLinkedLists(a, b)

# current = res
# while current:
#     print(current.data, end=" -> ")
#     current = current.next

# print(None)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print(None)

def reverseLinkedList(head):
    prev = None
    current = head

    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)


res = reverseLinkedList(head)
printList(res)

