r1 = int(input ("введи r1 "))
r2 = int(input ("введи r2 "))
r3 = int(input ("введи r3 "))
s1 = int(input ("введи s1 "))
s2 = int(input ("введи s2 "))
s3 = int(input ("введи s3 "))
x1 = r1/s1
x2 = r2/s2
x3 = r3/s3
if (x1>x2) and (x1>x3):
	print ('1')
if (x2>x1) and (x2>x3):
	print ('2')
if (x3>x1) and (x3>x1):
	print ('3')

