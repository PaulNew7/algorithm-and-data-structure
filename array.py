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

    def test_GetNumberOfK(self):
        '''
        测试用例
        '''
        test=[
        (range(10), 1, 1),
        (range(10), 10, 0),
        ([1,1,2,3,4,4,5], 2, 1),
        ([1,1,2,3,4,4,5], 4, 2),
        ([1,1,2,3,4,4,5], 6, 0),
        ([],1,0)
        ]
        #t=test[3]
        #print t
        #print '=====',s.GetNumberOfK(t[0],t[1])

        if 1:
            for t in test:
                res=s.GetNumberOfK(t[0],t[1])
                print '--------',res
                assert res==t[2], t

                res=s.GetNumberOfK2(t[0],t[1])
                print '2--------',res
                assert res==t[2], t

    def half_search(self, data, k):
        '''
        二分查找
        '''
        data.sort()
        left,right=0,len(data)
        while left<right:
            mid=data[(left+right)/2]
            if mid==k:
                return mid
            elif mid>k:
                #right=mid
                right=mid-1
            else:
                left=mid+1
        return None

    def half_search2(self, data, k):
        '''
        二分查找,
        返回所在index,不适合递归,适合判断是否在,以及个数
        '''
        data.sort()

        def _(s_data,k):
            if not s_data:
                return None
            mid=len(s_data)/2
            #if s_data[mid]==
            pass

    def sort_insert(self,l):
        '''
        插入排序

        '''
        if not l:
            l=[4,5,6,7,3,2,6,9,8]

        def insert_sort(ilist):
	        for i in range(len(ilist)):
	    	    for j in range(i):
	    	        if ilist[i] < ilist[j]:
	    	            ilist.insert(j, ilist.pop(i))
	    	            break
	        return ilist

        def self_do(l):
            for i in range(len(l)):
                for j in range(i):
                    if l[i]<l[j]: #
                        l.insert(j,l.pop(i)) # 内排序,移动到前j+1个元素该有的位置
                        break
            return l

        ilist = insert_sort(l)
        ilist2 = self_do(l)
        print ilist,ilist2
        assert ilist==ilist2

    def xier_sort(self,l):
        '''希尔排序
        将序列分为 len/2 列;
        对每列做插入排序;
        循环:列数减半
        '''
        def shell_sort(slist):
	        gap = len(slist)
	        while gap > 1:
	    	    gap = gap // 2
	    	    for i in range(gap, len(slist)):
	    	        #pdb.set_trace()
	    	        for j in range(i % gap, i, gap):
	    	            if slist[i] < slist[j]:
	    	                slist[i], slist[j] = slist[j], slist[i]
	        return slist
        shell_sort(l)

    def buble_sort(self,l,reverse=False):
        '''
        冒泡
        升序:
            从第一个元素开始,左到右依次比较,大就交换位置;
            右边界-1;循环,直到右边界为0
        '''
        nl=l[:]
        for r in range(len(l)-1,0,-1):
            for i in range(0,r):
                if reverse:
                    if l[i]<l[i+1]:
                        l[i],l[i+1]=l[i+1],l[i]
                else:
                    if l[i]>l[i+1]:
                        l[i],l[i+1]=l[i+1],l[i]
        print l,reverse,nl
        nl.sort(reverse=reverse)
        print l,reverse,nl
        assert l==nl
        return l

    def test_half_search(self):
        test=[
            (range(10),5,5),
            (range(10),10,None),
            ([],10,None),
        ]
        for t in test:
            res=self.half_search(t[0],t[1])
            assert res==t[2],'<<<<%s--%s'%(res,t)
            print 'done',t

if __name__=='__main__':
    s=Solution()
    unsort_list=[4,5,6,7,3,2,6,9,8]
    s.buble_sort(unsort_list)
    s.buble_sort(unsort_list,True)
    s.xier_sort(unsort_list)
    s.sort_insert(None)
    s.test_GetNumberOfK()
    s.test_half_search()
