# -*- coding:utf-8 -*-
'''
链表
'''
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

    def val_list(self, head):
        '''
        提取链表元素
        '''
        if not head:
            return []

        l=[head.val]
        while head.next:
            head=head.next
            l.append(head.val)

        return l

    def merge(self, head1, head2):
        '''
        输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
        '''
        if not head1:
            return head2
        if not head2:
            return head1

        l1,l2=self.val_list(head1), self.val_list(head2)
        l=l1+l2
        l.sort()
        return self.gen(l)


if __name__=='__main__':
    s=Solution()
    raw=s.gen(range(10))
    s.print_(raw)
    print '--------------------reverse'
    s.print_(s.ReverseList(raw))
    print '--------------------merge'
    raw2=s.gen(range(9,12))
    s.print_(raw2)
    print '--merge done'
    s.print_(s.merge(raw,raw2))
