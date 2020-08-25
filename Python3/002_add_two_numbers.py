#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    :   002_add_two_numbers.py
@Time    :   2020/08/22 16:55
@Author  :   TrenywanG
@Version :   1.0
@Contact :   brtxbrc0521@126.com
"""


# here put the import lib
class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    # def gatherAttrs(self):
    #     return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())
    #
    # def __str__(self):
    #     return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"

def printBackward(listnode):
    if listnode == None:return
    printBackward(listnode.next)
    print(listnode.val) #调换以上两句的顺序即可完成顺序打印



class Solution:
    def addTwoNumbers(self, l1, l2, ):
        def list_str(list):
            result = []
            while list:
                result.append(str(list.val))
                list = list.next
            return result

        def str_list(res):
            ResList = ListNode(int(res[0]))
            dummy = ResList
            for i in range(1, len(res)):
                ResList.next = ListNode(int(res[i]))
                ResList = ResList.next
            return dummy

        res1 = ''.join(list_str(l1))[::-1]
        res2 = ''.join(list_str(l2))[::-1]
        res = str(int(res1) + int(res2))[::-1]
        return str_list(res)


if __name__ == "__main__":
    solution1 = Solution()
    l1 = ListNode([2, 4, 3])
    l2 = ListNode([5, 6, 4])
    printBackward(solution1.addTwoNumbers(l1, l2))
    # print(solution1.addTwoNumbers(l1,l2))
