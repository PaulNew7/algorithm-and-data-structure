# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        new,val_list=None,[pHead.val]
        while pHead.next:
            val_list.append(pHead.next.val)
            pHead=pHead.next

        val_list.reverse()
        new=ListNode(val_list[0])
        now=new
        for i in val_list[1:]:
            node=ListNode(i)
            now.next=node
            now=node
        return new

    def gen(self, val_list):
        if not val_list:
            return None
        new=ListNode(val_list[0])
        now=new
        for i in val_list[1:]:
            node=ListNode(i)
            now.next=node
            now=node
        return new

    def print_(self, head):
        if not head:
            print 'None'

        done=[id(head)]
        now=head
        print now.val

        while now.next:
            if id(now.next) in done:
                print '-------cricle!'
                break
            print now.next.val
            now=now.next


if __name__=='__main__':
    s=Solution()
    raw=s.gen(range(10))
    s.print_(raw)
    print '--------------------reverse'
    s.print_(s.ReverseList(raw))

