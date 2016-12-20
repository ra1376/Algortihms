x=3;
y=5;
z=7;
if x%2 == 0:
	print 'x is even'
else:
	print 'x is odd'
if y%2 == 0:
	print 'y is even'
else:
	print 'y is odd'
if z%2 == 0:
	print 'z is even'
else:
	print 'z is odd'
print 'the block started'

if x%2 != 0 or y%2 !=0 or z%2 != 0:
	if x>y and x>z:
		print 'x is largest odd number',x
elif y>x and y>z:
	print 'y is largest odd number',y
elif z>x and z>y:
	print 'z is largest odd number',z




