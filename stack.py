#encoding=utf8
'''
栈
'''
# -*- coding:utf-8 -*-
import pdb
class Solution:
    def IsPopOrder(self, pushV, popV):
        '''
        判断popV是否为栈pushV出栈的一种情况
        '''
        # write code here
        stack=[]
        debug=0
        print pushV, popV,'------------'
        while pushV:
            while not stack and pushV and popV and pushV[0]==popV[-1]:
                if debug:
                    pdb.set_trace()
                pushV.pop(0)
                popV.pop()
            if pushV:
                stack.append(pushV.pop(0)) # 模拟创建

            while stack and popV and stack[-1]==popV[0]:
                if debug:
                    pdb.set_trace()
                stack.pop()
                popV.pop(0)
        print popV, stack
        if stack:
            return False
        return True

    def retry(self, lin, lout):
        new=[]
        print lin, lout,'-----2-------'
        while lin:
            while not new and lin and lout and lin[-1]==lout[0]:
                lin.pop()
                lout.pop(0)
            if lin: # 必须写这里!!!!
                new.append(lin.pop(0))
            while new and new[-1]==lout[0]:
                #pdb.set_trace()
                new.pop()
                lout.pop(0)

        print lout,new,'-----22-------'
        if not new:
            return True
        else:
            return False


if __name__ == '__main__':
    print '--------------start'
    S=Solution()
    p1=range(1,6)
    p2=[5,4,3,2,1]
    p3=[4,5,3,2,1]
    p4=[3,4,5,3,2,1] # 有问题
    p5=[3,4,5,2,1]
    p6=[4,3,5,1,2]
    #print S.IsPopOrder(range(1,6), p2)
    # S.IsPopOrder(range(1,6), p3)
    # S.IsPopOrder(range(1,6), p4)
    # S.IsPopOrder(range(1,6), p5)
    #print S.IsPopOrder(range(1,6), p6)

    #assert S.retry(range(1,6), p2[:])== S.IsPopOrder(range(1,6), p2[:])
    assert S.retry(range(1,6), p3[:])== S.IsPopOrder(range(1,6), p3[:])
    assert S.retry(range(1,6), p4[:])== S.IsPopOrder(range(1,6), p4[:])
    assert S.retry(range(1,6), p5[:])== S.IsPopOrder(range(1,6), p5[:])
    assert S.retry(range(1,6), p6[:])== S.IsPopOrder(range(1,6), p6[:])
