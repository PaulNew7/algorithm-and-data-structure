#encoding=utf8
'''
矩阵操作
'''
def gen(long_=4,width=4,start=1):
	'''
	生成制定宽高和起始值的矩阵
	'''
	res=[]
	for pre in range(0,long_*width,long_):
		l=[i+pre for i in range(start, long_+start)]
		res.append(l)
	return res


def clockwise(matrix):
	'''
	顺时针旋转多维数组
	'''
	if not matrix or not matrix[0]:
		return matrix
	
	done,res=[],[]
	import pdb
	i,j,ll,lw,circle=0,-1,len(matrix[0]),len(matrix),0
	while len(res)<ll*lw:
		# pdb.set_trace()
		print 1,done,res
		for j in range(j+1,ll-circle):
			if (i,j) in done:
				break
			done.append((i,j))
			res.append(matrix[i][j])
		print 2,done,res
		for i in range(i+1,lw-circle):
			if (i,j) in done:
				break
			done.append((i,j))
			res.append(matrix[i][j])
		print 3,done,res
		for j in range(j-1, -1+circle, -1):
			if (i,j) in done:
				break
			done.append((i,j))
			res.append(matrix[i][j])
		print 4,done,res
		for i in range(i-1, circle, -1):
			if (i,j) in done:
				break
			done.append((i,j))
			res.append(matrix[i][j])
		print 5,done,res
		circle+=1
		print circle
		
	print done, res,len(res),ll*lw
	return res


if __name__ == '__main__':
	print '--------------start'
	# print range(0,4*4,4)
	# print gen()
	# print gen(3,3)
	# print gen(3,4)
	# print gen(3,3,0)
	clockwise(gen())
	m=[[1],[2],[3],[4],[5]]
	print clockwise(m)
	print gen(5,1)
	print clockwise(gen(5,1))
	print gen(1,5)
	print clockwise(gen(1,5))

