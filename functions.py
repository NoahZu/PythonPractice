#函数作为参数
f = lambda x,y:x+y
def test(f,a,b):
	print 'test'
	print f(a,b)

test(f,3,5)