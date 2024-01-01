# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        resultHead = resultNode = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                resultNode.next = list1
                resultNode = resultNode.next
                list1 = list1.next
            else:
                resultNode.next = list2
                resultNode = resultNode.next
                list2 = list2.next
        if list1:
            resultNode.next = list1
        if list2:
            resultNode.next = list2

        return resultHead.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listToLinkedList(list):
    if len(list) == 0:
        return None
    result = None
    prevNode = None
    for value in list:
        node = ListNode()
        node.val = value
        if prevNode is None:
            prevNode = node
            result = node
        else:
            prevNode.next = node
            prevNode = node
    return result


def printLinkedList(linkedList):
    if linkedList is None:
        print([])
        return
    list = [linkedList.val]
    while linkedList.next is not None:
        linkedList = linkedList.next
        list.append(linkedList.val)
    print(list)


# Test 1
list1_1 = listToLinkedList([1, 2, 4])
printLinkedList(list1_1)
list1_2 = listToLinkedList([1, 3, 4])
printLinkedList(list1_2)

solution = Solution()
list1_result = solution.mergeTwoLists(list1_1, list1_2)
printLinkedList(list1_result)

# Test 2
list1_1 = listToLinkedList([])
printLinkedList(list1_1)
list1_2 = listToLinkedList([])
printLinkedList(list1_2)

solution = Solution()
list1_result = solution.mergeTwoLists(list1_1, list1_2)
printLinkedList(list1_result)

# Test 3
list1_1 = listToLinkedList([0])
printLinkedList(list1_1)
list1_2 = listToLinkedList([])
printLinkedList(list1_2)

solution = Solution()
list1_result = solution.mergeTwoLists(list1_1, list1_2)
printLinkedList(list1_result)
