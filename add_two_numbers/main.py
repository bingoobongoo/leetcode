class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def toList(self, node, list=[]):
        list.append(node.val)
        if node.next != None:
            return self.toList(node.next, list)
        if node.next == None:
            return list
    
    def toLinkedList(self, list):
        linkedList = []
        for i in range(len(list)):
            linkedList.append(ListNode(list[i]))
        for i in range(len(list)-1):
            linkedList[i].next = linkedList[i+1]
        
        return linkedList[0]


    def addTwoNumbers(self, l1, l2):
        list1 = self.toList(l1,[])
        list2 = self.toList(l2,[])
        print(list1)
        print(list2)
        if len(list1) > len(list2):
            for i in range(len(list2), len(list1)):
                list2.append(0)
        elif len(list2) > len(list1):
            for i in range(len(list1), len(list2)):
                list1.append(0)
        list3 = [0] * len(list1)
        for i in range(len(list1)):
            list3[i] += (list1[i]+list2[i])%10
            if list1[i] + list2[i] >= 10:
                try:
                    list3[i+1] += 1
                except:
                    list3.append(0)
                    list3[i+1] += 1
            if list3[i] >= 10:
                list3[i] = list3[i]%10
                try:
                    list3[i+1] += 1
                except:
                    list3.append(0)
                    list3[i+1] += 1
                
        l3 = self.toLinkedList(list3)
        return l3