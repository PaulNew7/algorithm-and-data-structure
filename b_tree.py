#encoding=utf8
'''
二叉树相关
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bulid(pre, mid):
    '''
    pre: 前序遍历
    mid: 中序遍历
    '''
    if not pre:
        return None
    r=pre[0]
    new=TreeNode(r)
    index=mid.index(r)
    new.left=bulid(pre[1:index+1],mid[:index])
    new.right=bulid(pre[index+1:],mid[index+1:])
    return new

def pre_run(r):
    '''
    前序遍历
    '''
    if not r:
        return ''
    return str(r.val)+pre_run(r.left)+pre_run(r.right)


def mid_run(r): # todo error!
    '''
    中序遍历
    '''
    if not r:
        return ''
    return mid_run(r.left)+str(r.val)+mid_run(r.right)



class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        def gen(r):
            if not r:
                return None
            new=TreeNode(r.val)
            if r.left:
                new.right=gen(r.left)
            if r.right:
                new.left=gen(r.right)
            return new
        return gen(root)


    def Mirror2(self, root):
        if root != None:
            root.left,root.right = root.right,root.left
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root

    def printit(self, root):
        '''
        从上到下，逐行打印
        '''
        if not root:
            return []
        from collections import defaultdict
        res=defaultdict(list)
        fuck_res=[]
        def _(r, i):
            res[i].append(r.val)
            if r.left:
                _(r.left, i+1)
            if r.right:
                _(r.right, i+1)
            return 
        _(root,0)
        for i in range(len(res)):#todo
            # if not res.get(i):
            #     print '=====done==='
            #     break
            print '\t'.join(map(str,res[i]))
            fuck_res.extend(res[i])
        return fuck_res



if __name__ == '__main__':
    print '------------------start'
    def gen(ttype='single'):
        pre=['a','b','e','f','c','d','g']
        mid=['e','b','f','a','d','g','c']
        t1=bulid(pre,mid)
        try:
            assert pre_run(t1)==''.join(pre) and mid_run(t1)==''.join(mid), 'check tree error'
        except:
            print pre_run(t1), mid_run(t1)

        if ttype=='single':
            return t1
        else:
            raise Exception('no support')

    t=gen()
    print '------------------',t

    # mirror=Solution().Mirror(t)
    # mirror2=Solution().Mirror2(t)
    # print '--------',pre_run(mirror), mid_run(mirror)
    # print '--------',pre_run(mirror2), mid_run(mirror2)
        
    Solution().printit(t)