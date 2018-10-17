# -*- coding:utf-8 -*-
import pdb
class Solution:
    def GetNumberOfK(self, data, k):
        '''
        统计一个数字在排序数组中出现的次数。(注意未明确升降序列)
        # todo 还是遍历了所有的元素,可以优化下
        '''
        # write code here
        if not data:
            return 0
        l=len(data)
        cnt=0
        mid=data[l/2]
        if mid==k:
            #pdb.set_trace()
            for i in range(l/2,l):
                if data[i]==k:
                    cnt+=1
            for i in range(l/2-1,-1,-1): # 注意可以遍历到0,故截至到-1
                if data[i]==k:
                    cnt+=1
            return cnt
        else:
            return self.GetNumberOfK(data[:l/2], k) + self.GetNumberOfK(data[l/2+1:], k) # 一定不能包括l/2本身,不然会无限递归

    def GetNumberOfK2(self, data, k):
        '''
        统计一个数字在排序数组中出现的次数。(注意未明确升降序列)
        # 优化后,利用有序的特征
        '''
        # write code here
        if not data:
            return 0
        l=len(data)
        cnt=0
        mid=data[l/2]
        if mid==k:
            #pdb.set_trace()
            l_find,r_find=False,False
            for i in range(l/2,l):
                if data[i]==k:
                    cnt+=1
                    r_find=True
                else:
                    if r_find:
                        break
            for i in range(l/2-1,-1,-1): # 注意可以遍历到0,故截至到-1
                if data[i]==k:
                    cnt+=1
                    l_find=True
                else:
                    if l_find:
                        break
            return cnt
        else:
            return self.GetNumberOfK(data[:l/2], k) + self.GetNumberOfK(data[l/2+1:], k) # 一定不能包括l/2本身,不然会无限递归


if __name__=='__main__':
    s=Solution()
    test=[
        (range(10), 1, 1),
        (range(10), 10, 0),
        ([1,1,2,3,4,4,5], 2, 1),
        ([1,1,2,3,4,4,5], 4, 2),
        ([1,1,2,3,4,4,5], 6, 0),
        ([],1,0)
    ]
    t=test[3]
    print t
    print '=====',s.GetNumberOfK(t[0],t[1])

    if 1:
        for t in test:
            res=s.GetNumberOfK(t[0],t[1])
            print '--------',res
            assert res==t[2], t

            res=s.GetNumberOfK(t[0],t[1])
            print '2--------',res
            assert res==t[2], t
